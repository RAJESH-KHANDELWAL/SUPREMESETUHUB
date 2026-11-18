"""Cohere CORE policy guardrails.

CORE validates metadata and caller context only. Provider writes and model
operations must execute through an approved API/ENGINE workflow.
"""
from __future__ import annotations

from typing import Any

from .catalog import CAPABILITIES

BLOCKED_OPERATIONS = frozenset({
    "train_model",
    "fine_tune",
    "delete_model",
    "create_deployment",
    "rotate_provider_key",
    "change_billing",
    "submit_payment",
    "delete_dataset",
    "delete_connector",
})
SENSITIVE_OPERATIONS = frozenset({
    "create_connector",
    "update_connector",
    "delete_connector",
    "create_dataset",
    "update_dataset",
    "delete_dataset",
    "create_deployment",
    "delete_deployment",
    "change_billing",
})
SENSITIVE_CAPABILITY_MARKERS = ("DELETE", "WRITE", "ADMIN", "BILLING", "DEPLOY", "TRAIN")


class CohereCorePolicyError(PermissionError):
    """Raised when a Cohere CORE policy boundary is violated."""


def ensure_operation_allowed(operation: str, *, explicitly_authorized: bool = False) -> None:
    if not isinstance(operation, str) or not operation.strip():
        raise ValueError("operation must be a non-empty string")
    normalized = operation.strip().lower()
    if normalized in BLOCKED_OPERATIONS:
        raise PermissionError(
            f"Operation is not executable from CORE and requires an approved ENGINE workflow: {normalized}"
        )
    if normalized in SENSITIVE_OPERATIONS and not explicitly_authorized:
        raise PermissionError(f"Explicit authorization and audit are required: {normalized}")


class CohereCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None:
            raise CohereCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator):
            raise CohereCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_capability(capability: str) -> None:
        if not isinstance(capability, str) or capability.strip().lower() not in CAPABILITIES:
            raise CohereCorePolicyError("CAPABILITY_NOT_REGISTERED")

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = capability.upper()
        return (
            "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION"
            if any(marker in upper for marker in SENSITIVE_CAPABILITY_MARKERS)
            else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
        )

    @staticmethod
    def safe_module_summary(module: dict[str, Any]) -> dict[str, Any]:
        blocked = {"token", "access_token", "refresh_token", "client_secret", "api_key", "secret", "password"}
        return {key: value for key, value in module.items() if key.casefold() not in blocked}


__all__ = [
    "BLOCKED_OPERATIONS",
    "SENSITIVE_OPERATIONS",
    "CohereCorePolicy",
    "CohereCorePolicyError",
    "ensure_operation_allowed",
]
