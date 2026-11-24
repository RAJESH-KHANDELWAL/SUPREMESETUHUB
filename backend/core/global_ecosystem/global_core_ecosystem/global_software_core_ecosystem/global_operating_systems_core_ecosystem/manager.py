"""Domain manager for Operating Systems."""
from ..domain_runtime import SoftwareCoreDomainManager
class OperatingSystemsManager(SoftwareCoreDomainManager):
    DOMAIN_ID="OPERATING_SYSTEMS"
def get_manager(): return OperatingSystemsManager()
