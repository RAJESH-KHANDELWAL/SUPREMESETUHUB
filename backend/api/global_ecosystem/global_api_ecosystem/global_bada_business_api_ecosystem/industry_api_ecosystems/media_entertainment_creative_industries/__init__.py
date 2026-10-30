"""Media, Entertainment & Creative Industries domain."""
INDUSTRY_ID="media_entertainment_creative_industries"
INDUSTRY_NAME="Media, Entertainment & Creative Industries"
COVERAGE=("india","global")
CHANNELS=("online","offline","hybrid")
STATUS="taxonomy_scaffold"
from .service import MediaService
__all__=["INDUSTRY_ID","INDUSTRY_NAME","COVERAGE","CHANNELS","STATUS","MediaService"]
