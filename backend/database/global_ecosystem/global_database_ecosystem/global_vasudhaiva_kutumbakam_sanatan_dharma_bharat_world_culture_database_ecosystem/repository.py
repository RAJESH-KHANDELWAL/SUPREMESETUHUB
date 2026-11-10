"""Governed repository facade for cultural knowledge persistence."""
from __future__ import annotations
from typing import Any
from backend.database.cultural_knowledge_repository import CulturalKnowledgeRepository
from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem.governance import validate_cultural_record

class GlobalCulturalRepository:
    def __init__(self, repository: CulturalKnowledgeRepository | None = None) -> None:
        self.repository = repository or CulturalKnowledgeRepository()

    def initialize(self) -> None:
        self.repository.initialize()

    def save(self, record: dict[str, Any]) -> None:
        errors = validate_cultural_record(record)
        if errors:
            raise ValueError("CULTURAL_RECORD_VALIDATION_FAILED:" + ",".join(errors))
        self.repository.save(record)

    def get(self, record_id: str) -> dict[str, Any] | None:
        if not str(record_id).strip():
            raise ValueError("CULTURAL_RECORD_ID_REQUIRED")
        return self.repository.get(record_id)

    def search(self, query: str, domain_id: str | None = None, limit: int = 30) -> list[dict[str, Any]]:
        return self.repository.search(query, domain_id=domain_id, limit=limit)

    def health(self) -> dict[str, Any]:
        try:
            self.initialize()
            return {"status": "READY", "table": self.repository.TABLE}
        except Exception as exc:
            return {"status": "UNAVAILABLE", "error_type": type(exc).__name__}
