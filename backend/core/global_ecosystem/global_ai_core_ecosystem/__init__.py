"""GLOBAL AI CORE ECOSYSTEM public interface."""
LAYER = "CORE"
CATEGORY = "AI"
ECOSYSTEM_NAME = "GLOBAL AI CORE ECOSYSTEM"
ECOSYSTEM_ID = "GLOBAL-AI-CORE-ECOSYSTEM"

from .domain_runtime import GlobalAICoreDomainManager
from .ecosystem_service import GlobalAICoreEcosystemService
from .manager import GlobalAICoreManager, get_manager
from .service import GlobalAICoreService

__all__ = [
    "LAYER",
    "CATEGORY",
    "ECOSYSTEM_NAME",
    "ECOSYSTEM_ID",
    "GlobalAICoreDomainManager",
    "GlobalAICoreEcosystemService",
    "GlobalAICoreManager",
    "GlobalAICoreService",
    "get_manager",
]
