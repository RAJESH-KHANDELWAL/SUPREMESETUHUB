"""Safety policies for Bada Business cloud operations."""
from __future__ import annotations

# Operations that can change infrastructure or destroy/alter data require
# explicit approval from the caller before reaching a provider adapter.
BADA_BUSINESS_CLOUD_POLICY = {
    "default_effect": "deny",
    "approval_required_by_default": True,
    "read_only_operations": (
        "inspect_hosting", "inspect_storage", "download_object",
        "inspect_database_service", "inspect_edge", "inspect_backup",
        "inspect_security", "inspect_health", "read_audit_events",
    ),
    "approval_required_operations": (
        "deploy_application", "rollback_deployment", "upload_object",
        "delete_object", "provision_database_service", "purge_cache",
        "update_dns", "create_backup", "restore_backup",
    ),
    "credentials_source": "injected_provider_adapter_only",
    "never_log_secrets": True,
}
