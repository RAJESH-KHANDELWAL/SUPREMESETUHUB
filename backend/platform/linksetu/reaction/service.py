"""LINKSETU reaction experience service."""


class LinkSetuReactionService:
    """Manage reactions on LINKSETU content."""

    platform_name = "LINKSETU"

    allowed_reactions = (
        "like",
        "love",
        "support",
        "celebrate",
        "laugh",
        "sad",
        "angry",
    )

    def add_reaction(
        self,
        user_id: str,
        post_id: str,
        reaction: str = "like",
    ) -> dict:

        if reaction not in self.allowed_reactions:
            raise ValueError(
                f"Unsupported reaction: {reaction}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "post_id": post_id,
            "reaction": reaction,
            "status": "added",
        }

    def remove_reaction(
        self,
        user_id: str,
        post_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "post_id": post_id,
            "status": "removed",
        }

    def get_reactions(self, post_id: str) -> dict:

        return {
            "platform": self.platform_name,
            "post_id": post_id,
            "reactions": {},
        }
