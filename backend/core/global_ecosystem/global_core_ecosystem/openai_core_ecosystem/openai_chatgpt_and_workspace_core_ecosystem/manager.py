"""ChatGPT and Workspace domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIChatgptAndWorkspaceDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "CHATGPT_AND_WORKSPACE"


def get_manager() -> OpenAIChatgptAndWorkspaceDomainManager:
    """Return the shared domain runtime bound to ChatGPT and Workspace."""
    return OpenAIChatgptAndWorkspaceDomainManager()
