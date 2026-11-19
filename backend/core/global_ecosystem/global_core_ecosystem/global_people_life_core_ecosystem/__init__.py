"""Public interface for the Global People Life CORE control plane."""
from .catalog import PEOPLE_LIFE_CORE_ECOSYSTEM,get_catalog,get_people_life_core_catalog,list_people_life_core_modules
from .contracts import CoreResult,PeopleLifeDomain,Readiness,SecretReference,TenantContext
from .domain_catalog import DOMAIN_DEFINITIONS,get_people_life_domain,list_people_life_domains,people_life_domain_summary
from .module_service import PeopleLifeDomainCoreService
from .orchestrator import PeopleLifeCoreOrchestrator
from .policy import PeopleLifePolicyError,adult_content_policy
from .service import PeopleLifeCoreEcosystemService

__all__=["PEOPLE_LIFE_CORE_ECOSYSTEM","get_catalog","get_people_life_core_catalog","list_people_life_core_modules","CoreResult","PeopleLifeDomain","Readiness","SecretReference","TenantContext","DOMAIN_DEFINITIONS","get_people_life_domain","list_people_life_domains","people_life_domain_summary","PeopleLifeDomainCoreService","PeopleLifeCoreOrchestrator","PeopleLifePolicyError","adult_content_policy","PeopleLifeCoreEcosystemService"]
