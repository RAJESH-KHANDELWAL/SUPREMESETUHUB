"""LINKSETU save experience service."""


class LinkSetuSaveService:
    """Manage saved LINKSETU content."""

    platform_name = "LINKSETU"

    def save_post(
        self,
        user_id: str,
        post_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "post_id": post_id,
            "status": "saved",
        }

    def unsave_post(
        self,
        user_id: str,
        post_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "post_id": post_id,
            "status": "unsaved",
        }

    def get_saved_posts(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "saved_posts": [],
        }

    def is_saved(
        self,
        user_id: str,
        post_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "post_id": post_id,
            "is_saved": False,
        }
