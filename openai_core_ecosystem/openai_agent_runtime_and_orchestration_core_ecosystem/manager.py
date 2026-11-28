"""Agent Runtime and Orchestration domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIAgentRuntimeAndOrchestrationDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "AGENT_RUNTIME_AND_ORCHESTRATION"


def get_manager() -> OpenAIAgentRuntimeAndOrchestrationDomainManager:
    """Return the shared domain runtime bound to Agent Runtime and Orchestration."""
    return OpenAIAgentRuntimeAndOrchestrationDomainManager()
