"""Domain taxonomy for Global Developer Core."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "DEVELOPER_PROVIDER_PLATFORMS": {"name": "Provider developer platforms", "purpose": "Provider-specific product and API metadata."},
    "DEVELOPER_API_AND_SDK": {"name": "APIs and SDKs", "purpose": "API products, SDKs, client libraries and developer documentation."},
    "AI_ML_AND_MODEL_DEVELOPMENT": {"name": "AI/ML and model development", "purpose": "Model APIs, training, inference and evaluation tooling."},
    "CLOUD_AND_INFRASTRUCTURE": {"name": "Cloud and infrastructure", "purpose": "Compute, networking, deployment and infrastructure automation."},
    "APPLICATION_AND_WEB_DEVELOPMENT": {"name": "Application and web development", "purpose": "Application frameworks, frontend, backend and web tooling."},
    "DATABASE_AND_DATA_ENGINEERING": {"name": "Database and data engineering", "purpose": "Databases, warehouses, streaming and data platforms."},
    "BLOCKCHAIN_AND_WEB3": {"name": "Blockchain and Web3", "purpose": "Smart contracts, nodes, wallets and Web3 developer infrastructure."},
    "IDENTITY_AND_ACCESS": {"name": "Identity and access", "purpose": "Authentication, authorization, identity federation and secrets boundaries."},
    "SECURITY_AND_COMPLIANCE": {"name": "Security and compliance", "purpose": "Secure SDLC, vulnerability management and compliance tooling."},
    "TESTING_AND_QUALITY": {"name": "Testing and quality", "purpose": "Automated tests, CI/CD quality and release validation."},
    "OBSERVABILITY_AND_OPERATIONS": {"name": "Observability and operations", "purpose": "Metrics, logs, traces, monitoring and incident metadata."},
    "NO_CODE_AND_AUTOMATION": {"name": "No-code and automation", "purpose": "Workflow builders, integration platforms and automation."},
    "PAYMENTS_AND_BILLING": {"name": "Payments and billing", "purpose": "Payment APIs, subscriptions, invoicing and billing."},
    "CONTENT_AND_TRUST_SAFETY": {"name": "Content and trust safety", "purpose": "Moderation, abuse controls and platform safety."},
    "AGE_ASSURANCE_AND_CONSENT": {"name": "Age assurance and consent", "purpose": "Age assurance, consent records and policy enforcement."},
    "CREATOR_AND_PLATFORM_ECONOMY": {"name": "Creator and platform economy", "purpose": "Creator tooling and platform monetization metadata."},
    "DATING_AND_RELATIONSHIP_PLATFORMS": {"name": "Dating and relationship platforms", "purpose": "Platform metadata with privacy, age and safety controls."},
    "SEXUAL_WELLNESS_EDUCATION": {"name": "Sexual wellness education", "purpose": "Educational resources and safe, consent-aware services."},
    "INDIA_DEVELOPER_ECOSYSTEM": {"name": "India developer ecosystem", "purpose": "India-specific developer platforms and regulatory references."},
}
def list_developer_domain_inventory() -> list[dict[str, Any]]:
    return [{"domain_id": key, **value} for key,value in DOMAIN_DEFINITIONS.items()]
def developer_domain_summary() -> dict[str, Any]:
    return {"success": True, "domain_count": len(DOMAIN_DEFINITIONS), "domains": list_developer_domain_inventory()}
__all__ = ["DOMAIN_DEFINITIONS","list_developer_domain_inventory","developer_domain_summary"]
