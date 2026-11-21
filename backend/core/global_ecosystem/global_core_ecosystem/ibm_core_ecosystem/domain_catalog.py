"""IBM Core domain taxonomy, grouped by responsibility rather than folder count."""
from __future__ import annotations
from typing import Any
DOMAIN_DEFINITIONS = {
    "PROVIDER_GOVERNANCE": {"name": "Provider Governance", "purpose": "IBM provider identity, service registration, lifecycle, readiness and cross-layer ownership."},
    "CLOUD_ACCOUNT_RESOURCE_GOVERNANCE": {"name": "Cloud Account and Resource Governance", "purpose": "Accounts, resource groups, projects, regions, service instances and resource ownership."},
    "IAM_IDENTITY_ACCESS": {"name": "IAM, Identity and Access", "purpose": "IAM identities, service IDs, access groups, trusted profiles, policies and authorization boundaries."},
    "COMPUTE_VPC_NETWORKING": {"name": "Compute, VPC and Networking", "purpose": "Virtual servers, images, volumes, VPCs, subnets, gateways, security groups and network interfaces."},
    "KUBERNETES_CONTAINERS": {"name": "Kubernetes, OpenShift and Containers", "purpose": "IBM Cloud Kubernetes Service, OpenShift, container workloads and registry boundaries."},
    "SERVERLESS_CODE_ENGINE": {"name": "Serverless and Code Engine", "purpose": "Code Engine projects, applications, jobs, builds and serverless workload metadata."},
    "OBJECT_STORAGE_ARTIFACTS": {"name": "Object Storage and Artifacts", "purpose": "Buckets, objects, multipart uploads, lifecycle, retention and artifact references."},
    "DATABASES_CLOUDANT": {"name": "Databases and Cloudant", "purpose": "Db2, Cloudant, database instances, documents, indexes, schemas and data lifecycle."},
    "WATSONX_AI_MODELS_INFERENCE": {"name": "watsonx AI, Models and Inference", "purpose": "Foundation models, model metadata, deployments, inference and AI lifecycle governance."},
    "WATSONX_DATA_ANALYTICS": {"name": "watsonx.data and Analytics", "purpose": "Data platform, engines, catalogs, analytics and governed data access."},
    "API_MANAGEMENT_GATEWAY": {"name": "API Management and Gateway", "purpose": "API Connect catalogs, spaces, products, APIs, gateway configuration and lifecycle."},
    "SECRETS_MANAGEMENT": {"name": "Secrets Management", "purpose": "Secret references, secret groups, rotation metadata, retrieval boundaries and access policy."},
    "KEY_MANAGEMENT_CRYPTOGRAPHY": {"name": "Key Management and Cryptography", "purpose": "Key Protect key lifecycle, cryptographic policy and key access boundaries."},
    "MONITORING_OBSERVABILITY": {"name": "Monitoring and Observability", "purpose": "Metrics, dashboards, alerts, service health and operational telemetry metadata."},
    "ACTIVITY_TRACKING_AUDIT": {"name": "Activity Tracking and Audit", "purpose": "Activity Tracker events, audit lineage, actor attribution and evidence metadata."},
    "RESOURCE_CATALOG_LIFECYCLE": {"name": "Resource Catalog and Service Lifecycle", "purpose": "Global Catalog, service plans, resource bindings, provisioning eligibility and lifecycle."},
    "BILLING_USAGE_COST": {"name": "Billing, Usage and Cost", "purpose": "Usage records, billing reports, consumption, budgets and cost governance."},
    "TENANCY_REGION_QUOTA_COMPLIANCE": {"name": "Tenancy, Region, Quota and Compliance", "purpose": "Tenant isolation, region eligibility, quota metadata, compliance and data residency."},
}
def list_domains() -> list[dict[str, Any]]:
    return [{"domain_id": key, **value} for key,value in DOMAIN_DEFINITIONS.items()]
def get_domain(domain_id: str) -> dict[str, Any] | None:
    key=str(domain_id).strip().upper()
    return next((x for x in list_domains() if x["domain_id"] == key),None)
def domain_summary() -> dict[str, Any]:
    items=list_domains()
    return {"domain_count":len(items),"domain_ids":[x["domain_id"] for x in items]}
