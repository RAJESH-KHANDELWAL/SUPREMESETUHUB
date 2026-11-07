"""LINKSETU search experience service."""


class LinkSetuSearchService:
    """Manage search experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_types = (
        "all",
        "people",
        "posts",
        "media",
        "pages",
        "groups",
    )

    def search(
        self,
        user_id: str,
        query: str,
        search_type: str = "all",
        limit: int = 20,
    ) -> dict:

        if search_type not in self.allowed_types:
            raise ValueError(
                f"Unsupported search type: {search_type}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "query": query,
            "search_type": search_type,
            "limit": limit,
            "results": [],
        }

    def search_people(
        self,
        user_id: str,
        query: str,
    ) -> dict:

        return self.search(
            user_id=user_id,
            query=query,
            search_type="people",
        )

    def search_posts(
        self,
        user_id: str,
        query: str,
    ) -> dict:

        return self.search(
            user_id=user_id,
            query=query,
            search_type="posts",
        )

    def search_media(
        self,
        user_id: str,
        query: str,
    ) -> dict:

        return self.search(
            user_id=user_id,
            query=query,
            search_type="media",
        )
