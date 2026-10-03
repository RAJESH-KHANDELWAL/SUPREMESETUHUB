"""
CORE Leadership Registry

Central registry for leadership and management roles.
"""

from typing import Dict, Optional

from .base import LeadershipRole


class LeadershipRegistry:
    """
    Central registry of CORE leadership roles.
    """

    def __init__(self) -> None:
        self._roles: Dict[str, LeadershipRole] = {}

    def register(self, role: LeadershipRole) -> LeadershipRole:
        """Register or replace a leadership role."""
        key = role.role_name.strip().lower()

        if not key:
            raise ValueError("role_name cannot be empty")

        self._roles[key] = role
        return role

    def get(self, role_name: str) -> Optional[LeadershipRole]:
        """Return a registered role, or None if it does not exist."""
        return self._roles.get(role_name.strip().lower())

    def has(self, role_name: str) -> bool:
        """Check whether a role is registered."""
        return role_name.strip().lower() in self._roles

    def remove(self, role_name: str) -> Optional[LeadershipRole]:
        """Remove and return a role if it exists."""
        return self._roles.pop(role_name.strip().lower(), None)

    def list_roles(self) -> list[LeadershipRole]:
        """Return all registered leadership roles."""
        return list(self._roles.values())

    def clear(self) -> None:
        """Clear the registry."""
        self._roles.clear()

    def count(self) -> int:
        """Return the number of registered roles."""
        return len(self._roles)
