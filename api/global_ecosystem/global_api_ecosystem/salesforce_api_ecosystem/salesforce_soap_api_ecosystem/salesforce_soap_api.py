"""Salesforce SOAP API service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_soap_api",
    "name": "SALESFORCE SOAP API API ECOSYSTEM",
    "scope": "Enterprise and Partner SOAP interfaces for metadata-aware and generic integrations.",
    "authentication_setup": "WSDL for target org/API version and OAuth session or supported authentication.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
