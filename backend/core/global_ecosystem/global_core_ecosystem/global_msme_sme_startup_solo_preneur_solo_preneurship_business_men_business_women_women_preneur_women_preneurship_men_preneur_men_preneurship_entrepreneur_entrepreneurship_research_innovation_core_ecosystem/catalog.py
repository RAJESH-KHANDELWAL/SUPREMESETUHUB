"""Global CORE catalog metadata."""
from .domain_catalog import DOMAINS
CATALOG={"catalogue_id":"GLOBAL_MSME_SME_STARTUP_ENTREPRENEURSHIP_RESEARCH_INNOVATION_CORE","domain_count":len(DOMAINS),"domains":[x["domain_id"] for x in DOMAINS]}
def get_catalog(): return {**CATALOG,"domains":list(CATALOG["domains"])}
