"""Technology, IT & Telecommunications domain package."""
INDUSTRY_ID="technology_it_telecommunications"
INDUSTRY_NAME="Technology, IT & Telecommunications"
COVERAGE=("india","global")
CHANNELS=("online","offline","hybrid")
STATUS="taxonomy_scaffold"
from .service import TechnologyService
__all__=["INDUSTRY_ID","INDUSTRY_NAME","COVERAGE","CHANNELS","STATUS","TechnologyService"]
