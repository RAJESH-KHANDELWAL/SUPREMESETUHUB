"""LINKSETU post experience service."""


class LinkSetuPostService:
    """Create and manage LINKSETU posts."""

    platform_name = "LINKSETU"

    def create_post(
        self,
        user_id: str,
        content: str,
        media: list | None = None,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "content": content,
            "media": media or [],
            "status": "created",
        }

    def get_post(self, post_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "post_id": post_id,
        }

    def delete_post(self, post_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "post_id": post_id,
            "status": "deleted",
        }
