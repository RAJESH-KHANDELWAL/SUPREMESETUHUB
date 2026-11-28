"""Security, publishing and lifecycle guardrails for WEBSITE CORE metadata."""
from __future__ import annotations
from dataclasses import dataclass

PROVIDER_STATES = ("CATALOG_ONLY", "ELIGIBILITY_REQUIRED", "VERIFIED")

@dataclass(frozen=True)
class WebsiteCorePolicy:
    require_explicit_authorization_for_changes: bool = True
    require_approval_for_production_changes: bool = True
    require_backup_reference_before_destructive_change: bool = True
    allow_remote_operations: bool = False
    allow_secret_values_in_metadata: bool = False
    require_external_secret_store: bool = True
    require_consent_metadata_for_tracking: bool = True

    def validate_provider_record(self, record: dict) -> None:
        if not record.get("provider_id") or not record.get("name"):
            raise ValueError("WEBSITE_PROVIDER_ID_AND_NAME_REQUIRED")
        if record.get("status") not in PROVIDER_STATES:
            raise ValueError("WEBSITE_PROVIDER_STATUS_INVALID")
        if record.get("live_connection_verified") is not False:
            raise ValueError("WEBSITE_CORE_MUST_NOT_CLAIM_LIVE_CONNECTION")
        if record.get("remote_operations_enabled") is not False:
            raise ValueError("WEBSITE_CORE_REMOTE_OPERATIONS_MUST_REMAIN_DISABLED")
