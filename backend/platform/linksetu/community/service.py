"""LINKSETU community experience service."""


class LinkSetuCommunityService:
    """Manage communities in LINKSETU."""

    platform_name = "LINKSETU"

    def create_community(
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
            "entity_type": "community",
            "status": "created",
        }

    def get_community(
        self,
        community_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "community_id": community_id,
            "entity_type": "community",
        }

    def update_community(
        self,
        community_id: str,
        data: dict,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "community_id": community_id,
            "entity_type": "community",
            "data": data,
            "status": "updated",
        }

    def join_community(
        self,
        user_id: str,
        community_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "community_id": community_id,
            "status": "joined",
        }

    def leave_community(
        self,
        user_id: str,
        community_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "community_id": community_id,
            "status": "left",
        }

    def get_communities(
        self,
        owner_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "communities": [],
        }
