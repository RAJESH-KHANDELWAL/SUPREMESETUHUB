"""Manager for the AI_ML_DATA integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AiMlDataDomainManager(IntegrationDomainManager):
    DOMAIN_ID="AI_ML_DATA"
def get_manager(): return AiMlDataDomainManager()
__all__=["AiMlDataDomainManager","get_manager"]
