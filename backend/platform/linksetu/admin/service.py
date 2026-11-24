"""LINKSETU admin experience service."""


class LinkSetuAdminService:
    """Manage LINKSETU platform administration."""

    platform_name = "LINKSETU"

    def get_entity_admin(
        self,
        admin_id: str,
        entity_id: str,
        entity_type: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "admin_id": admin_id,
            "entity_id": entity_id,
            "entity_type": entity_type,
            "status": "active",
        }

    def assign_role(
        self,
        admin_id: str,
        user_id: str,
        role: str,
        entity_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "admin_id": admin_id,
            "user_id": user_id,
            "role": role,
            "entity_id": entity_id,
            "status": "assigned",
        }

    def remove_role(
        self,
        admin_id: str,
        user_id: str,
        role: str,
        entity_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "admin_id": admin_id,
            "user_id": user_id,
            "role": role,
            "entity_id": entity_id,
            "status": "removed",
        }

    def get_members(
        self,
        entity_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "entity_id": entity_id,
            "members": [],
        }

    def get_roles(
        self,
        entity_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "entity_id": entity_id,
            "roles": [],
        }
