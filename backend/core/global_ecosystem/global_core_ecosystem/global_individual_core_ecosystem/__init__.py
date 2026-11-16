"""GLOBAL INDIVIDUAL CORE ECOSYSTEM."""
LAYER="CORE"
CATEGORY="INDIVIDUAL"
ECOSYSTEM_NAME="GLOBAL INDIVIDUAL CORE ECOSYSTEM"
ECOSYSTEM_ID="GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM"
from .orchestrator import GlobalIndividualCoreOrchestrator
from .service import GlobalIndividualCoreService
__all__=["LAYER","CATEGORY","ECOSYSTEM_NAME","ECOSYSTEM_ID","GlobalIndividualCoreOrchestrator","GlobalIndividualCoreService"]
