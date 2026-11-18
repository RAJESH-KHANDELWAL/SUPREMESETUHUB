"""Salesforce Platform Events and Pub/Sub metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_platform_events_pubsub_api",
    "scope": "Event publishing and subscription through Platform Events and Pub/Sub API.",
    "authentication_setup": "Pub/Sub API access, event channel permissions, OAuth, and event retention awareness.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
