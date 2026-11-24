"""Azure App Service and Functions service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_azure_app_service_functions_api",
    "name": "AZURE APP SERVICE AND FUNCTIONS API ECOSYSTEM",
    "scope": "Web apps, deployments, Function Apps, and serverless application management.",
    "authentication_setup": "Azure subscription, resource group, service principal, and scoped Contributor/Web Plan permissions.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
