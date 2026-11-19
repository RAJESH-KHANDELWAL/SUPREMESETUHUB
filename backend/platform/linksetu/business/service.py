"""LINKSETU business experience service."""


class LinkSetuBusinessService:
    """Manage business presence in LINKSETU."""

    platform_name = "LINKSETU"

    def create_business(
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
            "entity_type": "business",
            "status": "created",
        }

    def get_business(
        self,
        business_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "business_id": business_id,
            "entity_type": "business",
        }

    def update_business(
        self,
        business_id: str,
        data: dict,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "business_id": business_id,
            "entity_type": "business",
            "data": data,
            "status": "updated",
        }

    def get_businesses(
        self,
        owner_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "businesses": [],
        }
