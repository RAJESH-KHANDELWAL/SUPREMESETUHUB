"""Domain manager for Gaming and Interactive."""
from ..domain_runtime import SoftwareCoreDomainManager
class GamingAndInteractiveManager(SoftwareCoreDomainManager):
    DOMAIN_ID="GAMING_AND_INTERACTIVE"
def get_manager(): return GamingAndInteractiveManager()
