"""Application service composing the independently owned ecosystem layers.

The API owns transport orchestration only. Catalogue policy stays in CORE,
discovery in ENGINE, grounded context in AI, records in DATABASE, assets in
STORAGE, and remote synchronization in CLOUD.
"""
from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem.service import (
    GlobalCultureServiceWorkBusinessCore,
)
from backend.engine.global_ecosystem.global_engine_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_engine_ecosystem.manager import (
    GlobalCultureServiceWorkBusinessEngine,
)
from backend.ai.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_ai_ecosystem.assistant import (
    GlobalCultureServiceWorkBusinessAI,
)
from backend.database.global_ecosystem.global_database_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_database_ecosystem.repository import (
    GlobalCultureServiceWorkBusinessRepository,
)
from backend.storage.global_ecosystem.global_storage_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_storage_ecosystem.manager import (
    GlobalCultureServiceWorkBusinessStorage,
)
from backend.cloud.global_ecosystem.global_cloud_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_cloud_ecosystem.bridge import (
    GlobalCultureServiceWorkBusinessCloud,
)


class GlobalCultureServiceWorkBusinessAPIService:
    """Coordinate layer calls without absorbing their implementation."""

    ALLOWED_DOMAINS = frozenset({"SERVICE", "WORK", "BUSINESS"})

    def __init__(
        self,
        *,
        core: GlobalCultureServiceWorkBusinessCore | None = None,
        engine: GlobalCultureServiceWorkBusinessEngine | None = None,
        ai: GlobalCultureServiceWorkBusinessAI | None = None,
        repository: GlobalCultureServiceWorkBusinessRepository | None = None,
        storage: GlobalCultureServiceWorkBusinessStorage | None = None,
        cloud: GlobalCultureServiceWorkBusinessCloud | None = None,
    ) -> None:
        self.core = core or GlobalCultureServiceWorkBusinessCore()
        self.engine = engine or GlobalCultureServiceWorkBusinessEngine(self.core)
        self.ai = ai or GlobalCultureServiceWorkBusinessAI(self.engine)
        self.repository = repository or GlobalCultureServiceWorkBusinessRepository()
        self.storage = storage or GlobalCultureServiceWorkBusinessStorage()
        self.cloud = cloud or GlobalCultureServiceWorkBusinessCloud()

    @classmethod
    def _validate_domain(cls, domain: str | None) -> str | None:
        if domain is None:
            return None
        normalized = domain.strip().upper()
        if normalized not in cls.ALLOWED_DOMAINS:
            raise ValueError("INVALID_DOMAIN")
        return normalized

    def status(self) -> dict[str, Any]:
        database_status = self.repository.health()
        storage_status = self.storage.status()
        cloud_status = self.cloud.status()
        return {
            "ecosystem_id": self.core.ecosystem_id,
            "status": "FOUNDATION_READY",
            "layers": {
                "api": {"component": "API", "status": "READY"},
                "core": self.core.status(),
                "engine": self.engine.status(),
                "ai": self.ai.status(),
                "database": database_status,
                "storage": storage_status,
                "cloud": cloud_status,
            },
            "capabilities": {
                "catalogue_discovery": True,
                "domain_filtering": True,
                "relevance_search": True,
                "retrieval_grounded_ai_context": True,
                # DatabaseService.health() exposes a boolean, not a status string.
                "record_persistence": database_status.get("healthy") is True,
                "asset_storage": storage_status.get("status") == "READY",
                "cloud_sync": cloud_status.get("sync_enabled") is True,
            },
            "scope": {
                "domains": sorted(self.ALLOWED_DOMAINS),
                "taxonomy_only": True,
                "live_providers": False,
                "live_jobs_or_gigs": False,
                "external_ai_provider_invoked": False,
            },
        }

    def catalogue(self, domain: str | None = None) -> list[dict[str, Any]]:
        return self.engine.catalogue(self._validate_domain(domain))

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        normalized_query = str(query or "").strip()
        if not normalized_query:
            raise ValueError("SEARCH_QUERY_REQUIRED")
        return self.engine.search(normalized_query, self._validate_domain(domain))

    def ai_context(self, question: str, domain: str | None = None) -> dict[str, Any]:
        normalized_question = str(question or "").strip()
        if not normalized_question:
            raise ValueError("AI_QUESTION_REQUIRED")
        return self.ai.build_context(
            normalized_question, self._validate_domain(domain)
        )

    def validate_record(self, record: dict[str, Any]) -> list[str]:
        return self.core.validate(record)

    def can_publish_record(self, record: dict[str, Any]) -> bool:
        return self.core.can_publish(record)

    def save_record(self, record: dict[str, Any]) -> dict[str, Any]:
        """Validate with CORE and persist through the DATABASE repository."""
        errors = self.core.validate(record)
        if errors:
            raise ValueError("RECORD_VALIDATION_FAILED:" + ",".join(errors))
        self.repository.save(record)
        return {
            "record_id": record["record_id"],
            "status": str(record.get("status", "DRAFT")).upper(),
            "publication_allowed": self.core.can_publish(record),
        }

    def get_record(self, record_id: str) -> dict[str, Any] | None:
        normalized_id = str(record_id or "").strip()
        if not normalized_id:
            raise ValueError("RECORD_ID_REQUIRED")
        return self.repository.get(normalized_id)

    def search_records(
        self,
        query: str = "",
        capability_id: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        normalized_query = str(query or "").strip()
        normalized_capability = (
            str(capability_id).strip() if capability_id is not None else None
        )
        return self.repository.search(
            normalized_query, normalized_capability, limit
        )

    def store_asset(self, stream: Any, filename: str, max_bytes: int = 25 * 1024 * 1024) -> dict[str, Any]:
        """Delegate binary persistence to STORAGE; the API stores no file bytes."""
        return self.storage.store_asset(stream, filename, max_bytes)

    def open_asset(self, storage_key: str) -> Any:
        return self.storage.open_asset(storage_key)

    def delete_asset(self, storage_key: str) -> bool:
        return self.storage.delete_asset(storage_key)

    def sync_to_cloud(self, payload: dict[str, Any]) -> Any:
        """Delegate sync to CLOUD; unconfigured adapters fail explicitly."""
        return self.cloud.sync(payload)
