"""LINKSETU permission experience service."""


class LinkSetuPermissionService:
    """Manage platform-specific permissions in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_permissions = (
        "view",
        "create",
        "edit",
        "delete",
        "publish",
        "manage_members",
        "manage_roles",
        "moderate",
    )

    def grant_permission(
        self,
        assigned_by: str,
        user_id: str,
        entity_id: str,
        permission: str,
    ) -> dict:

        if permission not in self.allowed_permissions:
            raise ValueError(
                f"Unsupported permission: {permission}"
            )

        return {
            "platform": self.platform_name,
            "assigned_by": assigned_by,
            "user_id": user_id,
            "entity_id": entity_id,
            "permission": permission,
            "status": "granted",
        }

    def revoke_permission(
        self,
        revoked_by: str,
        user_id: str,
        entity_id: str,
        permission: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "revoked_by": revoked_by,
            "user_id": user_id,
            "entity_id": entity_id,
            "permission": permission,
            "status": "revoked",
        }

    def get_user_permissions(
        self,
        user_id: str,
        entity_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "entity_id": entity_id,
            "permissions": [],
        }

    def check_permission(
        self,
        user_id: str,
        entity_id: str,
        permission: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "entity_id": entity_id,
            "permission": permission,
            "allowed": False,
        }
