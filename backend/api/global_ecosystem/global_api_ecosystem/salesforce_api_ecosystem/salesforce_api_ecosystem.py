"""Salesforce provider-owned API ecosystem metadata and adapter linkage."""
from __future__ import annotations

PROVIDER_API_ECOSYSTEM = {
    "provider_id": "salesforce",
    "name": "GLOBAL SALESFORCE API ECOSYSTEM",
    "families": [
        "identity_oauth", "rest", "soap", "composite", "bulk_api_2",
        "platform_events_pubsub", "streaming", "metadata_tooling", "apex",
        "files_content", "service_cloud", "marketing_cloud", "data_cloud",
        "analytics_crm_analytics",
    ],
    "scope": "CRM records, platform APIs, identity, events, metadata, and Salesforce cloud product APIs subject to org configuration, entitlements, and OAuth scopes.",
    "status": "LIVE_VERIFICATION_IMPLEMENTED",
    "adapter_path": "backend/integrations/providers/salesforce.py",
    "live_connection_verified": False,
    "service_family_count": 14,
    "credential_source": "deployment_secret_manager",
    "credential_persistence_implemented": False,
}

__all__ = ["PROVIDER_API_ECOSYSTEM"]
