"""Salesforce Streaming API metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_streaming_api",
    "scope": "PushTopics, generic streaming, and change data capture subscriptions where supported.",
    "authentication_setup": "Streaming permissions, supported API version, and event channel configuration.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
