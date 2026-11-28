"""Fail-closed policy for the metadata-only Database Core."""
POLICY = {
    "allow_live_connections": False,
    "allow_query_execution": False,
    "allow_schema_mutation": False,
    "allow_migrations": False,
    "allow_provisioning": False,
    "allow_raw_credentials": False,
    "require_secret_references": True,
    "require_tenant_isolation": True,
    "require_audit_metadata": True,
    "require_encryption_policy": True,
}

def get_policy():
    return dict(POLICY)
