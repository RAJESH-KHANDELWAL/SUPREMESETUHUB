"""Salesforce Marketing Cloud metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_marketing_cloud_api",
    "scope": "Marketing Cloud REST/SOAP resources, messaging, journeys, and assets.",
    "authentication_setup": "Marketing Cloud Installed Package, tenant-specific auth base URI, scopes, and business-unit access.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
