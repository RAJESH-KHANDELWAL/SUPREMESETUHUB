"""Azure DevOps service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_devops_api",
    "name": "AZURE DEVOPS API ECOSYSTEM",
    "scope": "Organizations, projects, repositories, pipelines, builds, work items, and artifacts.",
    "authentication_setup": "Azure DevOps organization, scoped PAT or Entra OAuth, and project-level permissions.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
