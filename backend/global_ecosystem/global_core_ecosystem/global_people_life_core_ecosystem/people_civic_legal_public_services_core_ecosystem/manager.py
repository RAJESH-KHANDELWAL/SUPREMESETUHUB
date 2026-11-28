"""Domain-scoped metadata manager for CIVIC_LEGAL_AND_PUBLIC_SERVICES."""
from ..domain_runtime import PeopleLifeDomainManager

class CIVIC_LEGAL_AND_PUBLIC_SERVICESManager(PeopleLifeDomainManager):
    DOMAIN_ID = "CIVIC_LEGAL_AND_PUBLIC_SERVICES"

def get_manager() -> CIVIC_LEGAL_AND_PUBLIC_SERVICESManager:
    return CIVIC_LEGAL_AND_PUBLIC_SERVICESManager()
