"""Read-only controller for the existing backend database services."""
from __future__ import annotations

from typing import Any

from .service import DatabaseInfrastructureService


class DatabaseInfrastructureController:
    """Expose database health checks without owning persistence or migrations."""

    def __init__(self, service: DatabaseInfrastructureService | None = None) -> None:
        self.service = service or DatabaseInfrastructureService()

    def check_all(self, *, check_mysql: bool = False) -> dict[str, Any]:
        return self.service.check_all(check_mysql=check_mysql)

    def check_sqlite_runtime(self) -> dict[str, Any]:
        return self.service.check_sqlite_runtime()

    def check_central_mysql(self) -> dict[str, Any]:
        return self.service.check_central_mysql()


__all__ = ["DatabaseInfrastructureController"]
