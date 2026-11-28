"""LINKSETU farm experience service."""


class LinkSetuFarmService:
    """Manage farm and agriculture presence in LINKSETU."""

    platform_name = "LINKSETU"

    def create_farm(
        self,
        owner_id: str,
        name: str,
        description: str = "",
        farm_type: str = "",
        location: str = "",
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "farm_type": farm_type,
            "location": location,
            "entity_type": "farm",
            "status": "created",
        }

    def get_farm(
        self,
        farm_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "farm_id": farm_id,
            "entity_type": "farm",
        }

    def update_farm(
        self,
        farm_id: str,
        data: dict,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "farm_id": farm_id,
            "entity_type": "farm",
            "data": data,
            "status": "updated",
        }

    def get_farms(
        self,
        owner_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "farms": [],
        }
