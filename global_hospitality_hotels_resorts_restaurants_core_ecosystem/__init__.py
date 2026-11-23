"""Global hospitality industry core ecosystem."""
from .domain_catalog import DOMAINS, list_domains, get_domain
from .manager import GlobalHospitalityCoreManager, get_manager
__all__ = ["DOMAINS", "list_domains", "get_domain", "GlobalHospitalityCoreManager", "get_manager"]
