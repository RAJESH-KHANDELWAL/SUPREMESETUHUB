"""Transport, Logistics & Supply Chain domain."""
INDUSTRY_ID="transport_logistics_supply_chain"
INDUSTRY_NAME="Transport, Logistics & Supply Chain"
COVERAGE=("india","global")
CHANNELS=("online","offline","hybrid")
STATUS="taxonomy_scaffold"
from .service import TransportService
__all__=["INDUSTRY_ID","INDUSTRY_NAME","COVERAGE","CHANNELS","STATUS","TransportService"]
