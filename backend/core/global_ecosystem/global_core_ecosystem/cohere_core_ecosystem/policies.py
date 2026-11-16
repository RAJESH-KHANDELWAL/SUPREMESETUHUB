"""Safety and operation policies; CORE never performs provider-side writes."""
BLOCKED_OPERATIONS = frozenset({
    "train_model", "fine_tune", "delete_model", "create_deployment",
    "rotate_provider_key", "change_billing", "submit_payment",
})

def ensure_operation_allowed(operation: str) -> None:
    if operation.strip().lower() in BLOCKED_OPERATIONS:
        raise PermissionError(f"Operation requires an explicitly authorized ENGINE workflow: {operation}")
