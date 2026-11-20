"""Domain Core responsibility taxonomy."""
from .catalog import DOMAIN_DEFINITIONS
def get_domain_catalog():
    return {k:dict(v) for k,v in DOMAIN_DEFINITIONS.items()}
def get_domain_summary():
    return {"ecosystem_id":"GLOBAL-DOMAIN-CORE-ECOSYSTEM","domain_count":len(DOMAIN_DEFINITIONS),"domains":[{"domain_id":k,**v} for k,v in DOMAIN_DEFINITIONS.items()]}
