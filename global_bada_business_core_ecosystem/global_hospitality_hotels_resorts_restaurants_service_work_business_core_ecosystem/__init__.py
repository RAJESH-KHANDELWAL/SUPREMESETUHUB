"""Global hospitality service-work business ecosystem."""
from .domain_catalog import DOMAINS, list_domains, get_domain
from .manager import GlobalHospitalityBusinessManager, get_manager
__all__ = ["DOMAINS", "list_domains", "get_domain", "GlobalHospitalityBusinessManager", "get_manager"]
