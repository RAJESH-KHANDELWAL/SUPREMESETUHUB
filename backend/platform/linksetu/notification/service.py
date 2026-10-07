"""LINKSETU notification experience service."""


class LinkSetuNotificationService:
    """Manage LINKSETU notification experience."""

    platform_name = "LINKSETU"

    def create_notification(
        self,
        user_id: str,
        notification_type: str,
        message: str,
        actor_id: str | None = None,
        target_id: str | None = None,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "notification_type": notification_type,
            "message": message,
            "actor_id": actor_id,
            "target_id": target_id,
            "status": "created",
        }

    def get_notifications(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "notifications": [],
        }

    def mark_as_read(
        self,
        notification_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "notification_id": notification_id,
            "status": "read",
        }

    def mark_all_as_read(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "status": "all_read",
        }
