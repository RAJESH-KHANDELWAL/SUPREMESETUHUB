"""Independent GLOBAL SECURITY runtime ecosystem."""
from .manager import GlobalSecurityEcosystemManager
from .service import GlobalSecurityEcosystemService

LAYER = "SECURITY"
ECOSYSTEM_NAME = "GLOBAL SECURITY ECOSYSTEM"
ECOSYSTEM_ID = "GLOBAL-SECURITY-ECOSYSTEM"
__all__ = ["GlobalSecurityEcosystemManager", "GlobalSecurityEcosystemService", "LAYER", "ECOSYSTEM_NAME", "ECOSYSTEM_ID"]
