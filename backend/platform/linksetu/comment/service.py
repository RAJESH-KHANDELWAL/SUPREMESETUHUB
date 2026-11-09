"""LINKSETU comment experience service."""


class LinkSetuCommentService:
    """Manage comments on LINKSETU posts."""

    platform_name = "LINKSETU"

    def create_comment(
        self,
        user_id: str,
        post_id: str,
        content: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "post_id": post_id,
            "content": content,
            "status": "created",
        }

    def get_comments(self, post_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "post_id": post_id,
            "comments": [],
        }

    def delete_comment(self, comment_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "comment_id": comment_id,
            "status": "deleted",
        }
