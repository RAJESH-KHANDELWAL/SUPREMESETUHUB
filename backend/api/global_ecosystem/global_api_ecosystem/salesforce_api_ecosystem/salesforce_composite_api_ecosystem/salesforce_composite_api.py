"""Salesforce Composite API metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_composite_api",
    "scope": "Composite, batch, tree, and graph-style grouped REST operations.",
    "authentication_setup": "REST API OAuth token and permissions for every referenced object/resource.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
