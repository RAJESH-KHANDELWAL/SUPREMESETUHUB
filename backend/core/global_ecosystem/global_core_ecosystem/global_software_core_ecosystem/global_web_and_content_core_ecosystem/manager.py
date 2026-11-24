"""Domain manager for Web and Content."""
from ..domain_runtime import SoftwareCoreDomainManager
class WebAndContentManager(SoftwareCoreDomainManager):
    DOMAIN_ID="WEB_AND_CONTENT"
def get_manager(): return WebAndContentManager()
