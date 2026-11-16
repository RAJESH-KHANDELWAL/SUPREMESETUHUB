"""Cohere CORE operation guardrails.

CORE validates policy metadata only. Provider writes and model operations must
be implemented in the approved API/ENGINE workflow with separate authorization.
"""
from __future__ import annotations

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
