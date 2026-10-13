from __future__ import annotations

from backend.database.service import DatabaseService
from backend.platform.linksetu.notification.service import LinkSetuNotificationService
from backend.platform.linksetu.social.service import LinkSetuSocialService


def _service(tmp_path):
    db = DatabaseService(str(tmp_path / "social.db"))
    notifications = LinkSetuNotificationService(db)
    return LinkSetuSocialService(db, notifications), db


def test_post_comment_reaction_follow_persist_and_notify_only_target(tmp_path):
    service, db = _service(tmp_path)
    post = service.create_post("ram", "Hello LinkSetu")
    service.react("shyam", post["post_id"], "like")
    service.add_comment("shyam", post["post_id"], "Nice post")
    service.follow("shyam", "ram")

    assert service.list_posts()[0]["post_id"] == post["post_id"]
    assert service.get_comments(post["post_id"])[0]["content"] == "Nice post"
    assert service.get_reactions(post["post_id"])["reactions"] == {"like": 1}
    assert service.followers("ram") == ["shyam"]
    assert service.notifications.get_notifications("ram")["unread_count"] == 3
    assert service.notifications.get_notifications("shyam")["notifications"] == []
    db.close()


def test_reaction_is_unique_per_user_and_unfollow_is_scoped(tmp_path):
    service, db = _service(tmp_path)
    post = service.create_post("ram", "Post")
    service.react("shyam", post["post_id"], "like")
    service.react("shyam", post["post_id"], "love")
    assert service.get_reactions(post["post_id"])["reactions"] == {"love": 1}
    service.follow("shyam", "ram")
    service.follow("geeta", "ram")
    service.unfollow("shyam", "ram")
    assert service.followers("ram") == ["geeta"]
    db.close()


def test_users_cannot_follow_themselves_or_react_to_missing_post(tmp_path):
    service, db = _service(tmp_path)
    import pytest
    with pytest.raises(ValueError, match="cannot follow themselves"):
        service.follow("ram", "ram")
    with pytest.raises(LookupError, match="POST_NOT_FOUND"):
        service.react("shyam", "missing-post", "like")
    db.close()
