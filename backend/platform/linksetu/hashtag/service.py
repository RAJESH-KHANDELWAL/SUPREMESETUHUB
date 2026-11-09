"""LINKSETU hashtag experience service."""


class LinkSetuHashtagService:
    """Manage hashtags in LINKSETU."""

    platform_name = "LINKSETU"

    def create_hashtags(
        self,
        content: str,
    ) -> dict:

        hashtags = [
            word.lstrip("#")
            for word in content.split()
            if word.startswith("#")
        ]

        return {
            "platform": self.platform_name,
            "hashtags": hashtags,
        }

    def get_hashtag(
        self,
        hashtag: str,
    ) -> dict:

        normalized = hashtag.lstrip("#").lower()

        return {
            "platform": self.platform_name,
            "hashtag": normalized,
            "posts": [],
        }

    def get_trending_hashtags(
        self,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "hashtags": [],
        }
