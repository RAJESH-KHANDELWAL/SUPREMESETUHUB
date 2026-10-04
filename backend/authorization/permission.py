"""
MAIN BASE FOUNDATION
AUTHORIZATION PERMISSION FOUNDATION

Defines permissions used by the platform.

IMPORTANT:
- This module defines WHAT a user is allowed to do.
- It does not authenticate users.
- It does not manage passwords.
- It does not manage API routes.
- It does not contain WordPress logic.
- It does not contain database logic.
- It does not contain engine logic.

Actual permission assignment and enforcement belong
to the authorization layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class Permission(str, Enum):
    """Platform permissions."""

    # --------------------------------------------------------------
    # GENERAL
    # --------------------------------------------------------------

    VIEW = "view"

    CREATE = "create"

    EDIT = "edit"

    UPDATE = "update"

    DELETE = "delete"

    MANAGE = "manage"

    # --------------------------------------------------------------
    # DATABASE
    # --------------------------------------------------------------

    DATABASE_VIEW = "database.view"

    DATABASE_CREATE = "database.create"

    DATABASE_EDIT = "database.edit"

    DATABASE_UPDATE = "database.update"

    DATABASE_DELETE = "database.delete"

    DATABASE_MANAGE = "database.manage"

    # --------------------------------------------------------------
    # WORDPRESS
    # --------------------------------------------------------------

    WORDPRESS_VIEW = "wordpress.view"

    WORDPRESS_CREATE = "wordpress.create"

    WORDPRESS_EDIT = "wordpress.edit"

    WORDPRESS_UPDATE = "wordpress.update"

    WORDPRESS_DELETE = "wordpress.delete"

    WORDPRESS_MANAGE = "wordpress.manage"

    # --------------------------------------------------------------
    # THEMES
    # --------------------------------------------------------------

    THEME_VIEW = "theme.view"

    THEME_INSTALL = "theme.install"

    THEME_ACTIVATE = "theme.activate"

    THEME_UPDATE = "theme.update"

    THEME_DELETE = "theme.delete"

    # --------------------------------------------------------------
    # PLUGINS
    # --------------------------------------------------------------

    PLUGIN_VIEW = "plugin.view"

    PLUGIN_INSTALL = "plugin.install"

    PLUGIN_ACTIVATE = "plugin.activate"

    PLUGIN_UPDATE = "plugin.update"

    PLUGIN_DELETE = "plugin.delete"

    # --------------------------------------------------------------
    # DOMAIN
    # --------------------------------------------------------------

    DOMAIN_VIEW = "domain.view"

    DOMAIN_CREATE = "domain.create"

    DOMAIN_EDIT = "domain.edit"

    DOMAIN_UPDATE = "domain.update"

    DOMAIN_DELETE = "domain.delete"

    DOMAIN_MANAGE = "domain.manage"

    # --------------------------------------------------------------
    # HOSTING
    # --------------------------------------------------------------

    HOSTING_VIEW = "hosting.view"

    HOSTING_CREATE = "hosting.create"

    HOSTING_EDIT = "hosting.edit"

    HOSTING_UPDATE = "hosting.update"

    HOSTING_DELETE = "hosting.delete"

    HOSTING_MANAGE = "hosting.manage"

    # --------------------------------------------------------------
    # SERVER
    # --------------------------------------------------------------

    SERVER_VIEW = "server.view"

    SERVER_CREATE = "server.create"

    SERVER_EDIT = "server.edit"

    SERVER_UPDATE = "server.update"

    SERVER_DELETE = "server.delete"

    SERVER_MANAGE = "server.manage"

    # --------------------------------------------------------------
    # COMPANY / ORGANIZATION
    # --------------------------------------------------------------

    COMPANY_VIEW = "company.view"

    COMPANY_CREATE = "company.create"

    COMPANY_EDIT = "company.edit"

    COMPANY_UPDATE = "company.update"

    COMPANY_DELETE = "company.delete"

    COMPANY_MANAGE = "company.manage"

    # --------------------------------------------------------------
    # USERS
    # --------------------------------------------------------------

    USER_VIEW = "user.view"

    USER_CREATE = "user.create"

    USER_EDIT = "user.edit"

    USER_UPDATE = "user.update"

    USER_DELETE = "user.delete"

    USER_MANAGE = "user.manage"

    # --------------------------------------------------------------
    # SYSTEM
    # --------------------------------------------------------------

    SYSTEM_VIEW = "system.view"

    SYSTEM_MANAGE = "system.manage"

    SYSTEM_CONFIGURATION = "system.configuration"


@dataclass(frozen=True)
class PermissionSet:
    """Immutable collection of permissions."""

    permissions: frozenset[Permission]

    @classmethod
    def from_permissions(
        cls,
        permissions: Iterable[
            Permission | str
        ],
    ) -> "PermissionSet":
        """Create a permission set."""

        normalized: set[Permission] = set()

        for permission in permissions:

            if isinstance(
                permission,
                Permission,
            ):
                normalized.add(
                    permission
                )
                continue

            normalized.add(
                Permission(permission)
            )

        return cls(
            permissions=frozenset(
                normalized
            )
        )

    def has(
        self,
        permission: Permission | str,
    ) -> bool:
        """Check whether a permission exists."""

        if not isinstance(
            permission,
            Permission,
        ):
            permission = Permission(
                permission
            )

        return permission in self.permissions

    def has_any(
        self,
        permissions: Iterable[
            Permission | str
        ],
    ) -> bool:
        """Check whether at least one permission exists."""

        return any(
            self.has(permission)
            for permission in permissions
        )

    def has_all(
        self,
        permissions: Iterable[
            Permission | str
        ],
    ) -> bool:
        """Check whether all permissions exist."""

        return all(
            self.has(permission)
            for permission in permissions
        )

    def to_list(self) -> list[str]:
        """Return permissions as strings."""

        return sorted(
            permission.value
            for permission in self.permissions
        )


__all__ = [
    "Permission",
    "PermissionSet",
]
