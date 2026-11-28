"""Domain-scoped metadata manager for EDUCATION_LEARNING_AND_SKILLS."""
from ..domain_runtime import PeopleLifeDomainManager

class EDUCATION_LEARNING_AND_SKILLSManager(PeopleLifeDomainManager):
    DOMAIN_ID = "EDUCATION_LEARNING_AND_SKILLS"

def get_manager() -> EDUCATION_LEARNING_AND_SKILLSManager:
    return EDUCATION_LEARNING_AND_SKILLSManager()
