from .domain_catalog import list_domains
from .region_catalog import list_regional_frameworks
ECOSYSTEM_ID="GLOBAL-ENERGY-UTILITIES-ENVIRONMENT-CORE-ECOSYSTEM"
def get_catalog(): return {"ecosystem_id":ECOSYSTEM_ID,"name":"GLOBAL ENERGY UTILITIES & ENVIRONMENT CORE ECOSYSTEM","layer":"GLOBAL_CORE","domain_count":len(list_domains()),"regions":sorted(list_regional_frameworks()),"mode":"CANONICAL_METADATA"}
