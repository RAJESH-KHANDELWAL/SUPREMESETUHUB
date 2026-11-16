"""Safety and governance policies for infrastructure integrations."""
GOVERNANCE_POLICIES = {
    "default_provider_state": "NOT_CONFIGURED",
    "default_integration_state": "CATALOG_ONLY",
    "require_explicit_adapter": True,
    "require_credentials_from_secret_store": True,
    "never_store_secret_values_in_catalog": True,
    "require_authorization_before_mutation": True,
    "require_audit_record_for_mutations": True,
    "require_health_verification_after_mutation": True,
    "read_only_discovery_by_default": True,
    "destructive_operations_disabled_by_default": True,
}

def get_governance_policies() -> dict:
    """Return a copy so callers cannot mutate module policy state."""
    return dict(GOVERNANCE_POLICIES)
