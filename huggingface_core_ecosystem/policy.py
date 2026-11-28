"""Hugging Face CORE security and lifecycle guardrails."""
from dataclasses import dataclass
@dataclass(frozen=True)
class HuggingFaceCorePolicy:
    require_tenant_context: bool = True
    require_explicit_authorization_for_mutations: bool = True
    require_approval_for_production_changes: bool = True
    allow_remote_operations: bool = False
    allow_secret_values_in_core: bool = False
    require_external_secret_store: bool = True
    require_license_metadata_for_model_use: bool = True
    require_usage_and_quota_checks_in_execution_layer: bool = True
    require_audit_for_admin_billing_and_deployment_actions: bool = True
    def validate_product(self, item: dict) -> None:
        if not item.get("product_id") or not item.get("api_module"):
            raise ValueError("PRODUCT_ID_AND_API_MODULE_REQUIRED")
        if item.get("live_connection_verified") is not False:
            raise ValueError("CORE_CANNOT_ASSERT_LIVE_CONNECTION")
        if item.get("remote_operations_enabled") is not False:
            raise ValueError("CORE_REMOTE_OPERATIONS_MUST_REMAIN_DISABLED")
