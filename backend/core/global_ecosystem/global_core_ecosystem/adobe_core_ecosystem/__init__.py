"""Adobe Core Ecosystem public interfaces."""
from .service import AdobeCoreEcosystemService
from .orchestrator import AdobeCoreOrchestrator
from .manager import AdobeCoreManager, get_manager
from .domain_runtime import AdobeCoreDomainManager
__all__ = ["AdobeCoreEcosystemService", "AdobeCoreOrchestrator", "AdobeCoreManager", "AdobeCoreDomainManager", "get_manager"]
