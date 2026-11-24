"""Domain-scoped metadata manager for AGEING_RETIREMENT_AND_LIFE_TRANSITIONS."""
from ..domain_runtime import PeopleLifeDomainManager

class AGEING_RETIREMENT_AND_LIFE_TRANSITIONSManager(PeopleLifeDomainManager):
    DOMAIN_ID = "AGEING_RETIREMENT_AND_LIFE_TRANSITIONS"

def get_manager() -> AGEING_RETIREMENT_AND_LIFE_TRANSITIONSManager:
    return AGEING_RETIREMENT_AND_LIFE_TRANSITIONSManager()
