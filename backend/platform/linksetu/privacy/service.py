"""LINKSETU privacy experience service."""


class LinkSetuPrivacyService:
    """Manage platform-specific privacy preferences."""

    platform_name = "LINKSETU"

    allowed_profile_visibility = (
        "public",
        "connections",
        "private",
    )

    def get_privacy_settings(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "settings": {
                "profile_visibility": "public",
                "message_permission": "connections",
                "follow_permission": "public",
                "activity_visibility": True,
            },
        }

    def update_profile_visibility(
        self,
        user_id: str,
        visibility: str,
    ) -> dict:

        if visibility not in self.allowed_profile_visibility:
            raise ValueError(
                f"Unsupported profile visibility: {visibility}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "profile_visibility": visibility,
            "status": "updated",
        }

    def update_activity_visibility(
        self,
        user_id: str,
        visible: bool,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "activity_visibility": visible,
            "status": "updated",
        }
