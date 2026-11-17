"""Plan-only storage operations. Never transfers, overwrites or deletes data."""
from .catalog import get_provider
from .policy import authorize_plan

SUPPORTED = {"LIST", "DESCRIBE", "UPLOAD", "DOWNLOAD", "COPY", "MOVE", "DELETE", "RESTORE", "BACKUP"}


def build_plan(*, provider_id, tenant_id, actor_id, operation, resource_id=None):
    """Build a non-executing plan after validating its input contract."""
    if not isinstance(provider_id, str) or not provider_id.strip():
        raise ValueError("STORAGE_PROVIDER_ID_REQUIRED")
    normalized_provider_id = provider_id.strip().lower()
    if get_provider(normalized_provider_id) is None:
        raise ValueError("UNKNOWN_STORAGE_PROVIDER")

    if not isinstance(operation, str) or not operation.strip():
        raise ValueError("STORAGE_OPERATION_REQUIRED")
    normalized_operation = operation.strip().upper()
    if normalized_operation not in SUPPORTED:
        raise ValueError("UNSUPPORTED_STORAGE_OPERATION")

    if resource_id is not None and (not isinstance(resource_id, str) or not resource_id.strip()):
        raise ValueError("INVALID_STORAGE_RESOURCE_ID")

    policy = authorize_plan(
        tenant_id=tenant_id,
        actor_id=actor_id,
        operation=normalized_operation,
    )
    return {
        "success": True,
        "provider_id": normalized_provider_id,
        "operation": normalized_operation,
        "resource_id": resource_id,
        "policy": policy,
        "plan_only": True,
        "provider_call_performed": False,
        "data_transferred": False,
    }
