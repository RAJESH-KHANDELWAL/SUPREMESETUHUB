"""DigitalOcean CORE operation guardrails."""
BLOCKED_OPERATIONS=frozenset({"delete_droplet","delete_database","delete_space","change_billing","rotate_provider_token","destroy_project"})
def ensure_operation_allowed(operation):
    if not isinstance(operation,str) or not operation.strip(): raise ValueError("operation must be non-empty")
    if operation.strip().lower() in BLOCKED_OPERATIONS: raise PermissionError("operation requires explicit authorization and approved API/ENGINE workflow")
