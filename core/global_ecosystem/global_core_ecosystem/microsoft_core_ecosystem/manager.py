"""Canonical manager and provider/product catalog for Microsoft Core."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

_PRODUCT_ROWS: list[tuple[str, str, str, list[str]]] = [
    ("microsoft_azure_ai_core_ecosystem", "Microsoft Azure AI", "AI_ML_AND_INTELLIGENCE", ["AZURE_AI_SERVICE_METADATA", "MODEL_DEPLOYMENT_METADATA", "AI_GOVERNANCE_BOUNDARY"]),
    ("microsoft_azure_app_service_functions_core_ecosystem", "Azure App Service and Functions", "AZURE_COMPUTE_AND_APPLICATION_HOSTING", ["APP_HOSTING_METADATA", "SERVERLESS_FUNCTION_METADATA"]),
    ("microsoft_azure_compute_core_ecosystem", "Azure Compute", "AZURE_COMPUTE_AND_APPLICATION_HOSTING", ["VIRTUAL_MACHINE_METADATA", "CONTAINER_COMPUTE_METADATA"]),
    ("microsoft_azure_database_core_ecosystem", "Azure Database", "AZURE_DATA_AND_STORAGE", ["MANAGED_DATABASE_METADATA", "DATABASE_CONFIGURATION_BOUNDARY"]),
    ("microsoft_azure_network_dns_core_ecosystem", "Azure Networking and DNS", "AZURE_NETWORKING", ["VIRTUAL_NETWORK_METADATA", "DNS_AND_TRAFFIC_METADATA"]),
    ("microsoft_azure_storage_core_ecosystem", "Azure Storage", "AZURE_DATA_AND_STORAGE", ["OBJECT_STORAGE_METADATA", "FILE_AND_QUEUE_STORAGE_METADATA"]),
    ("microsoft_devops_core_ecosystem", "Azure DevOps", "DEVELOPER_AND_APPLICATION_PLATFORM", ["REPOSITORY_METADATA", "PIPELINE_AND_WORK_ITEM_METADATA"]),
    ("microsoft_entra_identity_oauth_core_ecosystem", "Microsoft Entra ID and OAuth", "IDENTITY_AND_ADMINISTRATION", ["IDENTITY_PROVIDER_METADATA", "OAUTH_CONFIGURATION_BOUNDARY", "TENANT_DIRECTORY_METADATA"]),
    ("microsoft_graph_core_ecosystem", "Microsoft Graph", "MICROSOFT_365_AND_COLLABORATION", ["GRAPH_RESOURCE_DISCOVERY", "MICROSOFT_365_RESOURCE_METADATA"]),
    ("microsoft_office_documents_core_ecosystem", "Microsoft Office Documents", "MICROSOFT_365_AND_COLLABORATION", ["DOCUMENT_PRODUCT_METADATA", "OFFICE_FILE_WORKFLOW_BOUNDARY"]),
    ("microsoft_onedrive_sharepoint_core_ecosystem", "OneDrive and SharePoint", "MICROSOFT_365_AND_COLLABORATION", ["FILE_STORAGE_METADATA", "SITE_AND_LIBRARY_METADATA"]),
    ("microsoft_outlook_mail_calendar_core_ecosystem", "Outlook Mail and Calendar", "MICROSOFT_365_AND_COLLABORATION", ["MAILBOX_METADATA", "CALENDAR_METADATA"]),
    ("microsoft_planner_tasks_core_ecosystem", "Planner and Tasks", "MICROSOFT_365_AND_COLLABORATION", ["TASK_PLAN_METADATA", "TASK_ASSIGNMENT_BOUNDARY"]),
    ("microsoft_power_platform_core_ecosystem", "Power Platform", "DEVELOPER_AND_APPLICATION_PLATFORM", ["POWER_APPS_METADATA", "POWER_AUTOMATE_METADATA", "DATAVERSE_METADATA"]),
    ("microsoft_security_defender_core_ecosystem", "Microsoft Security and Defender", "SECURITY_PRIVACY_AND_COMPLIANCE", ["DEFENDER_PRODUCT_METADATA", "SECURITY_ALERT_METADATA_BOUNDARY"]),
    ("microsoft_teams_core_ecosystem", "Microsoft Teams", "MICROSOFT_365_AND_COLLABORATION", ["TEAM_AND_CHANNEL_METADATA", "MEETING_AND_CHAT_METADATA"]),
]


def _product(row: tuple[str, str, str, list[str]]) -> dict[str, Any]:
    slug, name, domain, capabilities = row
    key = slug.removeprefix("microsoft_").removesuffix("_core_ecosystem").replace("_", "-").upper()
    return {
        "ecosystem_id": f"MICROSOFT-{key}-CORE-ECOSYSTEM",
        "name": name,
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "provider": "microsoft",
        "parent_id": "MICROSOFT-CORE-ECOSYSTEM",
        "core_module": f"backend/core/global_ecosystem/global_core_ecosystem/microsoft_core_ecosystem/{slug}",
        "domain_id": domain,
        "capabilities": list(capabilities),
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
    }


MICROSOFT_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "MICROSOFT-CORE-ECOSYSTEM",
    "name": "MICROSOFT CORE ECOSYSTEM",
    "provider": "microsoft",
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/microsoft_api_ecosystem",
    "capabilities": [
        "MICROSOFT_PROVIDER_REGISTRY", "MICROSOFT_365_CORE", "AZURE_CLOUD_CORE",
        "ENTRA_IDENTITY_CORE", "MICROSOFT_GRAPH_DISCOVERY", "PRODUCT_AND_DOMAIN_DISCOVERY",
        "TENANT_SCOPED_METADATA", "LEAST_PRIVILEGE_POLICY_BOUNDARY", "HEALTH_AND_READINESS_METADATA",
    ],
    "children": [_product(row) for row in _PRODUCT_ROWS],
    "live_connections_verified": 0,
    "api_calls_performed": 0,
}


def get_microsoft_core_catalog() -> dict[str, Any]:
    """Return an isolated copy so callers cannot mutate the canonical registry."""
    return deepcopy(MICROSOFT_CORE_ECOSYSTEM)


def list_microsoft_products(*, enabled_only: bool = False) -> list[dict[str, Any]]:
    """Return a detached Microsoft product-family inventory."""
    items = get_microsoft_core_catalog()["children"]
    return [item for item in items if not enabled_only or item.get("enabled", True)]


def microsoft_offerings_summary() -> dict[str, Any]:
    """Return product inventory with explicit non-connectivity metadata."""
    items = list_microsoft_products()
    return {
        "success": True,
        "count": len(items),
        "offerings": items,
        "live_connections_verified": 0,
        "api_calls_performed": 0,
    }


class MicrosoftCoreManager:
    """Stable public entry point for Microsoft Core metadata operations."""

    NAME = "MICROSOFT CORE ECOSYSTEM"
    ECOSYSTEM_ID = "MICROSOFT-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        # Lazy imports prevent a catalog/domain/orchestrator import cycle.
        from .orchestrator import MicrosoftCoreOrchestrator
        from .service import MicrosoftCoreEcosystemService

        self._orchestrator = MicrosoftCoreOrchestrator()
        self._service = MicrosoftCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(ecosystem_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def get_domain_manager(self, domain_id: str) -> Any:
        from .domain_runtime import MicrosoftCoreDomainManager
        return MicrosoftCoreDomainManager(domain_id)


def get_manager() -> MicrosoftCoreManager:
    """Create the canonical Microsoft Core manager."""
    return MicrosoftCoreManager()


__all__ = [
    "MICROSOFT_CORE_ECOSYSTEM",
    "MicrosoftCoreManager",
    "get_manager",
    "get_microsoft_core_catalog",
    "list_microsoft_products",
    "microsoft_offerings_summary",
]
