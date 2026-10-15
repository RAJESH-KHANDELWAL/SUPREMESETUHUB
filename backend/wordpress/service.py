"""
Service layer for the registered, existing WordPress installations.

The central SUPREME database stores registry metadata only. Live WordPress
content remains in each site's own database; this service performs connection
and read-only health/schema checks and never synchronizes or migrates content.
"""
from __future__ import annotations

from typing import Optional

from .connection import WordPressConnectionConfig, WordPressDatabaseConnection
from .registry import WordPressRegistry, WordPressSite


class WordPressService:
    """Coordinate registered WordPress sites and their live DB connections."""

    def __init__(self, registry: Optional[WordPressRegistry] = None) -> None:
        self.registry = registry or WordPressRegistry()
        self._connections: dict[str, WordPressDatabaseConnection] = {}

    def register_site(self, site: WordPressSite) -> WordPressSite:
        return self.registry.register(site)

    def get_site(self, site_id: str) -> Optional[WordPressSite]:
        return self.registry.get(site_id)

    def list_sites(self) -> list[WordPressSite]:
        return self.registry.list_sites()

    def connect_site(self, site_id: str, environment_prefix: str) -> dict:
        """Connect and verify a registered site using private env credentials."""
        site = self.registry.get(site_id)
        if site is None:
            return {"success": False, "status": "SITE_NOT_FOUND", "site_id": site_id}

        # Reuse an already-healthy connection instead of leaking/replacing it.
        current = self._connections.get(site_id)
        if current is not None:
            current_health = current.health()
            if current_health.get("success"):
                return {
                    "success": True,
                    "status": "ALREADY_CONNECTED",
                    "site_id": site_id,
                    "domain": site.domain,
                    "health": current_health,
                }
            current.disconnect()
            self._connections.pop(site_id, None)

        candidate: Optional[WordPressDatabaseConnection] = None
        try:
            config = WordPressConnectionConfig.from_environment(
                site_id=site.site_id,
                domain=site.domain,
                prefix=environment_prefix,
            )
            candidate = WordPressDatabaseConnection(config)
            health = candidate.health()
            if not health.get("success"):
                candidate.disconnect()
                self.registry.set_status(site_id, "CONNECTION_FAILED")
                return {
                    "success": False,
                    "status": "DATABASE_CONNECTION_FAILED",
                    "site_id": site_id,
                    "domain": site.domain,
                    "health": health,
                }

            self._connections[site_id] = candidate
            self.registry.set_status(site_id, "CONNECTED")
            return {
                "success": True,
                "status": "CONNECTED",
                "site_id": site_id,
                "domain": site.domain,
                "database": config.database_name,
                "health": health,
            }
        except Exception as exc:
            if candidate is not None:
                candidate.disconnect()
            self._connections.pop(site_id, None)
            self.registry.set_status(site_id, "CONNECTION_FAILED")
            # Exception messages can contain connection details; expose only the type.
            return {
                "success": False,
                "status": "CONNECTION_ERROR",
                "site_id": site_id,
                "domain": site.domain,
                "error_type": type(exc).__name__,
            }

    def disconnect_site(self, site_id: str) -> dict:
        connection = self._connections.pop(site_id, None)
        if connection is None:
            return {"success": True, "status": "ALREADY_DISCONNECTED", "site_id": site_id}

        try:
            connection.disconnect()
        finally:
            if self.registry.get(site_id) is not None:
                self.registry.set_status(site_id, "REGISTERED")
        return {"success": True, "status": "DISCONNECTED", "site_id": site_id}

    def health(self, site_id: str) -> dict:
        connection = self._connections.get(site_id)
        if connection is None:
            return {"success": False, "status": "NOT_CONNECTED", "site_id": site_id}
        result = connection.health()
        if not result.get("success"):
            self.registry.set_status(site_id, "CONNECTION_FAILED")
        return result

    def check_wordpress(self, site_id: str) -> dict:
        connection = self._connections.get(site_id)
        if connection is None:
            return {"success": False, "status": "NOT_CONNECTED", "site_id": site_id}
        return connection.check_wordpress_tables()

    def connection_status(self, site_id: str) -> dict:
        site = self.registry.get(site_id)
        if site is None:
            return {"success": False, "status": "SITE_NOT_FOUND", "site_id": site_id}

        connection = self._connections.get(site_id)
        live_connected = bool(connection and connection.status().get("connected"))
        return {
            "success": True,
            "site_id": site.site_id,
            "domain": site.domain,
            "site_status": site.status,
            "database_connected": live_connected,
        }

    def connection_status_all(self) -> list[dict]:
        return [self.connection_status(site.site_id) for site in self.registry.list_sites()]

    def summary(self) -> dict:
        sites = self.registry.list_sites()
        statuses = [self.connection_status(site.site_id) for site in sites]
        connected = sum(1 for status in statuses if status.get("database_connected"))
        failed = sum(1 for site in sites if site.status == "CONNECTION_FAILED")
        return {
            "service": "WordPressService",
            "total_sites": len(sites),
            "connected_sites": connected,
            "failed_sites": failed,
            "registered_sites": [site.to_dict() for site in sites],
        }


__all__ = ["WordPressService"]
