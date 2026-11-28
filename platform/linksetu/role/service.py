"""LINKSETU role experience service."""


class LinkSetuRoleService:
    """Manage platform-specific roles in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_roles = (
        "owner",
        "admin",
        "manager",
        "moderator",
        "editor",
        "member",
    )

    def assign_role(
        self,
        assigned_by: str,
        user_id: str,
        entity_id: str,
        role: str,
    ) -> dict:

        if role not in self.allowed_roles:
            raise ValueError(
                f"Unsupported role: {role}"
            )

        return {
            "platform": self.platform_name,
            "assigned_by": assigned_by,
            "user_id": user_id,
            "entity_id": entity_id,
            "role": role,
            "status": "assigned",
        }

    def remove_role(
        self,
        removed_by: str,
        user_id: str,
        entity_id: str,
        role: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "removed_by": removed_by,
            "user_id": user_id,
            "entity_id": entity_id,
            "role": role,
            "status": "removed",
        }

    def get_user_roles(
        self,
        user_id: str,
        entity_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "entity_id": entity_id,
            "roles": [],
        }

    def get_entity_roles(
        self,
        entity_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "entity_id": entity_id,
            "roles": [],
        }
