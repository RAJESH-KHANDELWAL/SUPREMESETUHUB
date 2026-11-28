"""Global Platforms directory package and compatibility service exports."""
from .routes import router
from .service import (
    get_platform_directory_status,
    get_platform_profile,
    list_platform_domains,
    list_platforms,
)

__all__ = [
    "router",
    "list_platforms",
    "get_platform_profile",
    "get_platform_directory_status",
    "list_platform_domains",
]
