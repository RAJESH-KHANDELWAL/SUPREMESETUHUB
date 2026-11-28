"""Public interface for the OpenAI Core Ecosystem."""
from .catalog import (
    OPENAI_API_CAPABILITIES,
    OPENAI_CORE_ECOSYSTEM,
    get_openai_core_catalog,
    get_openai_core_module,
    list_openai_core_modules,
    validate_openai_core_catalog,
)
from .contracts import CoreResult, Readiness, SecretReference, TenantContext
from .domain_catalog import (
    DOMAIN_DEFINITIONS,
    list_openai_domain_inventory,
    openai_domain_summary,
    validate_openai_domain_catalog,
)
from .domain_runtime import OpenAICoreDomainManager
from .manager import OpenAICoreManager, get_manager
from .module_service import OpenAIProductCoreService
from .orchestrator import OpenAICoreOrchestrator
from .policy import OpenAICorePolicy, OpenAICorePolicyError
from .product_catalog import (
    list_openai_api_capabilities,
    list_openai_offerings,
    openai_offerings_summary,
)
from .service import OpenAICoreEcosystemService

__all__ = [
    "OPENAI_API_CAPABILITIES", "OPENAI_CORE_ECOSYSTEM",
    "get_openai_core_catalog", "get_openai_core_module", "list_openai_core_modules",
    "validate_openai_core_catalog", "CoreResult", "Readiness",
    "SecretReference", "TenantContext", "DOMAIN_DEFINITIONS",
    "list_openai_domain_inventory", "openai_domain_summary",
    "validate_openai_domain_catalog", "OpenAICoreDomainManager",
    "OpenAICoreManager", "get_manager", "OpenAIProductCoreService",
    "OpenAICoreOrchestrator", "OpenAICorePolicy", "OpenAICorePolicyError",
    "list_openai_api_capabilities", "list_openai_offerings",
    "openai_offerings_summary", "OpenAICoreEcosystemService",
]
