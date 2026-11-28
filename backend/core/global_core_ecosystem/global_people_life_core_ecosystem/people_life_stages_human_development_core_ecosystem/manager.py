"""Domain-scoped metadata manager for LIFE_STAGES_AND_HUMAN_DEVELOPMENT."""
from ..domain_runtime import PeopleLifeDomainManager

class LIFE_STAGES_AND_HUMAN_DEVELOPMENTManager(PeopleLifeDomainManager):
    DOMAIN_ID = "LIFE_STAGES_AND_HUMAN_DEVELOPMENT"

def get_manager() -> LIFE_STAGES_AND_HUMAN_DEVELOPMENTManager:
    return LIFE_STAGES_AND_HUMAN_DEVELOPMENTManager()
