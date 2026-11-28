"""LINKSETU story experience service."""


class LinkSetuStoryService:
    """Manage temporary story experiences in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_media_types = (
        "text",
        "image",
        "video",
        "audio",
    )

    allowed_statuses = (
        "active",
        "expired",
        "archived",
        "deleted",
    )

    def create_story(
        self,
        user_id: str,
        content: str = "",
        media_url: str | None = None,
        media_type: str = "text",
        expires_at: str | None = None,
    ) -> dict:
        if media_type not in self.allowed_media_types:
            raise ValueError(
                f"Unsupported story media type: {media_type}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "content": content,
            "media_url": media_url,
            "media_type": media_type,
            "expires_at": expires_at,
            "status": "active",
        }

    def get_story(self, story_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "story_id": story_id,
            "status": "active",
        }

    def get_user_stories(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "stories": [],
        }

    def get_story_feed(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "stories": [],
        }

    def mark_story_viewed(
        self,
        user_id: str,
        story_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "story_id": story_id,
            "status": "viewed",
        }

    def delete_story(self, story_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "story_id": story_id,
            "status": "deleted",
        }

    def archive_story(self, story_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "story_id": story_id,
            "status": "archived",
        }

    def update_story_status(
        self,
        story_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported story status: {status}"
            )

        return {
            "platform": self.platform_name,
            "story_id": story_id,
            "status": status,
        }
