"""Hospitality service-work business ecosystem public interface."""
from .contracts import ECOSYSTEM_ID, ECOSYSTEM_VERSION
from .domain_catalog import DOMAINS, list_domains, get_domain, search_domains
from .manager import get_manager, GlobalHospitalityBusinessManager
__all__=["ECOSYSTEM_ID","ECOSYSTEM_VERSION","DOMAINS","list_domains","get_domain","search_domains","get_manager","GlobalHospitalityBusinessManager"]
