"""IBM Core domain taxonomy with explicit product-family coverage."""
from __future__ import annotations
from typing import Any
DOMAIN_DEFINITIONS = {
    "PROVIDER_GOVERNANCE": {"name": "Provider Governance", "purpose": "IBM provider identity, service registration, lifecycle, readiness and cross-layer ownership.", "product_ids": ["ibm_cloud_platform","ibm_resource_controller_catalog"]},
    "CLOUD_ACCOUNT_RESOURCE_GOVERNANCE": {"name": "Cloud Account and Resource Governance", "purpose": "Accounts, resource groups, projects, regions, service instances and resource ownership.", "product_ids": ["ibm_cloud_platform","ibm_resource_controller_catalog","ibm_billing_usage_cost"]},
    "IAM_IDENTITY_ACCESS": {"name": "IAM, Identity and Access", "purpose": "IAM identities, service IDs, access groups, trusted profiles, policies and authorization boundaries.", "product_ids": ["ibm_iam_identity","ibm_secrets_manager","ibm_security_key_protect"]},
    "COMPUTE_VPC_NETWORKING": {"name": "Compute, VPC and Networking", "purpose": "Virtual servers, images, volumes, VPCs, subnets, gateways, security groups and network interfaces.", "product_ids": ["ibm_vpc_compute_networking"]},
    "KUBERNETES_CONTAINERS": {"name": "Kubernetes, OpenShift and Containers", "purpose": "IBM Cloud Kubernetes Service, OpenShift, container workloads and registry boundaries.", "product_ids": ["ibm_kubernetes_containers"]},
    "SERVERLESS_CODE_ENGINE": {"name": "Serverless and Code Engine", "purpose": "Code Engine projects, applications, jobs, builds and serverless workload metadata.", "product_ids": ["ibm_code_engine_serverless"]},
    "OBJECT_STORAGE_ARTIFACTS": {"name": "Object Storage and Artifacts", "purpose": "Buckets, objects, multipart uploads, lifecycle, retention and artifact references.", "product_ids": ["ibm_cloud_object_storage"]},
    "DATABASES_CLOUDANT": {"name": "Databases and Cloudant", "purpose": "Db2, Cloudant, database instances, documents, indexes, schemas and data lifecycle.", "product_ids": ["ibm_db2_database","ibm_cloudant","ibm_watsonx_data"]},
    "WATSONX_AI_MODELS_INFERENCE": {"name": "watsonx AI, Models and Inference", "purpose": "Foundation models, model metadata, deployments, inference and AI lifecycle governance.", "product_ids": ["ibm_watsonx_ai"]},
    "WATSONX_DATA_ANALYTICS": {"name": "watsonx.data and Analytics", "purpose": "Data platform, engines, catalogs, analytics and governed data access.", "product_ids": ["ibm_watsonx_data","ibm_db2_database","ibm_cloudant"]},
    "API_MANAGEMENT_GATEWAY": {"name": "API Management and Gateway", "purpose": "API Connect catalogs, spaces, products, APIs, gateway configuration and lifecycle.", "product_ids": ["ibm_api_connect_gateway"]},
    "SECRETS_MANAGEMENT": {"name": "Secrets Management", "purpose": "Secret references, secret groups, rotation metadata, retrieval boundaries and access policy.", "product_ids": ["ibm_secrets_manager"]},
    "KEY_MANAGEMENT_CRYPTOGRAPHY": {"name": "Key Management and Cryptography", "purpose": "Key Protect key lifecycle, cryptographic policy and key access boundaries.", "product_ids": ["ibm_security_key_protect"]},
    "MONITORING_OBSERVABILITY": {"name": "Monitoring and Observability", "purpose": "Metrics, dashboards, alerts, service health and operational telemetry metadata.", "product_ids": ["ibm_monitoring_activity_tracker"]},
    "ACTIVITY_TRACKING_AUDIT": {"name": "Activity Tracking and Audit", "purpose": "Activity Tracker events, audit lineage, actor attribution and evidence metadata.", "product_ids": ["ibm_monitoring_activity_tracker","ibm_iam_identity"]},
    "RESOURCE_CATALOG_LIFECYCLE": {"name": "Resource Catalog and Service Lifecycle", "purpose": "Global Catalog, service plans, resource bindings, provisioning eligibility and lifecycle.", "product_ids": ["ibm_resource_controller_catalog","ibm_cloud_platform"]},
    "BILLING_USAGE_COST": {"name": "Billing, Usage and Cost", "purpose": "Usage records, billing reports, consumption, budgets and cost governance.", "product_ids": ["ibm_billing_usage_cost"]},
    "TENANCY_REGION_QUOTA_COMPLIANCE": {"name": "Tenancy, Region, Quota and Compliance", "purpose": "Tenant isolation, region eligibility, quota metadata, compliance and data residency.", "product_ids": ["ibm_cloud_platform","ibm_iam_identity","ibm_vpc_compute_networking"]},
}
def list_domains() -> list[dict[str, Any]]:
    return [{"domain_id":key,**value} for key,value in DOMAIN_DEFINITIONS.items()]
def get_domain(domain_id: str) -> dict[str, Any] | None:
    key=str(domain_id).strip().upper()
    return next((item for item in list_domains() if item["domain_id"]==key),None)
def domain_summary() -> dict[str, Any]:
    items=list_domains()
    return {"domain_count":len(items),"domain_ids":[x["domain_id"] for x in items],"mapped_product_count":len({p for d in items for p in d["product_ids"]})}
