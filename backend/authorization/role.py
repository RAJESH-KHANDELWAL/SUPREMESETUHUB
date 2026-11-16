"""
MAIN BASE FOUNDATION
AUTHORIZATION ROLE SYSTEM

Defines platform roles and their permission sets.

IMPORTANT:
- Role definitions belong to authorization.
- Permission definitions remain in permission.py.
- No API logic.
- No database logic.
- No WordPress logic.
- No engine logic.
"""

from __future__ import annotations

from enum import Enum

from .permission import Permission, PermissionSet


class Role(str, Enum):
    """Platform authorization roles."""

    SUPREME_ADMIN_OWNER = "supreme_admin_owner"

    COMPANY_OWNER = "company_owner"

    ADMIN = "admin"

    DEVELOPER = "developer"

    STAFF = "staff"

    CUSTOMER = "customer"


class RolePermissionRegistry:
    """
    Maps each role to its default permissions.

    These are role definitions only.
    User assignment is handled separately.
    """

    @staticmethod
    def permissions_for(
        role: Role,
    ) -> PermissionSet:
        """Return the default permissions for a role."""

        if role == Role.SUPREME_ADMIN_OWNER:
            return PermissionSet.from_permissions(
                Permission
            )

        if role == Role.COMPANY_OWNER:
            return PermissionSet.from_permissions(
                [
                    Permission.COMPANY_VIEW,
                    Permission.COMPANY_EDIT,
                    Permission.COMPANY_UPDATE,

                    Permission.USER_VIEW,
                    Permission.USER_CREATE,
                    Permission.USER_EDIT,
                    Permission.USER_UPDATE,

                    Permission.WEBSITE_VIEW,
                    Permission.WORDPRESS_VIEW,
                    Permission.WORDPRESS_CREATE,
                    Permission.WORDPRESS_EDIT,
                    Permission.WORDPRESS_UPDATE,

                    Permission.DOMAIN_VIEW,
                    Permission.DOMAIN_CREATE,
                    Permission.DOMAIN_EDIT,
                    Permission.DOMAIN_UPDATE,

                    Permission.HOSTING_VIEW,
                    Permission.HOSTING_CREATE,
                    Permission.HOSTING_EDIT,
                    Permission.HOSTING_UPDATE,
                ]
            )

        if role == Role.ADMIN:
            return PermissionSet.from_permissions(
                [
                    Permission.COMPANY_VIEW,

                    Permission.USER_VIEW,
                    Permission.USER_CREATE,
                    Permission.USER_EDIT,
                    Permission.USER_UPDATE,

                    Permission.WEBSITE_VIEW,

                    Permission.WORDPRESS_VIEW,
                    Permission.WORDPRESS_EDIT,
                    Permission.WORDPRESS_UPDATE,

                    Permission.DOMAIN_VIEW,

                    Permission.HOSTING_VIEW,
                ]
            )

        if role == Role.DEVELOPER:
            return PermissionSet.from_permissions(
                [
                    Permission.WEBSITE_VIEW,

                    Permission.WORDPRESS_VIEW,
                    Permission.WORDPRESS_EDIT,
                    Permission.WORDPRESS_UPDATE,

                    Permission.DATABASE_VIEW,

                    Permission.SERVER_VIEW,

                    Permission.SYSTEM_VIEW,
                ]
            )

        if role == Role.STAFF:
            return PermissionSet.from_permissions(
                [
                    Permission.COMPANY_VIEW,
                    Permission.USER_VIEW,
                    Permission.WEBSITE_VIEW,
                    Permission.WORDPRESS_VIEW,
                    Permission.DOMAIN_VIEW,
                    Permission.HOSTING_VIEW,
                ]
            )

        if role == Role.CUSTOMER:
            return PermissionSet.from_permissions(
                [
                    Permission.COMPANY_VIEW,
                    Permission.WEBSITE_VIEW,
                    Permission.WORDPRESS_VIEW,
                    Permission.DOMAIN_VIEW,
                    Permission.HOSTING_VIEW,
                ]
            )

        return PermissionSet.from_permissions([])


__all__ = [
    "Role",
    "RolePermissionRegistry",
]
