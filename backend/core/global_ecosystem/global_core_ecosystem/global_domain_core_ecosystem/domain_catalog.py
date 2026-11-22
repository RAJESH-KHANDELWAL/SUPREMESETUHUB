"""Domain catalog with standardized sector ecosystem naming."""
from .manager import DOMAIN_DEFINITIONS, ECOSYSTEM_ID, ECOSYSTEM_NAME, list_sector_ecosystems
def get_domain_catalog():
    return {k:dict(v) for k,v in DOMAIN_DEFINITIONS.items()}
def get_domain_summary():
    return {"ecosystem_id":ECOSYSTEM_ID,"ecosystem_name":ECOSYSTEM_NAME,"domain_count":len(DOMAIN_DEFINITIONS),"domains":[{"domain_id":k,**v} for k,v in DOMAIN_DEFINITIONS.items()],"sector_ecosystem_count":len(list_sector_ecosystems())}
def get_sector_ecosystem_catalog():
    return list_sector_ecosystems()
