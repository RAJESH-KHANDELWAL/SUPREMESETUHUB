"""Public interface for the Global People Life CORE control plane."""
from .catalog import PEOPLE_LIFE_CORE_ECOSYSTEM, SERVICE_TIERS, get_catalog, get_people_life_core_catalog, list_people_life_core_modules
from .contracts import CoreResult, PeopleLifeDomain, Readiness, SecretReference, TenantContext
from .domain_catalog import DOMAIN_DEFINITIONS, get_people_life_domain, list_people_life_domains, list_people_life_modules, people_life_domain_summary
from .domain_runtime import PeopleLifeDomainManager
from .manager import PeopleLifeCoreManager, get_manager
from .module_service import PeopleLifeDomainCoreService
from .orchestrator import PeopleLifeCoreOrchestrator
from .policy import PeopleLifePolicyError, adult_content_policy
from .service import PeopleLifeCoreEcosystemService

__all__ = [
    "PEOPLE_LIFE_CORE_ECOSYSTEM", "SERVICE_TIERS", "get_catalog",
    "get_people_life_core_catalog", "list_people_life_core_modules",
    "CoreResult", "PeopleLifeDomain", "Readiness", "SecretReference", "TenantContext",
    "DOMAIN_DEFINITIONS", "get_people_life_domain", "list_people_life_domains",
    "list_people_life_modules", "people_life_domain_summary", "PeopleLifeDomainManager",
    "PeopleLifeCoreManager", "get_manager", "PeopleLifeDomainCoreService",
    "PeopleLifeCoreOrchestrator", "PeopleLifePolicyError", "adult_content_policy",
    "PeopleLifeCoreEcosystemService",
]
