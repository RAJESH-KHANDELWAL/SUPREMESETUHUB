"""BADA BUSINESS APP ECOSYSTEM — application composition layer."""
from .catalog import APP_ECOSYSTEM_PROFILE, APP_MODULES, get_app_catalog
from .service import BadaBusinessAppService
from .manager import BadaBusinessAppManager
LAYER = "APP"
ECOSYSTEM_ID = "BADA_BUSINESS_APP_ECOSYSTEM"
STATUS = "APP_COMPOSITION_FOUNDATION_READY"
__all__ = ["APP_ECOSYSTEM_PROFILE", "APP_MODULES", "get_app_catalog",
           "BadaBusinessAppService", "BadaBusinessAppManager",
           "LAYER", "ECOSYSTEM_ID", "STATUS"]
