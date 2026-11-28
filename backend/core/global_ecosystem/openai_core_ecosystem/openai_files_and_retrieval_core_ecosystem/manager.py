"""Files and Retrieval domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIFilesAndRetrievalDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "FILES_AND_RETRIEVAL"


def get_manager() -> OpenAIFilesAndRetrievalDomainManager:
    """Return the shared domain runtime bound to Files and Retrieval."""
    return OpenAIFilesAndRetrievalDomainManager()
