"""LINKSETU feed experience service."""


class LinkSetuFeedService:
    """LINKSETU-specific feed experience."""

    platform_name = "LINKSETU"

    def get_feed(self, user_id: str, limit: int = 20) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "source": "LINKSETU",
            "limit": limit,
            "items": [],
        }

    def get_personalized_feed(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "feed_type": "personalized",
            "items": [],
        }
