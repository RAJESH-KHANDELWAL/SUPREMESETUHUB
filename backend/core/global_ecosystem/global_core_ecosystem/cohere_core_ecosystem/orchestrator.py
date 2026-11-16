"""Provider-level discovery/readiness summary; no execution."""
from .catalog import list_capabilities
from .domain_catalog import list_domains
from .ecosystem_config import CORE_STATUS, LIVE_PROVIDER_CALLS_ENABLED
def ecosystem_summary():
    items = list_capabilities()
    return {"provider":"cohere","layer":"CORE","status":CORE_STATUS,"live_provider_calls_enabled":LIVE_PROVIDER_CALLS_ENABLED,"capability_count":len(items),"capabilities":items,"domains":list_domains(),"execution_enabled":False}
