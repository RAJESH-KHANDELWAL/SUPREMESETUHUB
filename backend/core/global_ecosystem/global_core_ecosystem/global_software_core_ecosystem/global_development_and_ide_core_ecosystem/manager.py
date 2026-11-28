"""Domain manager for Development and IDE."""
from ..domain_runtime import SoftwareCoreDomainManager
class DevelopmentAndIdeManager(SoftwareCoreDomainManager):
    DOMAIN_ID="DEVELOPMENT_AND_IDE"
def get_manager(): return DevelopmentAndIdeManager()
