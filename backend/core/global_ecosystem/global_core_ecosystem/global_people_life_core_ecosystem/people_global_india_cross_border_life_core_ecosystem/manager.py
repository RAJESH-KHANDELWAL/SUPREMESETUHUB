"""Domain-scoped metadata manager for GLOBAL_INDIA_AND_CROSS_BORDER_PEOPLE_LIFE."""
from ..domain_runtime import PeopleLifeDomainManager

class GLOBAL_INDIA_AND_CROSS_BORDER_PEOPLE_LIFEManager(PeopleLifeDomainManager):
    DOMAIN_ID = "GLOBAL_INDIA_AND_CROSS_BORDER_PEOPLE_LIFE"

def get_manager() -> GLOBAL_INDIA_AND_CROSS_BORDER_PEOPLE_LIFEManager:
    return GLOBAL_INDIA_AND_CROSS_BORDER_PEOPLE_LIFEManager()
