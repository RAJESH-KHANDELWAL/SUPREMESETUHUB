"""Travel, Tourism & Hospitality domain package."""
INDUSTRY_ID="travel_tourism_hospitality"
INDUSTRY_NAME="Travel, Tourism & Hospitality"
COVERAGE=("india","global")
CHANNELS=("online","offline","hybrid")
STATUS="taxonomy_scaffold"
from .service import TravelService
__all__=["INDUSTRY_ID","INDUSTRY_NAME","COVERAGE","CHANNELS","STATUS","TravelService"]
