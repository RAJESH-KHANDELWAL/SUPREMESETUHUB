"""Central SUPREMESETUHUB database control plane.

This module uses the canonical SUPREME_DB_* connection and never provisions a
database or changes WordPress databases. Provisioning remains a Hostinger hPanel
operation; this code manages the application's connection and health checks.
"""
from __future__ import annotations

from typing import Any

from backend.database.gde_connection import (
    GDEDatabaseConnection,
    PRIMARY_IDENTITY,
    IDENTITY_GATES,
    SupremeDatabaseConfig,
)


class DatabaseControlPlane:
    """Read-only central database manager with safe status reporting."""

    def __init__(self, config: SupremeDatabaseConfig | None = None) -> None:
        self.config = config or SupremeDatabaseConfig.from_environment()

    def configuration_status(self) -> dict[str, Any]:
        try:
            self.config.validate()
        except ValueError as exc:
            return {
                "system": "DATABASE_MANAGER",
                "status": "CONFIGURATION_INCOMPLETE",
                "valid": False,
                "reason": str(exc),
                "credentials_exposed": False,
            }
        return {
            "system": "DATABASE_MANAGER",
            "status": "CONFIGURED",
            "valid": True,
            "engine": "MYSQL_OR_MARIADB",
            "database": self.config.database,
            "host": self.config.host,
            "port": self.config.port,
            "primary_identity": PRIMARY_IDENTITY,
            "identity_gates": list(IDENTITY_GATES),
            "credentials_exposed": False,
        }

    def health(self) -> dict[str, Any]:
        self.config.validate()
        connection = GDEDatabaseConnection(self.config)
        try:
            result = connection.health()
            return {
                **result,
                "system": "DATABASE_MANAGER",
                "credentials_exposed": False,
                "mutations_performed": False,
            }
        finally:
            connection.close()
