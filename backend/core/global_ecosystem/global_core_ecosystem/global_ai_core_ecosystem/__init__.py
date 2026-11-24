"""AI CORE ECOSYSTEM package and public manager interface."""
LAYER = "CORE"
CATEGORY = "AI"
ECOSYSTEM_NAME = f"GLOBAL {CATEGORY.replace('_', ' ')} {LAYER} ECOSYSTEM"
ECOSYSTEM_ID = f"GLOBAL-{CATEGORY.replace('_', '-')}-{LAYER.upper()}-ECOSYSTEM"

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
