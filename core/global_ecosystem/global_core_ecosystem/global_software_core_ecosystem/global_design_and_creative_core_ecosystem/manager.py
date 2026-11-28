"""Domain manager for Design and Creative."""
from ..domain_runtime import SoftwareCoreDomainManager
class DesignAndCreativeManager(SoftwareCoreDomainManager):
    DOMAIN_ID="DESIGN_AND_CREATIVE"
def get_manager(): return DesignAndCreativeManager()
