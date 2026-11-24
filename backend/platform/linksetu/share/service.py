"""LINKSETU share experience service."""


class LinkSetuShareService:
    """Manage sharing of LINKSETU content."""

    platform_name = "LINKSETU"

    def share_post(
        self,
        user_id: str,
        post_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "post_id": post_id,
            "status": "shared",
        }

    def share_to_profile(
        self,
        user_id: str,
        post_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "post_id": post_id,
            "share_type": "profile",
            "status": "shared",
        }

    def share_link(
        self,
        post_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "post_id": post_id,
            "share_type": "link",
            "status": "ready",
        }
