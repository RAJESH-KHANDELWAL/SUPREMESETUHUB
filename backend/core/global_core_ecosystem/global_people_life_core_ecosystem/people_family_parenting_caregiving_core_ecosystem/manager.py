"""Domain-scoped metadata manager for FAMILY_PARENTING_AND_CAREGIVING."""
from ..domain_runtime import PeopleLifeDomainManager

class FAMILY_PARENTING_AND_CAREGIVINGManager(PeopleLifeDomainManager):
    DOMAIN_ID = "FAMILY_PARENTING_AND_CAREGIVING"

def get_manager() -> FAMILY_PARENTING_AND_CAREGIVINGManager:
    return FAMILY_PARENTING_AND_CAREGIVINGManager()
