"""Sports, Recreation & Community domain package."""
INDUSTRY_ID="sports_recreation_community"
INDUSTRY_NAME="Sports, Recreation & Community"
COVERAGE=("india","global")
CHANNELS=("online","offline","hybrid")
STATUS="taxonomy_scaffold"
from .service import SportsCommunityService
__all__=["INDUSTRY_ID","INDUSTRY_NAME","COVERAGE","CHANNELS","STATUS","SportsCommunityService"]
