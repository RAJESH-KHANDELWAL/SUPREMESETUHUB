BLOCKED_OPERATIONS=frozenset({"delete_model","change_billing","rotate_provider_key","create_deployment","delete_dataset"})
def ensure_operation_allowed(operation):
    if not isinstance(operation,str) or not operation.strip(): raise ValueError("operation must be non-empty")
    if operation.strip().lower() in BLOCKED_OPERATIONS: raise PermissionError("operation requires approved API/ENGINE authorization")
