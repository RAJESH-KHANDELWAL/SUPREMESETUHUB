"""Retrieval-grounded AI context builder; does not call an LLM provider."""
from __future__ import annotations
from typing import Any
from .policy import CULTURE_SERVICE_WORK_BUSINESS_POLICY
class GlobalCultureServiceWorkBusinessAI:
    def __init__(self,engine:Any)->None: self.engine=engine
    def status(self)->dict[str,Any]:
        return {"component":"AI","status":"CONTEXT_BUILDER_READY","provider_invoked":False,"provider":"NOT_CONFIGURED"}
    def build_context(self,question:str,domain:str|None=None)->dict[str,Any]:
        question=str(question or "").strip()
        if not question: raise ValueError("AI_QUESTION_REQUIRED")
        return {"ecosystem":"GLOBAL_VASUDHAIVA_KUTUMBAKAM_CULTURE_SERVICE_WORK_BUSINESS","question":question,"domain":domain,"retrieval":self.engine.search(question,domain),"answer_policy":list(CULTURE_SERVICE_WORK_BUSINESS_POLICY),"provider_invocation":"NOT_PERFORMED","instruction":"Use only supported catalogue/evidence; state when live provider or opportunity data is unavailable."}
