"""Domain-scoped metadata manager for CAREER_EMPLOYMENT_AND_WORKFORCE."""
from ..domain_runtime import PeopleLifeDomainManager

class CAREER_EMPLOYMENT_AND_WORKFORCEManager(PeopleLifeDomainManager):
    DOMAIN_ID = "CAREER_EMPLOYMENT_AND_WORKFORCE"

def get_manager() -> CAREER_EMPLOYMENT_AND_WORKFORCEManager:
    return CAREER_EMPLOYMENT_AND_WORKFORCEManager()
