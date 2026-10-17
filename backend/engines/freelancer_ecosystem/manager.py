"""GLOBAL FREELANCER ECOSYSTEM orchestration engine."""
from __future__ import annotations

from typing import Any

from backend.database.freelancer_ecosystem import (
    FreelancerEcosystemRepository,
    RECORD_TYPES,
)
from backend.engines.storage import StorageEngine
from backend.storage.provider_registry import get_storage_provider_status


ECOSYSTEM_ID = "GLOBAL-FREELANCER-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL FREELANCER ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "SUPREMESETUHUB"


class FreelancerEcosystemEngine:
    """Connect API-facing freelancer workflows to central database and storage."""

    def __init__(self, db_path: str | None = None) -> None:
        self.repository = FreelancerEcosystemRepository(db_path=db_path)

    @staticmethod
    def catalog() -> dict[str, Any]:
        return {
            "ecosystem_id": ECOSYSTEM_ID,
            "name": ECOSYSTEM_NAME,
            "parent_ecosystem_id": PARENT_ECOSYSTEM_ID,
            "record_types": sorted(RECORD_TYPES),
            "capabilities": [
                "FREELANCER_PROFILES",
                "SERVICE_OFFERS",
                "PORTFOLIO_METADATA",
                "PROJECT_BRIEFS",
                "APPLICATION_TRACKING",
                "WORK_HISTORY",
                "CENTRAL_DATABASE_METADATA",
                "CENTRAL_STORAGE_ASSET_REFERENCES",
            ],
            "provider_hierarchy": [
                {"provider": "Google", "position": 1, "status": "PLANNED_NOT_VERIFIED"},
                {"provider": "Google Cloud", "position": 2, "status": "PLANNED_NOT_VERIFIED"},
                {"provider": "Microsoft", "position": 3, "status": "PLANNED_NOT_VERIFIED"},
                {"provider": "AWS", "position": 4, "status": "ADAPTER_STATUS_REQUIRES_LIVE_VERIFICATION"},
                {"provider": "Other approved providers", "position": 5, "status": "ADAPTER_SPECIFIC"},
            ],
            "runtime_policy": {
                "render": "TEMPORARY_TEST_RUNTIME_ONLY",
                "production_data_migration": "NOT_APPROVED",
            },
        }

    def status(self) -> dict[str, Any]:
        storage = get_storage_provider_status()
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "name": ECOSYSTEM_NAME,
            "status": "FOUNDATION_SCAFFOLD_CONNECTED_TO_CENTRAL_DATABASE",
            "database": {
                "system": "SUPREMESETUHUB_CENTRAL_DATABASE",
                "implementation": "CURRENT_REPOSITORY_DATABASE_SERVICE",
                "storage": "METADATA_AND_REFERENCES_ONLY",
                "durability": "NOT_VERIFIED_BY_THIS_STATUS_ENDPOINT",
            },
            "storage": {
                "system": "SUPREMESETUHUB_CENTRAL_STORAGE_ENGINE",
                "provider": storage,
                "asset_api": "/api/v1/storage/files",
                "note": "File bytes stay in the storage engine; this ecosystem stores authorized asset references.",
            },
            "provider_integrations": {
                "google_drive": "NOT_IMPLEMENTED",
                "google_cloud_storage": "SCAFFOLD_ONLY",
                "microsoft_onedrive": "NOT_IMPLEMENTED",
                "aws_s3": "ADAPTER_EXISTS_LIVE_CONNECTION_NOT_VERIFIED",
            },
            "production_ready": False,
        }

    def create_record(
        self,
        *,
        owner_id: str,
        record_type: str,
        title: str,
        payload: dict[str, Any],
        storage_asset_ids: list[str] | None = None,
        status: str = "DRAFT",
    ) -> dict[str, Any]:
        # Never attach arbitrary asset IDs: verify every referenced asset against
        # the existing storage engine's owner/access policy first.
        for asset_id in storage_asset_ids or []:
            asset = StorageEngine().get_asset(
                asset_id,
                actor_id=owner_id,
                action="VIEW",
            )
            if asset is None:
                raise ValueError("STORAGE_ASSET_NOT_FOUND_OR_NOT_AUTHORIZED")
        return self.repository.create(
            owner_id=owner_id,
            record_type=record_type,
            title=title,
            payload=payload,
            storage_asset_ids=storage_asset_ids,
            status=status,
        )

    def list_records(
        self,
        *,
        owner_id: str,
        record_type: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        return self.repository.list_for_owner(
            owner_id=owner_id,
            record_type=record_type,
            limit=limit,
        )

    def get_record(self, record_id: str, *, owner_id: str) -> dict[str, Any] | None:
        return self.repository.get(record_id, owner_id=owner_id)
