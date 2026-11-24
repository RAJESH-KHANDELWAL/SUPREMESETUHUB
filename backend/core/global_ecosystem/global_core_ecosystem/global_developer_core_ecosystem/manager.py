"""Canonical manager and catalog for the Global Developer Core Ecosystem."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

GLOBAL_DEVELOPER_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
    "name": "GLOBAL DEVELOPER CORE ECOSYSTEM",
    "provider": "global",
    "ecosystem_type": "GLOBAL_DOMAIN_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "api_catalog_ref": None,
    "capabilities": [
        "DEVELOPER_PLATFORM_REGISTRY", "DEVELOPER_PRODUCT_SERVICE_DISCOVERY",
        "SDK_AND_API_CAPABILITY_METADATA", "DEVELOPER_TOOLCHAIN_CLASSIFICATION",
        "SECURITY_AND_COMPLIANCE_POLICY_METADATA", "TENANT_SCOPED_CONNECTION_METADATA",
        "CREDENTIAL_BOUNDARY_AND_SECRET_REFERENCE", "DEPENDENCY_AND_LIFECYCLE_METADATA"
    ],
    "children": [
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-ADULT-CREATOR-BUSINESS-CORE-ECOSYSTEM",
        "name": "ADULT CREATOR BUSINESS CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/adult_creator_business_core_ecosystem",
        "domain_id": "CREATOR_AND_PLATFORM_ECONOMY",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Creator business models, monetization and platform governance.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-ADULT-PLATFORM-DISCOVERY-CORE-ECOSYSTEM",
        "name": "ADULT PLATFORM DISCOVERY CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/adult_platform_discovery_core_ecosystem",
        "domain_id": "CONTENT_AND_TRUST_SAFETY",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Age-appropriate discovery metadata for adult-oriented platforms; no explicit content processing.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-AGE-VERIFICATION-CONSENT-CORE-ECOSYSTEM",
        "name": "AGE VERIFICATION AND CONSENT CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/age_verification_consent_core_ecosystem",
        "domain_id": "AGE_ASSURANCE_AND_CONSENT",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Age assurance, consent evidence and jurisdiction-aware policy boundaries.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-AI-ML-DATA-CORE-ECOSYSTEM",
        "name": "AI ML AND DATA CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/ai_ml_data_core_ecosystem",
        "domain_id": "AI_ML_AND_MODEL_DEVELOPMENT",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "AI/ML developer platforms, model lifecycle and data tooling.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-ANTHROPIC-DEVELOPER-CORE-ECOSYSTEM",
        "name": "ANTHROPIC DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/anthropic_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Anthropic developer products and API capability metadata.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-APPLE-DEVELOPER-CORE-ECOSYSTEM",
        "name": "APPLE DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/apple_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Apple developer ecosystem, app distribution and platform services.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-ATLASSIAN-DEVELOPER-CORE-ECOSYSTEM",
        "name": "ATLASSIAN DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/atlassian_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Atlassian developer tools, collaboration and extensibility.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-AWS-DEVELOPER-CORE-ECOSYSTEM",
        "name": "AWS DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/aws_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "AWS developer services, SDKs and cloud development.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-BLOCKCHAIN-WEB3-CORE-ECOSYSTEM",
        "name": "BLOCKCHAIN WEB3 CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/blockchain_web3_core_ecosystem",
        "domain_id": "BLOCKCHAIN_AND_WEB3",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Blockchain, Web3 developer infrastructure and smart-contract tooling.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-COHERE-DEVELOPER-CORE-ECOSYSTEM",
        "name": "COHERE DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/cohere_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Cohere developer products and AI platform metadata.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-CONTENT-MODERATION-SAFETY-CORE-ECOSYSTEM",
        "name": "CONTENT MODERATION AND SAFETY CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/content_moderation_safety_core_ecosystem",
        "domain_id": "CONTENT_AND_TRUST_SAFETY",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Content moderation, abuse prevention and developer safety controls.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-DATABASE-STORAGE-CORE-ECOSYSTEM",
        "name": "DATABASE AND STORAGE CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/database_storage_core_ecosystem",
        "domain_id": "DATABASE_AND_DATA_ENGINEERING",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Database engines, data platforms, storage and data access tooling.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-DATING-RELATIONSHIPS-CORE-ECOSYSTEM",
        "name": "DATING AND RELATIONSHIPS CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/dating_relationships_core_ecosystem",
        "domain_id": "DATING_AND_RELATIONSHIP_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Relationship and dating platform integration metadata with safety boundaries.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-DEEPSEEK-DEVELOPER-CORE-ECOSYSTEM",
        "name": "DEEPSEEK DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/deepseek_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "DeepSeek developer products and AI platform metadata.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-DEVELOPER-SECURITY-COMPLIANCE-CORE-ECOSYSTEM",
        "name": "DEVELOPER SECURITY AND COMPLIANCE CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/developer_security_compliance_core_ecosystem",
        "domain_id": "SECURITY_AND_COMPLIANCE",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Secure development, vulnerability management, compliance and software supply chain.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-GITHUB-DEVELOPER-CORE-ECOSYSTEM",
        "name": "GITHUB DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/github_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS",
            "REPOSITORY_WRITE"
        ],
        "purpose": "GitHub repositories, actions, apps and developer workflow metadata.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-GLOBAL-CLOUD-INFRASTRUCTURE-CORE-ECOSYSTEM",
        "name": "GLOBAL CLOUD INFRASTRUCTURE CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/global_cloud_infrastructure_core_ecosystem",
        "domain_id": "CLOUD_AND_INFRASTRUCTURE",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Cloud infrastructure providers, deployment and infrastructure-as-code.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-GOOGLE-DEVELOPER-CORE-ECOSYSTEM",
        "name": "GOOGLE DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/google_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Google developer products, APIs and developer tooling.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-HUGGINGFACE-DEVELOPER-CORE-ECOSYSTEM",
        "name": "HUGGING FACE DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/huggingface_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Model hubs, datasets, inference and ML developer tooling.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-IDENTITY-AUTHENTICATION-CORE-ECOSYSTEM",
        "name": "IDENTITY AND AUTHENTICATION CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/identity_authentication_core_ecosystem",
        "domain_id": "IDENTITY_AND_ACCESS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Developer identity, OAuth/OIDC, authentication and authorization metadata.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-INDIA-DEVELOPER-PLATFORM-CORE-ECOSYSTEM",
        "name": "INDIA DEVELOPER PLATFORMS CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/india_developer_platform_core_ecosystem",
        "domain_id": "INDIA_DEVELOPER_ECOSYSTEM",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "India-focused developer platforms, digital public infrastructure and compliance references.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-MICROSOFT-DEVELOPER-CORE-ECOSYSTEM",
        "name": "MICROSOFT DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/microsoft_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Microsoft developer products, Azure and software development tooling.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-MISTRAL-DEVELOPER-CORE-ECOSYSTEM",
        "name": "MISTRAL DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/mistral_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Mistral developer products and AI platform metadata.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-NO-CODE-AUTOMATION-CORE-ECOSYSTEM",
        "name": "NO CODE AND AUTOMATION CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/no_code_automation_core_ecosystem",
        "domain_id": "NO_CODE_AND_AUTOMATION",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "No-code, low-code, workflow automation and integration builders.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-NVIDIA-DEVELOPER-CORE-ECOSYSTEM",
        "name": "NVIDIA DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/nvidia_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "NVIDIA developer platforms, GPU software and AI compute tooling.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-OPENAI-DEVELOPER-CORE-ECOSYSTEM",
        "name": "OPENAI DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/openai_developer_core_ecosystem",
        "domain_id": "DEVELOPER_PROVIDER_PLATFORMS",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "OpenAI developer platform, API product and model capability metadata.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-PAYMENTS-BILLING-CORE-ECOSYSTEM",
        "name": "PAYMENTS AND BILLING CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/payments_billing_core_ecosystem",
        "domain_id": "PAYMENTS_AND_BILLING",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Developer payment gateways, billing APIs and subscription infrastructure.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-SEXUAL-WELLNESS-EDUCATION-CORE-ECOSYSTEM",
        "name": "SEXUAL WELLNESS EDUCATION CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/sexual_wellness_education_core_ecosystem",
        "domain_id": "SEXUAL_WELLNESS_EDUCATION",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Educational and wellness developer resources with age, consent and safety boundaries.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-TESTING-OBSERVABILITY-CORE-ECOSYSTEM",
        "name": "TESTING AND OBSERVABILITY CORE ECOSYSTEM",
        "ecosystem_type": "DEVELOPER_DOMAIN_CORE",
        "parent_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/testing_observability_core_ecosystem",
        "domain_id": "TESTING_AND_QUALITY",
        "capabilities": [
            "DISCOVERY_METADATA",
            "CAPABILITY_CLASSIFICATION",
            "LIFECYCLE_STATUS"
        ],
        "purpose": "Testing, CI/CD quality, monitoring, tracing and developer observability.",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False
    }
]
}

def get_global_developer_core_catalog() -> dict[str, Any]:
    """Return an isolated copy of the canonical catalog."""
    return deepcopy(GLOBAL_DEVELOPER_CORE_ECOSYSTEM)

__all__ = ["GLOBAL_DEVELOPER_CORE_ECOSYSTEM", "get_global_developer_core_catalog"]

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .domain_runtime import DeveloperCoreDomainManager


class GlobalDeveloperCoreManager:
    NAME = "GLOBAL DEVELOPER CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-DEVELOPER-CORE-ECOSYSTEM"

    def __init__(self):
        # Lazy imports keep the catalog in this manager without circular imports.
        from .orchestrator import DeveloperCoreOrchestrator
        from .service import DeveloperCoreEcosystemService
        self._orchestrator = DeveloperCoreOrchestrator()
        self._service = DeveloperCoreEcosystemService()

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

    def get_domain_manager(self, domain_id: str) -> "DeveloperCoreDomainManager":
        from .domain_runtime import DeveloperCoreDomainManager
        return DeveloperCoreDomainManager(domain_id)


_manager: GlobalDeveloperCoreManager | None = None


def get_manager() -> GlobalDeveloperCoreManager:
    global _manager
    if _manager is None:
        _manager = GlobalDeveloperCoreManager()
    return _manager


__all__ = [
    "GLOBAL_DEVELOPER_CORE_ECOSYSTEM",
    "get_global_developer_core_catalog",
    "GlobalDeveloperCoreManager",
    "get_manager",
]
