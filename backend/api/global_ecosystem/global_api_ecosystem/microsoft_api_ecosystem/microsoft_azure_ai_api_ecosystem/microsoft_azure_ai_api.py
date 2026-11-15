"""Azure AI Services service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_azure_ai_api",
    "name": "AZURE AI SERVICES API ECOSYSTEM",
    "scope": "Azure AI services, Azure OpenAI deployments, and AI resource management.",
    "authentication_setup": "Azure resource endpoint, deployment name, approved API key or Entra identity, and region access.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
