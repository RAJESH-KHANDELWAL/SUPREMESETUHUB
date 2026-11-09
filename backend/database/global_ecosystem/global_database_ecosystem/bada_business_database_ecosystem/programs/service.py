"""Persistence service; reads canonical provider records only when explicitly asked."""

from __future__ import annotations

from .models import BadaBusinessProgramRecord
from .repository import BadaBusinessProgramRepository


class BadaBusinessProgramPersistenceService:
    CANONICAL_CATALOG = "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog"

    def __init__(self, repository=None, catalog_loader=None):
        self.repository = repository or BadaBusinessProgramRepository()
        self.catalog_loader = catalog_loader

    @staticmethod
    def _identity(owner_user_id: str):
        if not isinstance(owner_user_id, str) or not owner_user_id.strip():
            raise ValueError("owner_user_id is required")

    def save_snapshot(self, owner_user_id: str, program: dict, *, source_version: str = ""):
        self._identity(owner_user_id)
        if not isinstance(program, dict):
            raise ValueError("program must be a mapping")
        program_id = str(program.get("program_id") or "").strip().lower()
        name = str(program.get("name") or "").strip()
        if not program_id or not name:
            raise ValueError("program_id and name are required")
        # Preserve an explicit status if known; otherwise mark as unconfirmed.
        status = str(program.get("status") or "UNCONFIRMED").upper()
        if status not in {"AVAILABLE", "UPCOMING", "PAST_EVENT_DATE", "UNCONFIRMED", "UNKNOWN"}:
            status = "UNCONFIRMED"
        record = BadaBusinessProgramRecord(
            owner_user_id=owner_user_id,
            program_id=program_id,
            program_name=name,
            program_status=status,
            source_version=source_version,
            snapshot=program,
        )
        return self.repository.upsert(record)

    def sync_canonical_catalog(self, owner_user_id: str, *, source_version: str = ""):
        self._identity(owner_user_id)
        if self.catalog_loader is None:
            from backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog import list_programs
            programs = list_programs()
        else:
            programs = self.catalog_loader()
        saved = [
            self.save_snapshot(owner_user_id, program, source_version=source_version)
            for program in programs
        ]
        return {
            "success": True,
            "owner_user_id": owner_user_id,
            "source_catalog": self.CANONICAL_CATALOG,
            "records_seen": len(programs),
            "records_saved": len(saved),
            "data": saved,
        }

    def get_program(self, owner_user_id: str, program_id: str):
        self._identity(owner_user_id)
        return self.repository.get(owner_user_id, str(program_id).strip().lower())

    def list_programs(self, owner_user_id: str, *, program_status: str | None = None, limit: int = 100):
        self._identity(owner_user_id)
        return self.repository.list(owner_user_id, program_status=program_status, limit=limit)

    def delete_program(self, owner_user_id: str, program_id: str):
        self._identity(owner_user_id)
        return self.repository.delete(owner_user_id, str(program_id).strip().lower())
