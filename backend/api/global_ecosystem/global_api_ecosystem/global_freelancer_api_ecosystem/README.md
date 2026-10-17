# GLOBAL FREELANCER API ECOSYSTEM

This catalog package represents the freelancer category in the GLOBAL API
ECOSYSTEM hierarchy. The live FastAPI router remains registered from
`backend/api/global_freelancer_ecosystem.py` by `backend/api/app.py`.

The category is connected to:
- Core registration: `GLOBAL-FREELANCER-ECOSYSTEM`
- Engine: `backend/engines/freelancer_ecosystem/manager.py`
- Central database repository: `backend/database/freelancer_ecosystem.py`
- Existing storage engine and asset access controls.

Do not duplicate HTTP route implementations in this catalog package. The API
hierarchy is discovery metadata; `backend/api/app.py` remains the runtime owner.
