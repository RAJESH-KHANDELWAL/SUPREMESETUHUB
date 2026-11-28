"""Manager for the AI, Machine Learning and Intelligence AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class AiMlAndIntelligenceDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="AI_ML_AND_INTELLIGENCE"
def get_manager()->AiMlAndIntelligenceDomainManager:return AiMlAndIntelligenceDomainManager()
__all__=["AiMlAndIntelligenceDomainManager","get_manager"]
