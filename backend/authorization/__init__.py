"""MAIN BASE FOUNDATION authorization system."""

from .manager import AuthorizationManager
from .models import AuthorizationRequest
from .role import Role, RolePermissionRegistry

__all__ = [
    "AuthorizationManager",
    "AuthorizationRequest",
    "Role",
    "RolePermissionRegistry",
]
