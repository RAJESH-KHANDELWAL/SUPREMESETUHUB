"""Salesforce REST API service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_rest_api",
    "name": "SALESFORCE REST API API ECOSYSTEM",
    "scope": "SObjects, records, queries, describe resources, and REST resources.",
    "authentication_setup": "Connected App OAuth and API-enabled user with object/field permissions.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
