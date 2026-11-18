from backend.database.service import DatabaseService
from backend.platform.linksetu.notification.service import LinkSetuNotificationService


def test_notifications_are_persisted_and_scoped_to_each_user(tmp_path):
    database_path = str(tmp_path / "notifications.db")
    service = LinkSetuNotificationService(DatabaseService(database_path))
    try:
        ram_notice = service.create_notification(
            user_id="ram",
            notification_type="LIKE",
            message="Someone liked your post",
            actor_id="shyam",
            target_id="post-1",
        )
        service.create_notification(
            user_id="shyam",
            notification_type="COMMENT",
            message="Someone commented on your post",
            actor_id="ram",
            target_id="post-2",
        )

        assert ram_notice["notification_id"].startswith("NTF-")
        assert service.get_notifications("ram")["notifications"][0]["message"] == "Someone liked your post"
        assert len(service.get_notifications("ram")["notifications"]) == 1
        assert len(service.get_notifications("shyam")["notifications"]) == 1
        assert service.get_notifications("ram")["unread_count"] == 1
    finally:
        service.database.close()

    reopened = LinkSetuNotificationService(DatabaseService(database_path))
    try:
        assert len(reopened.get_notifications("ram")["notifications"]) == 1
        assert reopened.get_notifications("ram")["unread_count"] == 1
    finally:
        reopened.database.close()


def test_user_cannot_mark_another_users_notification_as_read(tmp_path):
    service = LinkSetuNotificationService(DatabaseService(str(tmp_path / "notification-access.db")))
    try:
        notice = service.create_notification(
            user_id="ram",
            notification_type="FOLLOW",
            message="Shyam followed you",
            actor_id="shyam",
        )

        denied = service.mark_as_read(notice["notification_id"], user_id="shyam")
        assert denied["status"] == "not_found"
        assert service.get_notifications("ram")["unread_count"] == 1

        allowed = service.mark_as_read(notice["notification_id"], user_id="ram")
        assert allowed["status"] == "read"
        assert service.get_notifications("ram")["unread_count"] == 0
    finally:
        service.database.close()


def test_mark_all_as_read_only_updates_the_requesting_users_notifications(tmp_path):
    service = LinkSetuNotificationService(DatabaseService(str(tmp_path / "notification-mark-all.db")))
    try:
        service.create_notification("ram", "LIKE", "Ram notice")
        service.create_notification("ram", "COMMENT", "Ram another notice")
        service.create_notification("shyam", "FOLLOW", "Shyam notice")

        result = service.mark_all_as_read("ram")
        assert result["updated_count"] == 2
        assert service.get_notifications("ram")["unread_count"] == 0
        assert service.get_notifications("shyam")["unread_count"] == 1
    finally:
        service.database.close()
