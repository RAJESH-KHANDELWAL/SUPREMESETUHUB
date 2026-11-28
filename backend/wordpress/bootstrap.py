"""
WordPress service bootstrap.

The registry is persistent, but live MySQL sockets are process-local. On every
startup, stale CONNECTED metadata must be reset until a new connection and
WordPress core-table verification succeeds.
"""
from __future__ import annotations

from backend.wordpress.registry import WordPressRegistry
from backend.wordpress.service import WordPressService
from backend.wordpress.sites import WORDPRESS_SITES


def create_wordpress_service() -> WordPressService:
    registry = WordPressRegistry()
    service = WordPressService(registry=registry)

    for configured_site in WORDPRESS_SITES:
        existing = registry.get(configured_site.site_id)
        if existing is None:
            registry.register(configured_site)
            continue

        changed = False
        # Refresh only non-secret metadata from the allow-listed configuration.
        for field in ("domain", "site_url", "provider", "database_name", "table_prefix", "environment", "description"):
            configured_value = getattr(configured_site, field)
            if configured_value and getattr(existing, field) != configured_value:
                setattr(existing, field, configured_value)
                changed = True

        # A previous process's MySQL connection cannot survive a restart.
        if existing.status == "CONNECTED":
            existing.status = "REGISTERED"
            changed = True

        if changed:
            registry.update(existing)

    return service


__all__ = ["create_wordpress_service"]
