"""LINKSETU page experience service."""


class LinkSetuPageService:
    """Manage public pages in LINKSETU."""

    platform_name = "LINKSETU"

    def create_page(
        self,
        owner_id: str,
        name: str,
        description: str = "",
        category: str = "",
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "category": category,
            "entity_type": "page",
            "status": "created",
        }

    def get_page(
        self,
        page_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "page_id": page_id,
            "entity_type": "page",
        }

    def update_page(
        self,
        page_id: str,
        data: dict,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "page_id": page_id,
            "entity_type": "page",
            "data": data,
            "status": "updated",
        }

    def get_pages(
        self,
        owner_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "pages": [],
        }
