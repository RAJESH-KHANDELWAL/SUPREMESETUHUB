"""Domain manager for Desktop and Productivity."""
from ..domain_runtime import SoftwareCoreDomainManager
class DesktopAndProductivityManager(SoftwareCoreDomainManager):
    DOMAIN_ID="DESKTOP_AND_PRODUCTIVITY"
def get_manager(): return DesktopAndProductivityManager()
