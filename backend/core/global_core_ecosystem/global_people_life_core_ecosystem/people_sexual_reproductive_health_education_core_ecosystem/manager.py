"""Domain-scoped metadata manager for SEXUAL_REPRODUCTIVE_HEALTH_AND_EDUCATION."""
from ..domain_runtime import PeopleLifeDomainManager

class SEXUAL_REPRODUCTIVE_HEALTH_AND_EDUCATIONManager(PeopleLifeDomainManager):
    DOMAIN_ID = "SEXUAL_REPRODUCTIVE_HEALTH_AND_EDUCATION"

def get_manager() -> SEXUAL_REPRODUCTIVE_HEALTH_AND_EDUCATIONManager:
    return SEXUAL_REPRODUCTIVE_HEALTH_AND_EDUCATIONManager()
