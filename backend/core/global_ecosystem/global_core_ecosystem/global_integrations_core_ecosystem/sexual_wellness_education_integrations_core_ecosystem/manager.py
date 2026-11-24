"""Manager for the SEXUAL_WELLNESS_EDUCATION integration domain."""
from ..domain_runtime import IntegrationDomainManager
class SexualWellnessEducationDomainManager(IntegrationDomainManager):
    DOMAIN_ID="SEXUAL_WELLNESS_EDUCATION"
def get_manager(): return SexualWellnessEducationDomainManager()
__all__=["SexualWellnessEducationDomainManager","get_manager"]
