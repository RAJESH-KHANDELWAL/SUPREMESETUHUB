"""CORE policy guardrails; no provider authentication or transaction execution."""
from __future__ import annotations
SENSITIVE_OPERATIONS = frozenset({"REGISTRATION_SUBMIT", "PAYMENT_PROCESS", "ACCOUNT_CHANGE", "LEAD_SUBMIT", "ORDER_CREATE", "REFUND"})

class BadaBusinessPolicyError(PermissionError):
    pass

def require_text(value: str, field: str = "value") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field.upper()}_REQUIRED")
    return value.strip()

def ensure_operation_is_catalog_only(operation: str) -> None:
    operation = require_text(operation, "operation").upper()
    if operation in SENSITIVE_OPERATIONS:
        raise BadaBusinessPolicyError(f"{operation}_DISABLED_IN_CORE")

def registration_readiness() -> dict[str, object]:
    return {"draft_validation": True, "provider_submission": False, "payment_processing": False, "live_provider_connection": False, "reason": "No verified provider API or transaction adapter is configured."}
