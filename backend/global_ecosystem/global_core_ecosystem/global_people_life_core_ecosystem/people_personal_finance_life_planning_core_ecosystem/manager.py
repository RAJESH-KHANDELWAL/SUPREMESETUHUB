"""Domain-scoped metadata manager for PERSONAL_FINANCE_AND_LIFE_PLANNING."""
from ..domain_runtime import PeopleLifeDomainManager

class PERSONAL_FINANCE_AND_LIFE_PLANNINGManager(PeopleLifeDomainManager):
    DOMAIN_ID = "PERSONAL_FINANCE_AND_LIFE_PLANNING"

def get_manager() -> PERSONAL_FINANCE_AND_LIFE_PLANNINGManager:
    return PERSONAL_FINANCE_AND_LIFE_PLANNINGManager()
