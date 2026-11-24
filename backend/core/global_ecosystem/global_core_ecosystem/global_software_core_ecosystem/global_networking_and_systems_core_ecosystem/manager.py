"""Domain manager for Networking and Systems."""
from ..domain_runtime import SoftwareCoreDomainManager
class NetworkingAndSystemsManager(SoftwareCoreDomainManager):
    DOMAIN_ID="NETWORKING_AND_SYSTEMS"
def get_manager(): return NetworkingAndSystemsManager()
