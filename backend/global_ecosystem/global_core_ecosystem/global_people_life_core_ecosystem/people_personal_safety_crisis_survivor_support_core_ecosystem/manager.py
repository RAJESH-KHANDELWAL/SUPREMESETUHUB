"""Domain-scoped metadata manager for PERSONAL_SAFETY_CRISIS_AND_SURVIVOR_SUPPORT."""
from ..domain_runtime import PeopleLifeDomainManager

class PERSONAL_SAFETY_CRISIS_AND_SURVIVOR_SUPPORTManager(PeopleLifeDomainManager):
    DOMAIN_ID = "PERSONAL_SAFETY_CRISIS_AND_SURVIVOR_SUPPORT"

def get_manager() -> PERSONAL_SAFETY_CRISIS_AND_SURVIVOR_SUPPORTManager:
    return PERSONAL_SAFETY_CRISIS_AND_SURVIVOR_SUPPORTManager()
