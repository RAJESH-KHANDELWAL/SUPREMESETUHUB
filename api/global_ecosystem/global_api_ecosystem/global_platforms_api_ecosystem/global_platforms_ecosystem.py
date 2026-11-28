"""Compatibility facade for the Global Platforms directory ecosystem."""
from .global_platforms_ecosystem import (
    get_platform_directory_status,
    get_platform_profile,
    list_platform_domains,
    list_platforms,
    router,
)

__all__ = [
    "router",
    "list_platforms",
    "get_platform_profile",
    "get_platform_directory_status",
    "list_platform_domains",
]
