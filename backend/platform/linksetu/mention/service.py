"""LINKSETU mention experience service."""


class LinkSetuMentionService:
    """Manage user mentions in LINKSETU content."""

    platform_name = "LINKSETU"

    def create_mentions(
        self,
        content: str,
    ) -> dict:

        mentions = [
            word.lstrip("@")
            for word in content.split()
            if word.startswith("@")
        ]

        return {
            "platform": self.platform_name,
            "mentions": mentions,
        }

    def get_mentions(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "mentions": [],
        }

    def mention_user(
        self,
        actor_id: str,
        mentioned_user_id: str,
        content_id: str,
    ) -> dict:

        if actor_id == mentioned_user_id:
            raise ValueError(
                "A person cannot mention themselves."
            )

        return {
            "platform": self.platform_name,
            "actor_id": actor_id,
            "mentioned_user_id": mentioned_user_id,
            "content_id": content_id,
            "status": "created",
        }
