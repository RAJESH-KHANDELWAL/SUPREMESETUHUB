"""
MAIN BASE FOUNDATION
WORDPRESS BOOTSTRAP

Loads registered WordPress sites into the central registry.

IMPORTANT:
- This does NOT connect to the live database automatically.
- It only registers the configured WordPress sites.
- Database connection happens explicitly through WordPressService.
"""

from __future__ import annotations

from backend.wordpress.registry import (
    WordPressRegistry,
)

from backend.wordpress.service import (
    WordPressService,
)

from backend.wordpress.sites import (
    WORDPRESS_SITES,
)


def create_wordpress_service() -> WordPressService:
    """
    Create the central WordPress service and
    load all configured WordPress sites.
    """

    registry = WordPressRegistry()

    service = WordPressService(
        registry=registry
    )

    for site in WORDPRESS_SITES:

        existing = registry.get(
            site.site_id
        )

        if existing is None:

            registry.register(
                site
            )

    return service


__all__ = [
    "create_wordpress_service",
]
