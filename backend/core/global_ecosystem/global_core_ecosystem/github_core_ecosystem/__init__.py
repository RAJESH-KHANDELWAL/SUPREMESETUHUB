"""GitHub provider-level CORE ecosystem public interface."""
from .catalog import get_github_core_catalog, list_github_families
from .manager import GitHubCoreManager, get_manager
from .orchestrator import GitHubCoreOrchestrator
from .service import GitHubCoreEcosystemService

__all__ = [
    "get_github_core_catalog",
    "list_github_families",
    "GitHubCoreManager",
    "get_manager",
    "GitHubCoreOrchestrator",
    "GitHubCoreEcosystemService",
]
