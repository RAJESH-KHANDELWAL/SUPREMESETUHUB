"""Manager for the AI_ML_AND_INTELLIGENCE Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class AiMachineLearningDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "AI_ML_AND_INTELLIGENCE"


def get_manager() -> AiMachineLearningDomainManager:
    return AiMachineLearningDomainManager()


__all__ = ["AiMachineLearningDomainManager", "get_manager"]
