"""
MAIN BASE FOUNDATION
WORDPRESS SERVICE

Central service layer for connected WordPress websites.

Responsibilities:
- register WordPress sites
- retrieve WordPress sites
- connect to WordPress databases
- check WordPress database health
- verify WordPress tables
- disconnect database connections
- provide central platform status

IMPORTANT:
- Live WordPress data remains on the hosting/provider.
- Database credentials are never stored in this service.
- Credentials come from secure environment variables.
- This service coordinates Connection + Registry.
"""

from __future__ import annotations

from typing import Optional

from .connection import (
    WordPressConnectionConfig,
    WordPressDatabaseConnection,
)

from .registry import (
    WordPressRegistry,
    WordPressSite,
)


class WordPressService:
    """Central service for WordPress platform management."""

    def __init__(
        self,
        registry: Optional[
            WordPressRegistry
        ] = None,
    ) -> None:

        self.registry = (
            registry
            or WordPressRegistry()
        )

        self._connections: dict[
            str,
            WordPressDatabaseConnection
        ] = {}

    # ==============================================================
    # REGISTER SITE
    # ==============================================================

    def register_site(
        self,
        site: WordPressSite,
    ) -> WordPressSite:
        """Register a WordPress site."""

        return self.registry.register(
            site
        )

    # ==============================================================
    # GET SITE
    # ==============================================================

    def get_site(
        self,
        site_id: str,
    ) -> Optional[WordPressSite]:
        """Return a registered WordPress site."""

        return self.registry.get(
            site_id
        )

    # ==============================================================
    # LIST SITES
    # ==============================================================

    def list_sites(
        self,
    ) -> list[WordPressSite]:
        """Return all registered WordPress sites."""

        return self.registry.list_sites()

    # ==============================================================
    # CONNECT DATABASE
    # ==============================================================

    def connect_site(
        self,
        site_id: str,
        environment_prefix: str,
    ) -> dict:
        """
        Connect one registered WordPress site
        to its live database.

        The database credentials are loaded from
        secure environment variables.
        """

        site = self.registry.get(
            site_id
        )

        if site is None:
            return {
                "success": False,
                "status": "SITE_NOT_FOUND",
                "site_id": site_id,
            }

        try:

            config = (
                WordPressConnectionConfig
                .from_environment(
                    site_id=site.site_id,
                    domain=site.domain,
                    prefix=environment_prefix,
                )
            )

            connection = (
                WordPressDatabaseConnection(
                    config
                )
            )

            health = connection.health()

            if not health["success"]:

                return {
                    "success": False,
                    "status": (
                        "DATABASE_CONNECTION_FAILED"
                    ),
                    "site_id": site_id,
                    "domain": site.domain,
                    "health": health,
                }

            self._connections[
                site_id
            ] = connection

            self.registry.set_status(
                site_id,
                "CONNECTED",
            )

            return {
                "success": True,
                "status": "CONNECTED",

                "site_id": site_id,

                "domain": site.domain,

                "database": (
                    config.database_name
                ),

                "health": health,
            }

        except Exception as exc:

            self.registry.set_status(
                site_id,
                "CONNECTION_FAILED",
            )

            return {
                "success": False,
                "status": (
                    "CONNECTION_ERROR"
                ),

                "site_id": site_id,

                "domain": site.domain,

                "error": str(exc),
            }

    # ==============================================================
    # DISCONNECT DATABASE
    # ==============================================================

    def disconnect_site(
        self,
        site_id: str,
    ) -> dict:
        """Disconnect a WordPress site's database."""

        connection = self._connections.get(
            site_id
        )

        if connection is None:

            return {
                "success": True,
                "status": (
                    "ALREADY_DISCONNECTED"
                ),
                "site_id": site_id,
            }

        connection.disconnect()

        del self._connections[
            site_id
        ]

        site = self.registry.get(
            site_id
        )

        if site is not None:
            self.registry.set_status(
                site_id,
                "REGISTERED",
            )

        return {
            "success": True,
            "status": "DISCONNECTED",
            "site_id": site_id,
        }

    # ==============================================================
    # HEALTH
    # ==============================================================

    def health(
        self,
        site_id: str,
    ) -> dict:
        """Return live database health."""

        connection = self._connections.get(
            site_id
        )

        if connection is None:

            return {
                "success": False,
                "status": "NOT_CONNECTED",
                "site_id": site_id,
            }

        return connection.health()

    # ==============================================================
    # WORDPRESS TABLE CHECK
    # ==============================================================

    def check_wordpress(
        self,
        site_id: str,
    ) -> dict:
        """Verify essential WordPress tables."""

        connection = self._connections.get(
            site_id
        )

        if connection is None:

            return {
                "success": False,
                "status": "NOT_CONNECTED",
                "site_id": site_id,
            }

        return (
            connection
            .check_wordpress_tables()
        )

    # ==============================================================
    # CONNECTION STATUS
    # ==============================================================

    def connection_status(
        self,
        site_id: str,
    ) -> dict:
        """Return safe connection status."""

        connection = self._connections.get(
            site_id
        )

        site = self.registry.get(
            site_id
        )

        if site is None:

            return {
                "success": False,
                "status": "SITE_NOT_FOUND",
                "site_id": site_id,
            }

        return {
            "success": True,

            "site_id": site.site_id,

            "domain": site.domain,

            "site_status": site.status,

            "database_connected": (
                connection is not None
                and connection.connection
                is not None
            ),
        }

    # ==============================================================
    # ALL CONNECTIONS
    # ==============================================================

    def connection_status_all(
        self,
    ) -> list[dict]:
        """Return connection status for every site."""

        return [
            self.connection_status(
                site.site_id
            )
            for site
            in self.registry.list_sites()
        ]

    # ==============================================================
    # PLATFORM SUMMARY
    # ==============================================================

    def summary(self) -> dict:
        """Return WordPress platform summary."""

        sites = self.registry.list_sites()

        connected = sum(
            1
            for site in sites
            if site.status == "CONNECTED"
        )

        failed = sum(
            1
            for site in sites
            if site.status
            == "CONNECTION_FAILED"
        )

        return {
            "service": "WordPressService",

            "total_sites": len(sites),

            "connected_sites": connected,

            "failed_sites": failed,

            "registered_sites": [
                site.to_dict()
                for site in sites
            ],
        }


__all__ = [
    "WordPressService",
]
