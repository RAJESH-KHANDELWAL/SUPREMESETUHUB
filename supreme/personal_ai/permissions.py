from __future__ import annotations

from typing import Any


class SupremePermissions:
    """
    SUPREME PERSONAL AI permission layer.

    OWNER has full control over personal/system write operations.
    Other actors can only receive capabilities explicitly allowed
    by the access policy.
    """

    OWNER_ROLE = "OWNER"

    OWNER_ONLY = {
        "memory.write",
        "memory.delete",
        "github.write",
        "wordpress.write",
        "system.write",
        "automation.write",
    }

    READABLE = {
        "memory.read",
        "github.read",
        "wordpress.read",
        "system.read",
        "research.read",
        "files.read",
    }

    def allowed(
        self,
        actor_role: str,
        capability: str,
    ) -> bool:
        role = actor_role.strip().upper()
        capability_name = capability.strip().lower()

        if capability_name in self.OWNER_ONLY:
            return role == self.OWNER_ROLE

        return (
            capability_name in self.READABLE
            or role == self.OWNER_ROLE
        )

    def check(
        self,
        actor_role: str,
        capability: str,
    ) -> dict[str, Any]:
        allowed = self.allowed(
            actor_role=actor_role,
            capability=capability,
        )

        return {
            "allowed": allowed,
            "actor_role": actor_role.strip().upper(),
            "capability": capability.strip().lower(),
        }

    def require_owner(
        self,
        actor_role: str,
    ) -> None:
        if actor_role.strip().upper() != self.OWNER_ROLE:
            raise PermissionError(
                "SUPREME_OWNER_PERMISSION_REQUIRED"
            )
