"""Domain-scoped metadata manager for HOME_HOUSEHOLD_AND_DAILY_LIVING."""
from ..domain_runtime import PeopleLifeDomainManager

class HOME_HOUSEHOLD_AND_DAILY_LIVINGManager(PeopleLifeDomainManager):
    DOMAIN_ID = "HOME_HOUSEHOLD_AND_DAILY_LIVING"

def get_manager() -> HOME_HOUSEHOLD_AND_DAILY_LIVINGManager:
    return HOME_HOUSEHOLD_AND_DAILY_LIVINGManager()
