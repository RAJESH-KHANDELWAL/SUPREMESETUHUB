"""GLOBAL DOMAIN CORE ECOSYSTEM package."""
from .catalog import ECOSYSTEM_ID, ECOSYSTEM_NAME, DOMAIN_DEFINITIONS, PROVIDER_DIRECTORIES
from .sector_catalog import SECTORS, list_sectors
from .provider_registry import list_expanded_provider_registry
from .manager import GlobalDomainCoreManager, get_manager
LAYER = "CORE"
CATEGORY = "DOMAIN"
__all__=["LAYER","CATEGORY","ECOSYSTEM_ID","ECOSYSTEM_NAME","DOMAIN_DEFINITIONS","PROVIDER_DIRECTORIES","SECTORS","list_sectors","list_expanded_provider_registry","GlobalDomainCoreManager","get_manager"]
