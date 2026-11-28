"""Read-only ecosystem inventory export."""
from .constants import ECOSYSTEM_ID
from .catalog import list_products
from .domain_catalog import list_domains
def snapshot(): return {"ecosystem_id":ECOSYSTEM_ID,"products":list_products(),"domains":list_domains(),"live_connections_verified":False}
