"""Global hospitality industry core ecosystem public interface."""
from .contracts import ECOSYSTEM_ID, ECOSYSTEM_VERSION
from .domain_catalog import DOMAINS, list_domains, get_domain, search_domains
from .manager import get_manager, GlobalHospitalityCoreManager
__all__=["ECOSYSTEM_ID","ECOSYSTEM_VERSION","DOMAINS","list_domains","get_domain","search_domains","get_manager","GlobalHospitalityCoreManager"]
