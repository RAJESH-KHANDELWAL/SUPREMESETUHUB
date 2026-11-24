"""LINKSETU status experience service."""


class LinkSetuStatusService:
    """Manage temporary user status updates in LINKSETU."""

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

    def create_status(
        self,
        user_id: str,
        content: str = "",
        media_url: str | None = None,
        media_type: str = "text",
        expires_at: str | None = None,
    ) -> dict:
        if media_type not in self.allowed_media_types:
            raise ValueError(
                f"Unsupported status media type: {media_type}"
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

    def get_status(self, status_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "status_id": status_id,
            "status": "active",
        }

    def get_user_statuses(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "statuses": [],
        }

    def get_status_feed(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "statuses": [],
        }

    def mark_status_viewed(
        self,
        user_id: str,
        status_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "status_id": status_id,
            "status": "viewed",
        }

    def delete_status(self, status_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "status_id": status_id,
            "status": "deleted",
        }

    def archive_status(self, status_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "status_id": status_id,
            "status": "archived",
        }

    def update_status_state(
        self,
        status_id: str,
        state: str,
    ) -> dict:
        if state not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported status state: {state}"
            )

        return {
            "platform": self.platform_name,
            "status_id": status_id,
            "status": state,
        }
