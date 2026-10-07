"""LINKSETU profile experience service."""


class LinkSetuProfileService:
    """Resolve a MAIN PROFILE into the LINKSETU experience."""

    platform_name = "LINKSETU"

    def get_profile(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "profile_source": "MAIN_BASE_PROFILE",
            "status": "linked",
        }

    def get_profile_experience(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "profile_source": "MAIN_BASE_PROFILE",
            "experience": {
                "profile": True,
                "connections": True,
                "posts": True,
                "media": True,
            },
        }
