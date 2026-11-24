"""Private owner-only SUPREME PERSONAL AI research and outreach-draft routes."""
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,Field
from backend.supreme.personal_ai.research import TRACKS,draft_outreach,list_results,research,status
router=APIRouter(prefix="/api/v1/supreme-personal-ai",tags=["SUPREME PERSONAL AI"])
class ResearchRequest(BaseModel):
 track:str="all"
 limit_per_query:int=Field(default=5,ge=1,le=10)
class DraftRequest(BaseModel):
 business_name:str=Field(min_length=1,max_length=200)
 service:str=Field(min_length=1,max_length=300)
 public_context:str=Field(min_length=1,max_length=1000)
 contact_name:str=Field(default="",max_length=120)
 channel:str="email"
@router.get("/status")
def personal_ai_status(): return status()
@router.get("/tracks")
def research_tracks(): return {"success":True,"tracks":TRACKS}
@router.post("/research")
async def run_research(payload:ResearchRequest):
 result=await research(payload.track,payload.limit_per_query)
 if result.get("error")=="UNKNOWN_RESEARCH_TRACK": raise HTTPException(status_code=400,detail=result)
 if result.get("error")=="GOOGLE_SEARCH_NOT_CONFIGURED": raise HTTPException(status_code=503,detail=result)
 return result
@router.get("/research/results")
def get_research_results(track:str|None=None,limit:int=50): return list_results(track,limit)
@router.post("/outreach/draft")
def create_outreach_draft(payload:DraftRequest):
 channel=payload.channel.strip().lower()
 if channel not in {"email","whatsapp"}: raise HTTPException(status_code=400,detail="CHANNEL_MUST_BE_EMAIL_OR_WHATSAPP")
 try: return {"success":True,"draft":draft_outreach(payload.business_name,payload.service,payload.public_context,payload.contact_name,channel)}
 except ValueError as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc
