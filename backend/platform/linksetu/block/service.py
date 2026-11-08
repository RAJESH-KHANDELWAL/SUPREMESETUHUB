"""LINKSETU block experience service."""


class LinkSetuBlockService:
    """Manage user blocking in LINKSETU."""

    platform_name = "LINKSETU"

    def block_user(
        self,
        user_id: str,
        blocked_user_id: str,
    ) -> dict:

        if user_id == blocked_user_id:
            raise ValueError(
                "A person cannot block themselves."
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "blocked_user_id": blocked_user_id,
            "status": "blocked",
        }

    def unblock_user(
        self,
        user_id: str,
        blocked_user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "blocked_user_id": blocked_user_id,
            "status": "unblocked",
        }

    def get_blocked_users(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "blocked_users": [],
        }

    def is_blocked(
        self,
        user_id: str,
        other_user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "other_user_id": other_user_id,
            "is_blocked": False,
        }
