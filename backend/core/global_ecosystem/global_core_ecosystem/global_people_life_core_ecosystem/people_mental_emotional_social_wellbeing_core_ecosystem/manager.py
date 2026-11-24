"""Domain-scoped metadata manager for MENTAL_EMOTIONAL_AND_SOCIAL_WELLBEING."""
from ..domain_runtime import PeopleLifeDomainManager

class MENTAL_EMOTIONAL_AND_SOCIAL_WELLBEINGManager(PeopleLifeDomainManager):
    DOMAIN_ID = "MENTAL_EMOTIONAL_AND_SOCIAL_WELLBEING"

def get_manager() -> MENTAL_EMOTIONAL_AND_SOCIAL_WELLBEINGManager:
    return MENTAL_EMOTIONAL_AND_SOCIAL_WELLBEINGManager()
