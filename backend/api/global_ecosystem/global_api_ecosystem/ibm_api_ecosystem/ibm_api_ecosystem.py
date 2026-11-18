"""Canonical IBM provider-owned API ecosystem metadata.

Catalog and readiness metadata only; this module does not call IBM APIs.
"""
from __future__ import annotations

IBM_API_ECOSYSTEM = {
    "provider_id": "ibm",
    "name": "IBM API ECOSYSTEM",
    "status": "CONFIGURATION_READINESS_SCAFFOLD",
    "live_connection_verified": False,
    "platforms": [
        "IBM Cloud", "watsonx.ai", "watsonx.data", "IBM Db2",
        "IBM Cloudant", "IBM Cloud Object Storage", "IBM VPC",
        "IBM Cloud Kubernetes Service", "Red Hat OpenShift on IBM Cloud",
        "IBM Code Engine", "IBM API Connect", "IBM Key Protect",
        "IBM Secrets Manager", "IBM Cloud Monitoring", "IBM Activity Tracker",
    ],
    "api_families": ["cloud_platform", "iam_identity", "watsonx_ai", "watsonx_data", "db2_database", "cloudant", "cloud_object_storage", "vpc_compute_networking", "kubernetes_containers", "code_engine_serverless", "api_connect_gateway", "security_key_protect", "secrets_manager", "monitoring_activity_tracker", "resource_controller_catalog", "billing_usage_cost"],
    "children": [
        {"id": "cloud_platform", "name": "IBM CLOUD PLATFORM API ECOSYSTEM", "folder": "ibm_cloud_platform_api_ecosystem", "status": "catalog_only"},
        {"id": "iam_identity", "name": "IBM IAM AND IDENTITY API ECOSYSTEM", "folder": "ibm_iam_identity_api_ecosystem", "status": "catalog_only"},
        {"id": "watsonx_ai", "name": "IBM WATSONX AI API ECOSYSTEM", "folder": "ibm_watsonx_ai_api_ecosystem", "status": "catalog_only"},
        {"id": "watsonx_data", "name": "IBM WATSONX DATA API ECOSYSTEM", "folder": "ibm_watsonx_data_api_ecosystem", "status": "catalog_only"},
        {"id": "db2_database", "name": "IBM DB2 DATABASE API ECOSYSTEM", "folder": "ibm_db2_database_api_ecosystem", "status": "catalog_only"},
        {"id": "cloudant", "name": "IBM CLOUDANT API ECOSYSTEM", "folder": "ibm_cloudant_api_ecosystem", "status": "catalog_only"},
        {"id": "cloud_object_storage", "name": "IBM CLOUD OBJECT STORAGE API ECOSYSTEM", "folder": "ibm_cloud_object_storage_api_ecosystem", "status": "catalog_only"},
        {"id": "vpc_compute_networking", "name": "IBM VPC COMPUTE AND NETWORKING API ECOSYSTEM", "folder": "ibm_vpc_compute_networking_api_ecosystem", "status": "catalog_only"},
        {"id": "kubernetes_containers", "name": "IBM KUBERNETES AND CONTAINERS API ECOSYSTEM", "folder": "ibm_kubernetes_containers_api_ecosystem", "status": "catalog_only"},
        {"id": "code_engine_serverless", "name": "IBM CODE ENGINE AND SERVERLESS API ECOSYSTEM", "folder": "ibm_code_engine_serverless_api_ecosystem", "status": "catalog_only"},
        {"id": "api_connect_gateway", "name": "IBM API CONNECT AND GATEWAY API ECOSYSTEM", "folder": "ibm_api_connect_gateway_api_ecosystem", "status": "catalog_only"},
        {"id": "security_key_protect", "name": "IBM SECURITY AND KEY PROTECT API ECOSYSTEM", "folder": "ibm_security_key_protect_api_ecosystem", "status": "catalog_only"},
        {"id": "secrets_manager", "name": "IBM SECRETS MANAGER API ECOSYSTEM", "folder": "ibm_secrets_manager_api_ecosystem", "status": "catalog_only"},
        {"id": "monitoring_activity_tracker", "name": "IBM MONITORING AND ACTIVITY TRACKER API ECOSYSTEM", "folder": "ibm_monitoring_activity_tracker_api_ecosystem", "status": "catalog_only"},
        {"id": "resource_controller_catalog", "name": "IBM RESOURCE CONTROLLER AND CATALOG API ECOSYSTEM", "folder": "ibm_resource_controller_catalog_api_ecosystem", "status": "catalog_only"},
        {"id": "billing_usage_cost", "name": "IBM BILLING USAGE AND COST API ECOSYSTEM", "folder": "ibm_billing_usage_cost_api_ecosystem", "status": "catalog_only"},
    ],
    "related_ecosystems": [
        "GLOBAL AI API ECOSYSTEM", "GLOBAL CLOUD API ECOSYSTEM",
        "GLOBAL DATABASE API ECOSYSTEM", "GLOBAL LANGUAGE API ECOSYSTEM",
        "GLOBAL BUSINESS API ECOSYSTEM", "GLOBAL SECURITY API ECOSYSTEM",
        "GLOBAL VPS API ECOSYSTEM", "GLOBAL HOSTING API ECOSYSTEM",
    ],
    "adapter_path": "backend/integrations/providers/ibm.py",
    "credential_source": "environment_or_managed_secret_store",
    "official_documentation": [
        "https://www.ibm.com/docs/",
        "https://cloud.ibm.com/apidocs",
    ],
}


def list_ibm_api_ecosystems() -> dict[str, object]:
    """List IBM API family catalogs; this does not assert live connectivity."""
    children = [dict(item) for item in IBM_API_ECOSYSTEM["children"]]
    return {
        "success": True,
        "provider": IBM_API_ECOSYSTEM["name"],
        "status": IBM_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }


__all__ = ["IBM_API_ECOSYSTEM", "list_ibm_api_ecosystems"]
