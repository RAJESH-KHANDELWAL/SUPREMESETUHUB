"""Science, Research, Innovation & Technology API ecosystem."""
INDUSTRY_ID="science_research_innovation"
INDUSTRY_NAME="Science, Research, Innovation & Technology API Ecosystem"
COVERAGE=("india","global")
CHANNELS=("online","offline","hybrid")
STATUS="taxonomy_scaffold"
from .service import ScienceResearchService

__all__=["INDUSTRY_ID","INDUSTRY_NAME","COVERAGE","CHANNELS","STATUS","ScienceResearchService"]
