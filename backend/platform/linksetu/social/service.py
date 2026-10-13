"""Persistent LINKSETU posts, comments, reactions, and follows."""
from __future__ import annotations

from typing import Any
from uuid import uuid4

from backend.database.service import DatabaseService
from backend.platform.linksetu.notification.service import LinkSetuNotificationService


class LinkSetuSocialService:
    """Store social actions in the central DB and notify only target owners."""

    def __init__(self, database: DatabaseService | None = None, notifications: LinkSetuNotificationService | None = None):
        self.database = database or DatabaseService()
        self.notifications = notifications or LinkSetuNotificationService(self.database)
        self.initialize()

    def initialize(self) -> None:
        self.database.execute("""CREATE TABLE IF NOT EXISTS linksetu_posts (
            post_id TEXT PRIMARY KEY, user_id TEXT NOT NULL, content TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)""")
        self.database.execute("""CREATE TABLE IF NOT EXISTS linksetu_comments (
            comment_id TEXT PRIMARY KEY, post_id TEXT NOT NULL, user_id TEXT NOT NULL,
            content TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(post_id) REFERENCES linksetu_posts(post_id) ON DELETE CASCADE)""")
        self.database.execute("""CREATE TABLE IF NOT EXISTS linksetu_reactions (
            post_id TEXT NOT NULL, user_id TEXT NOT NULL, reaction TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(post_id, user_id),
            FOREIGN KEY(post_id) REFERENCES linksetu_posts(post_id) ON DELETE CASCADE)""")
        self.database.execute("""CREATE TABLE IF NOT EXISTS linksetu_follows (
            follower_id TEXT NOT NULL, following_id TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(follower_id, following_id),
            CHECK(follower_id != following_id))""")
        self.database.execute("CREATE INDEX IF NOT EXISTS idx_linksetu_posts_user ON linksetu_posts(user_id, created_at DESC)")
        self.database.execute("CREATE INDEX IF NOT EXISTS idx_linksetu_comments_post ON linksetu_comments(post_id, created_at)")

    @staticmethod
    def _dict(row: Any) -> dict[str, Any] | None:
        return dict(row) if row is not None else None

    def create_post(self, user_id: str, content: str) -> dict[str, Any]:
        actor, body = str(user_id or "").strip(), str(content or "").strip()
        if not actor or not body:
            raise ValueError("user_id and content are required")
        post_id = f"LSP-{uuid4().hex}"
        self.database.execute("INSERT INTO linksetu_posts(post_id,user_id,content) VALUES(?,?,?)", (post_id, actor, body))
        return self._dict(self.database.fetchone("SELECT * FROM linksetu_posts WHERE post_id=?", (post_id,))) or {}

    def list_posts(self, limit: int = 50) -> list[dict[str, Any]]:
        safe_limit = max(1, min(int(limit), 100))
        return [dict(row) for row in self.database.fetchall(
            "SELECT * FROM linksetu_posts ORDER BY created_at DESC, post_id DESC LIMIT ?", (safe_limit,))]

    def _post(self, post_id: str) -> dict[str, Any]:
        row = self.database.fetchone("SELECT * FROM linksetu_posts WHERE post_id=?", (post_id,))
        if row is None:
            raise LookupError("POST_NOT_FOUND")
        return dict(row)

    def add_comment(self, user_id: str, post_id: str, content: str) -> dict[str, Any]:
        actor, body = str(user_id or "").strip(), str(content or "").strip()
        if not actor or not body:
            raise ValueError("user_id and content are required")
        post = self._post(post_id)
        comment_id = f"LSC-{uuid4().hex}"
        self.database.execute("INSERT INTO linksetu_comments(comment_id,post_id,user_id,content) VALUES(?,?,?,?)",
                              (comment_id, post_id, actor, body))
        comment = self._dict(self.database.fetchone("SELECT * FROM linksetu_comments WHERE comment_id=?", (comment_id,))) or {}
        if post["user_id"] != actor:
            self.notifications.create_notification(post["user_id"], "COMMENT", "Someone commented on your post", actor, post_id)
        return comment

    def get_comments(self, post_id: str) -> list[dict[str, Any]]:
        self._post(post_id)
        return [dict(row) for row in self.database.fetchall(
            "SELECT * FROM linksetu_comments WHERE post_id=? ORDER BY created_at, comment_id", (post_id,))]

    def react(self, user_id: str, post_id: str, reaction: str = "like") -> dict[str, Any]:
        actor, kind = str(user_id or "").strip(), str(reaction or "").strip().lower()
        if not actor:
            raise ValueError("user_id is required")
        if kind not in {"like", "love", "support", "celebrate", "laugh", "sad", "angry"}:
            raise ValueError("UNSUPPORTED_REACTION")
        post = self._post(post_id)
        previous = self.database.fetchone("SELECT reaction FROM linksetu_reactions WHERE post_id=? AND user_id=?", (post_id, actor))
        self.database.execute("""INSERT INTO linksetu_reactions(post_id,user_id,reaction) VALUES(?,?,?)
            ON CONFLICT(post_id,user_id) DO UPDATE SET reaction=excluded.reaction""", (post_id, actor, kind))
        if previous is None and post["user_id"] != actor:
            self.notifications.create_notification(post["user_id"], "LIKE" if kind == "like" else "REACTION",
                                                   "Someone liked your post" if kind == "like" else "Someone reacted to your post",
                                                   actor, post_id)
        return {"post_id": post_id, "user_id": actor, "reaction": kind, "status": "added"}

    def remove_reaction(self, user_id: str, post_id: str) -> dict[str, Any]:
        self._post(post_id)
        self.database.execute("DELETE FROM linksetu_reactions WHERE post_id=? AND user_id=?", (post_id, str(user_id)))
        return {"post_id": post_id, "user_id": str(user_id), "status": "removed"}

    def get_reactions(self, post_id: str) -> dict[str, Any]:
        self._post(post_id)
        rows = self.database.fetchall("SELECT reaction, COUNT(*) AS total FROM linksetu_reactions WHERE post_id=? GROUP BY reaction", (post_id,))
        return {"post_id": post_id, "reactions": {row["reaction"]: int(row["total"]) for row in rows}}

    def follow(self, follower_id: str, following_id: str) -> dict[str, Any]:
        follower, following = str(follower_id or "").strip(), str(following_id or "").strip()
        if not follower or not following:
            raise ValueError("follower_id and following_id are required")
        if follower == following:
            raise ValueError("A person cannot follow themselves.")
        cursor = self.database.execute("INSERT OR IGNORE INTO linksetu_follows(follower_id,following_id) VALUES(?,?)", (follower, following))
        if cursor.rowcount and follower != following:
            self.notifications.create_notification(following, "FOLLOW", "Someone started following you", follower, following)
        return {"follower_id": follower, "following_id": following, "status": "following"}

    def unfollow(self, follower_id: str, following_id: str) -> dict[str, Any]:
        self.database.execute("DELETE FROM linksetu_follows WHERE follower_id=? AND following_id=?", (str(follower_id), str(following_id)))
        return {"follower_id": str(follower_id), "following_id": str(following_id), "status": "unfollowed"}

    def followers(self, user_id: str) -> list[str]:
        return [row["follower_id"] for row in self.database.fetchall("SELECT follower_id FROM linksetu_follows WHERE following_id=? ORDER BY created_at", (str(user_id),))]

    def following(self, user_id: str) -> list[str]:
        return [row["following_id"] for row in self.database.fetchall("SELECT following_id FROM linksetu_follows WHERE follower_id=? ORDER BY created_at", (str(user_id),))]
