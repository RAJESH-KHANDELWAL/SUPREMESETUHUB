"""LINKSETU discovery experience service."""


class LinkSetuDiscoveryService:
    """Manage discovery and explore experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_sections = (
        "recommended",
        "trending",
        "new",
        "people",
        "posts",
        "media",
    )

    def get_discovery(
        self,
        user_id: str,
        section: str = "recommended",
        limit: int = 20,
    ) -> dict:

        if section not in self.allowed_sections:
            raise ValueError(
                f"Unsupported discovery section: {section}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "section": section,
            "limit": limit,
            "items": [],
        }

    def get_recommended(
        self,
        user_id: str,
    ) -> dict:

        return self.get_discovery(
            user_id=user_id,
            section="recommended",
        )

    def get_trending(
        self,
        user_id: str,
    ) -> dict:

        return self.get_discovery(
            user_id=user_id,
            section="trending",
        )

    def get_new_content(
        self,
        user_id: str,
    ) -> dict:

        return self.get_discovery(
            user_id=user_id,
            section="new",
        )
