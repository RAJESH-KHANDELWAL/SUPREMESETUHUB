"""Read-only health adapters for the existing database implementations.

Database ownership stays in backend.database. This module does not create schemas,
run migrations, seed records, or silently switch the application's database engine.
"""
from __future__ import annotations

from typing import Any

from backend.database.gde_connection import (
    GDEDatabaseConnection,
    SupremeDatabaseConfig,
)


class DatabaseInfrastructureService:
    """Check configured database connectivity without changing database contents."""

    def __init__(self, sqlite_service: Any | None = None) -> None:
        # Inject the application's existing DatabaseService when its status is needed.
        # Do not instantiate it here: DatabaseService.connect() can create a new file.
        self.sqlite_service = sqlite_service

    def check_sqlite_runtime(self) -> dict[str, Any]:
        """Check an already-created SQLite service; never create one implicitly."""
        if self.sqlite_service is None:
            return {
                "success": False,
                "status": "NOT_CHECKED",
                "engine": "SQLITE",
                "reason": "Inject the existing DatabaseService instance to check it.",
                "mutations_performed": False,
            }
        try:
            result = self.sqlite_service.health()
            healthy = bool(result.get("healthy"))
            return {
                "success": healthy,
                "status": "HEALTHY" if healthy else "UNHEALTHY",
                "engine": "SQLITE",
                "details": result,
                "mutations_performed": False,
            }
        except Exception as exc:
            return {
                "success": False,
                "status": "CHECK_FAILED",
                "engine": "SQLITE",
                "error_type": type(exc).__name__,
                "mutations_performed": False,
            }

    def check_central_mysql(self) -> dict[str, Any]:
        """Check the existing central MySQL connector when configuration is present."""
        try:
            config = SupremeDatabaseConfig.from_environment()
            config.validate()
        except (TypeError, ValueError) as exc:
            return {
                "success": False,
                "status": "CONFIGURATION_INCOMPLETE",
                "engine": "MYSQL",
                "reason": str(exc),
                "connection_attempted": False,
                "mutations_performed": False,
            }

        connection = GDEDatabaseConnection(config)
        try:
            result = connection.health()
            return {
                **result,
                "engine": "MYSQL",
                "connection_attempted": True,
                "mutations_performed": False,
            }
        finally:
            connection.close()

    def check_all(self, *, check_mysql: bool = False) -> dict[str, Any]:
        """Return checks for configured engines; MySQL network access is opt-in."""
        checks = {"sqlite_runtime": self.check_sqlite_runtime()}
        if check_mysql:
            checks["central_mysql"] = self.check_central_mysql()
        else:
            checks["central_mysql"] = {
                "success": False,
                "status": "NOT_CHECKED",
                "engine": "MYSQL",
                "reason": "Pass check_mysql=True to perform the read-only connection test.",
                "connection_attempted": False,
                "mutations_performed": False,
            }
        return {
            "success": all(item.get("success", False) for item in checks.values()),
            "service": "DatabaseInfrastructureService",
            "checks": checks,
            "mutations_performed": False,
        }


__all__ = ["DatabaseInfrastructureService"]
