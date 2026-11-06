"""Aggregate readiness for the CORE, database, and storage foundation.

This service reports implemented capabilities honestly: SQLite and the storage
metadata registry can be healthy while physical blob storage remains absent.
"""
from __future__ import annotations

from typing import Any

from backend.database.service import DatabaseService
from backend.engines.storage import StorageEngine


class CoreReadinessService:
    """Return a single, truthful readiness snapshot for core persistence."""

    def __init__(
        self,
        database: DatabaseService | None = None,
        storage: StorageEngine | None = None,
    ) -> None:
        self.database = database or DatabaseService()
        self.storage = storage or StorageEngine()

    def snapshot(self) -> dict[str, Any]:
        """Check the live database and storage registry without hiding failures."""
        try:
            database_health = self.database.health()
            database_ready = bool(database_health.get("healthy"))
        except Exception:
            database_health = {"database": "SQLITE", "healthy": False, "connected": False}
            database_ready = False

        try:
            storage_health = self.storage.health()
            storage_registry_ready = storage_health.get("database_registry") == "READY"
        except Exception:
            storage_health = {
                "engine": "AI Storage Engine",
                "health": "UNHEALTHY",
                "database_registry": "UNAVAILABLE",
                "physical_storage": "NOT_CONFIGURED",
                "physical_storage_configured": False,
            }
            storage_registry_ready = False

        core_ready = database_ready and storage_registry_ready
        physical_storage_ready = bool(
            storage_health.get("physical_storage_configured", False)
        )
        if not core_ready:
            overall = "UNHEALTHY"
        elif not physical_storage_ready:
            overall = "DEGRADED"
        else:
            overall = "HEALTHY"
        return {
            "service": "MAIN BASE FOUNDATION",
            "core": "READY" if core_ready else "DEGRADED",
            "overall": overall,
            "components": {
                "core": {"status": "READY" if core_ready else "DEGRADED"},
                "database": {
                    "status": "READY" if database_ready else "UNAVAILABLE",
                    "engine": database_health.get("database", "SQLITE"),
                    "connected": bool(database_health.get("connected")),
                },
                "storage": {
                    "status": "METADATA_ONLY" if storage_registry_ready else "UNAVAILABLE",
                    "metadata_registry": storage_health.get("database_registry", "UNAVAILABLE"),
                    "physical_storage": storage_health.get("physical_storage", "NOT_CONFIGURED"),
                    "physical_storage_configured": bool(
                        storage_health.get("physical_storage_configured", False)
                    ),
                },
            },
        }
