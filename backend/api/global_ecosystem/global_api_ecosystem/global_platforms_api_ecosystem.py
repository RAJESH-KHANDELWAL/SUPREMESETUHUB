"""Backward-compatible import facade for the modular Global Platforms API."""
from pathlib import Path

from fastapi import APIRouter

# The compatibility module shares its name with the canonical package folder.
__path__ = [str(Path(__file__).with_name("global_platforms_api_ecosystem"))]

from .global_platforms_api_ecosystem import router as _modular_router
from .provider_directory import get_provider_directory_status
from .global_platforms_api_ecosystem.service import (
    get_platform_directory_status,
    get_platform_profile,
    list_platform_domains,
    list_platforms,
)

router = APIRouter(tags=["GLOBAL PLATFORMS API COMPATIBILITY"])
router.routes.extend(route for route in _modular_router.routes if hasattr(route, "path"))

ECOSYSTEM_NAME = "GLOBAL PLATFORMS API ECOSYSTEM"


def get_ecosystem_info() -> dict:
    status = get_platform_directory_status()
    return {
        "name": ECOSYSTEM_NAME,
        "status": status["status"],
        "profile_count": status["profile_count"],
        "domain_count": status["domain_count"],
        "provider_count": get_provider_directory_status()["provider_count"],
        "live_external_connections": False,
    }


__all__ = [
    "router",
    "get_ecosystem_info",
    "ECOSYSTEM_NAME",
    "list_platforms",
    "get_platform_profile",
    "get_platform_directory_status",
    "list_platform_domains",
]
