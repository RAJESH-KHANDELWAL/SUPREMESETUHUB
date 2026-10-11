"""Global AI ecosystem bridge to existing central and personal AI APIs."""
from __future__ import annotations
from fastapi import APIRouter
from backend.api.ai import ai_engine
from backend.supreme.personal_ai.research import status as personal_ai_status
from backend.supreme.supreme_ecosystem.supreme_ai_ecosystem import status as supreme_ai_status
router=APIRouter(prefix="/api/v1/global-ai-ecosystem",tags=["GLOBAL AI ECOSYSTEM"])
@router.get("/status")
def global_ai_ecosystem_status():
 return {"success":True,"system":"GLOBAL AI ECOSYSTEM","parent":"SUPREME AI ECOSYSTEM","root":"SUPREME",
 "central_ai":ai_engine.status(),"personal_ai_research":personal_ai_status(),
 "supreme_ai_ecosystem":supreme_ai_status(),
 "source_package":"backend.api.global_ecosystem.global_api_ecosystem.global_ai_api_ecosystem",
 "privacy":"PRIVATE_BY_DEFAULT"}
@router.get("/capabilities")
def global_ai_capabilities():
 return {"success":True,"system":"GLOBAL AI ECOSYSTEM","capabilities":sorted(ai_engine.CAPABILITIES)}
@router.get("/providers")
def global_ai_providers():
 return {"success":True,"system":"GLOBAL AI ECOSYSTEM","providers":ai_engine.list_providers()}
