"""Codex and Developer Execution domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAICodexAndDeveloperExecutionDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "CODEX_AND_DEVELOPER_EXECUTION"


def get_manager() -> OpenAICodexAndDeveloperExecutionDomainManager:
    """Return the shared domain runtime bound to Codex and Developer Execution."""
    return OpenAICodexAndDeveloperExecutionDomainManager()
