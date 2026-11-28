"""Safety, Evaluation and Moderation domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAISafetyEvaluationAndModerationDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "SAFETY_EVALUATION_AND_MODERATION"


def get_manager() -> OpenAISafetyEvaluationAndModerationDomainManager:
    """Return the shared domain runtime bound to Safety, Evaluation and Moderation."""
    return OpenAISafetyEvaluationAndModerationDomainManager()
