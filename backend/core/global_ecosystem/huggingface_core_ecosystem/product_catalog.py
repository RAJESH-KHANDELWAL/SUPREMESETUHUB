"""Curated Hugging Face product/API-family inventory; not a live integration claim."""
from __future__ import annotations
PRODUCTS = (
    {"product_id": "huggingface_authentication", "name": "Authentication and Token Governance", "core_module": "huggingface_authentication_core_ecosystem", "api_module": "huggingface_authentication_api_ecosystem", "capabilities": ["TOKEN_REFERENCE_METADATA","AUTHORIZATION_SCOPE_METADATA","ACCESS_BOUNDARY"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_billing", "name": "Billing and Pricing", "core_module": "huggingface_billing_core_ecosystem", "api_module": "huggingface_billing_api_ecosystem", "capabilities": ["PLAN_METADATA","PRICING_METADATA","BILLING_BOUNDARY"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_datasets", "name": "Datasets", "core_module": "huggingface_datasets_core_ecosystem", "api_module": "huggingface_datasets_api_ecosystem", "capabilities": ["DATASET_DISCOVERY","DATASET_METADATA","DATASET_REVISION_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_discussions", "name": "Discussions", "core_module": "huggingface_discussions_core_ecosystem", "api_module": "huggingface_discussions_api_ecosystem", "capabilities": ["DISCUSSION_METADATA","REPOSITORY_COMMUNITY_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_downloads", "name": "Downloads and Cache", "core_module": "huggingface_downloads_core_ecosystem", "api_module": "huggingface_downloads_api_ecosystem", "capabilities": ["DOWNLOAD_METADATA","CACHE_POLICY_METADATA","ARTIFACT_REFERENCE"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_evaluation", "name": "Evaluation", "core_module": "huggingface_evaluation_core_ecosystem", "api_module": "huggingface_evaluation_api_ecosystem", "capabilities": ["EVALUATION_METADATA","BENCHMARK_METADATA","RESULT_LINEAGE"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_hub", "name": "Hub and Repository Governance", "core_module": "huggingface_hub_core_ecosystem", "api_module": "huggingface_hub_api_ecosystem", "capabilities": ["HUB_REPOSITORY_METADATA","REVISION_METADATA","REPOSITORY_GOVERNANCE"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_inference", "name": "Inference Providers", "core_module": "huggingface_inference_core_ecosystem", "api_module": "huggingface_inference_api_ecosystem", "capabilities": ["INFERENCE_CAPABILITY_METADATA","TASK_COMPATIBILITY","MODEL_ROUTING_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_inference_endpoints", "name": "Inference Endpoints", "core_module": "huggingface_inference_endpoints_core_ecosystem", "api_module": "huggingface_inference_endpoints_api_ecosystem", "capabilities": ["ENDPOINT_CONFIGURATION_METADATA","DEPLOYMENT_READINESS","SCALING_POLICY_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_models", "name": "Models", "core_module": "huggingface_models_core_ecosystem", "api_module": "huggingface_models_api_ecosystem", "capabilities": ["MODEL_DISCOVERY","MODEL_CARD_METADATA","LICENSE_AND_TASK_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_organizations", "name": "Organizations and Teams", "core_module": "huggingface_organizations_core_ecosystem", "api_module": "huggingface_organizations_api_ecosystem", "capabilities": ["ORGANIZATION_METADATA","MEMBERSHIP_BOUNDARY","ROLE_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_spaces", "name": "Spaces and Applications", "core_module": "huggingface_spaces_core_ecosystem", "api_module": "huggingface_spaces_api_ecosystem", "capabilities": ["SPACE_METADATA","APPLICATION_RUNTIME_METADATA","HARDWARE_PROFILE_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_storage", "name": "Storage and Artifacts", "core_module": "huggingface_storage_core_ecosystem", "api_module": "huggingface_storage_api_ecosystem", "capabilities": ["STORAGE_QUOTA_METADATA","ARTIFACT_LIFECYCLE","RETENTION_POLICY_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_tasks", "name": "Tasks and Pipelines", "core_module": "huggingface_tasks_core_ecosystem", "api_module": "huggingface_tasks_api_ecosystem", "capabilities": ["TASK_TAXONOMY","PIPELINE_CONTRACT_METADATA","INPUT_OUTPUT_SCHEMA_METADATA"], "status": "CORE_CATALOG_ONLY"},
    {"product_id": "huggingface_webhooks", "name": "Webhooks and Events", "core_module": "huggingface_webhooks_core_ecosystem", "api_module": "huggingface_webhooks_api_ecosystem", "capabilities": ["WEBHOOK_REGISTRATION_METADATA","EVENT_SCHEMA_METADATA","DELIVERY_POLICY_METADATA"], "status": "CORE_CATALOG_ONLY"},
)
def list_products() -> list[dict]:
    return [dict(item, live_connection_verified=False, remote_operations_enabled=False) for item in PRODUCTS]
def get_product(product_id: str) -> dict | None:
    key = str(product_id).strip().lower()
    return next((item for item in list_products() if item["product_id"] == key), None)
def product_summary() -> dict:
    items = list_products()
    return {"product_count": len(items), "product_ids": [item["product_id"] for item in items]}
