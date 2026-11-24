"""AWS Core domain taxonomy and service-family coverage."""
from __future__ import annotations
from typing import Any
from .product_catalog import list_aws_offerings

DOMAINS = [
    {
        "domain_id": "APPLICATION_INTEGRATION_AND_API_MANAGEMENT",
        "name": "Application Integration and API Management",
        "description": "API endpoints, gateways, metrics and application integration control-plane metadata"
    },
    {
        "domain_id": "AI_ML_AND_INTELLIGENCE",
        "name": "AI, Machine Learning and Intelligence",
        "description": "Foundation-model, managed AI platform and model deployment metadata"
    },
    {
        "domain_id": "BILLING_COST_AND_GOVERNANCE",
        "name": "Billing, Cost and Governance",
        "description": "Billing accounts, budgets, cost allocation and usage reporting metadata"
    },
    {
        "domain_id": "COMPUTE_AND_CONTAINERS",
        "name": "Compute and Containers",
        "description": "Virtual machines, serverless functions, container orchestration and managed compute"
    },
    {
        "domain_id": "DATABASE_AND_DATA_SERVICES",
        "name": "Database and Data Services",
        "description": "Relational, clustered and NoSQL database control-plane metadata"
    },
    {
        "domain_id": "DOMAIN_AND_NAME_SERVICES",
        "name": "Domain and Name Services",
        "description": "Hosted zones, DNS records, health checks and domain operations"
    },
    {
        "domain_id": "INFRASTRUCTURE_PROVISIONING_AND_AUTOMATION",
        "name": "Infrastructure Provisioning and Automation",
        "description": "Infrastructure templates, stacks, change sets and provisioning lifecycle metadata"
    },
    {
        "domain_id": "NETWORKING_AND_EDGE",
        "name": "Networking and Edge",
        "description": "Virtual networks, routing, gateways, DNS and API edge configuration"
    },
    {
        "domain_id": "OBSERVABILITY_AND_AUDIT",
        "name": "Observability and Audit",
        "description": "Metrics, alarms, logs, dashboards, audit trails and event history"
    },
    {
        "domain_id": "ORGANIZATION_AND_GOVERNANCE",
        "name": "Organization and Governance",
        "description": "AWS account context, organization-wide policy and governance references"
    },
    {
        "domain_id": "SECURITY_AND_IDENTITY",
        "name": "Security and Identity",
        "description": "IAM identities, roles, policies, keys, secrets and resource access boundaries"
    },
    {
        "domain_id": "STORAGE_AND_DATA_MANAGEMENT",
        "name": "Storage and Data Management",
        "description": "Object storage, database backups, encryption and data lifecycle policies"
    },
    {
        "domain_id": "DEVELOPER_AND_APPLICATION_PLATFORM",
        "name": "Developer and Application Platform",
        "description": "Application delivery, model lifecycle and developer-facing AWS services"
    }
]

def list_aws_domain_inventory() -> list[dict[str, Any]]:
    offerings = list_aws_offerings()
    return [{**domain, "offering_count": sum(1 for item in offerings if domain["domain_id"] in item["domains"]), "families": [item["id"] for item in offerings if domain["domain_id"] in item["domains"]]} for domain in DOMAINS]

def aws_domain_summary() -> dict[str, Any]:
    inventory = list_aws_domain_inventory()
    return {"success": True, "domain_count": len(inventory), "offering_count": len(list_aws_offerings()), "live_connections_verified": 0, "domains": inventory}
