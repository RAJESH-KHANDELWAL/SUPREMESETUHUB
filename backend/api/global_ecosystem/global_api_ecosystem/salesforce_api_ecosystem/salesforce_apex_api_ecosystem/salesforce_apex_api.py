"""Salesforce Apex APIs metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_apex_api",
    "scope": "Apex execution and supported Apex REST interfaces for controlled automation.",
    "authentication_setup": "Appropriate Apex authoring/execution permissions; restrict execution to trusted administrators.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
