"""Domain-scoped metadata manager for DIGITAL_LIFE_AND_GLOBAL_DIGITAL_SERVICES."""
from ..domain_runtime import PeopleLifeDomainManager

class DIGITAL_LIFE_AND_GLOBAL_DIGITAL_SERVICESManager(PeopleLifeDomainManager):
    DOMAIN_ID = "DIGITAL_LIFE_AND_GLOBAL_DIGITAL_SERVICES"

def get_manager() -> DIGITAL_LIFE_AND_GLOBAL_DIGITAL_SERVICESManager:
    return DIGITAL_LIFE_AND_GLOBAL_DIGITAL_SERVICESManager()
