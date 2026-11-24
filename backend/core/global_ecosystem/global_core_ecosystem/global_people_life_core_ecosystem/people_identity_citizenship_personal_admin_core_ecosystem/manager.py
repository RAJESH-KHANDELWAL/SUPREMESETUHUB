"""Domain-scoped metadata manager for IDENTITY_CITIZENSHIP_AND_PERSONAL_ADMIN."""
from ..domain_runtime import PeopleLifeDomainManager

class IDENTITY_CITIZENSHIP_AND_PERSONAL_ADMINManager(PeopleLifeDomainManager):
    DOMAIN_ID = "IDENTITY_CITIZENSHIP_AND_PERSONAL_ADMIN"

def get_manager() -> IDENTITY_CITIZENSHIP_AND_PERSONAL_ADMINManager:
    return IDENTITY_CITIZENSHIP_AND_PERSONAL_ADMINManager()
