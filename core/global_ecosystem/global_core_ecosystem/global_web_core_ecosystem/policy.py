"""Security and lifecycle guardrails for WEB CORE metadata."""
from __future__ import annotations
from dataclasses import dataclass

PROVIDER_STATES = ("CATALOG_ONLY", "ELIGIBILITY_REQUIRED", "VERIFIED")
RISK_LEVELS = ("LOW", "MEDIUM", "HIGH", "CRITICAL")

@dataclass(frozen=True)
class WebCorePolicy:
    require_explicit_authorization_for_changes: bool = True
    allow_remote_operations: bool = False
    allow_secret_values_in_metadata: bool = False
    require_external_secret_store: bool = True
    production_requires_approval: bool = True

    def validate_provider_record(self, record: dict) -> None:
        if not record.get("provider_id") or not record.get("name"):
            raise ValueError("WEB_PROVIDER_ID_AND_NAME_REQUIRED")
        if record.get("status") not in PROVIDER_STATES:
            raise ValueError("WEB_PROVIDER_STATUS_INVALID")
        if record.get("live_connection_verified") is not False:
            raise ValueError("WEB_CORE_MUST_NOT_CLAIM_LIVE_CONNECTION")
        if record.get("remote_operations_enabled") is not False:
            raise ValueError("WEB_CORE_REMOTE_OPERATIONS_MUST_REMAIN_DISABLED")
