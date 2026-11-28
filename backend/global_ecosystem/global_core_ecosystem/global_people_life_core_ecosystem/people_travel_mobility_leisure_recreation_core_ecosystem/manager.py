"""Domain-scoped metadata manager for TRAVEL_MOBILITY_LEISURE_AND_RECREATION."""
from ..domain_runtime import PeopleLifeDomainManager

class TRAVEL_MOBILITY_LEISURE_AND_RECREATIONManager(PeopleLifeDomainManager):
    DOMAIN_ID = "TRAVEL_MOBILITY_LEISURE_AND_RECREATION"

def get_manager() -> TRAVEL_MOBILITY_LEISURE_AND_RECREATIONManager:
    return TRAVEL_MOBILITY_LEISURE_AND_RECREATIONManager()
