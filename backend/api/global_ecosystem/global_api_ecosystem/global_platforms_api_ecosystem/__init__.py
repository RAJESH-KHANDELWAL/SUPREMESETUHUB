"""Global Platforms API ecosystem public package interface."""
from .provider_directory import get_provider_directory_status
from .routes import router
from .service import (
    get_ecosystem_status,
    get_platform,
    get_domain,
    list_domains,
    search_platforms,
)


def get_ecosystem_info() -> dict:
    status = get_ecosystem_status()
    return {
        "name": status["ecosystem"],
        "status": status["status"],
        "profile_count": status["profile_count"],
        "domain_count": status["domain_count"],
        "provider_count": get_provider_directory_status()["provider_count"],
        "live_external_connections": False,
    }


__all__ = [
    "router",
    "get_ecosystem_info",
    "get_ecosystem_status",
    "get_platform",
    "get_domain",
    "list_domains",
    "search_platforms",
    "get_provider_directory_status",
]
