"""Metadata-only Twilio discovery and dependency orchestration."""
from __future__ import annotations
from .catalog import get_catalog, list_products
from .service import TwilioCoreService

class TwilioCoreOrchestrator:
    def __init__(self) -> None:
        self._service = TwilioCoreService()

    def health(self) -> dict:
        return self._service.health()

    def products(self, *, enabled_only: bool = False) -> list[dict]:
        return list_products(enabled_only=enabled_only)

    def dependency_map(self) -> dict:
        catalog = get_catalog()
        return {
            "core": catalog["ecosystem_id"],
            "dependencies": [
                {"layer": "API", "path": catalog["api_catalog_ref"], "required_for": ["authentication", "transport", "webhooks"]},
                {"layer": "ENGINE", "path": "backend/engine/global_ecosystem/global_engine_ecosystem/twilio_engine_ecosystem", "required_for": ["execution", "queues", "retries"]},
                {"layer": "DATABASE", "path": "backend/database", "required_for": ["durable tenant records", "audit persistence"]},
                {"layer": "STORAGE", "path": "backend/storage/global_ecosystem/global_storage_ecosystem/twilio_storage_ecosystem", "required_for": ["media artifacts"]},
            ],
            "api_calls_performed": False,
            "live_connection_verified": False,
        }
