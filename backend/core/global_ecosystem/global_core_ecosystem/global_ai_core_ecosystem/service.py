"""Executor-injected Global AI task boundary; no provider SDK or API transport."""
from typing import Any,Callable
from .request_contracts import validate_ai_request
class GlobalAICoreService:
 def __init__(self,executor:Callable[...,dict[str,Any]]):
  if not callable(executor):raise ValueError("AI_EXECUTOR_REQUIRED")
  self._executor=executor
 def generate(self,*,task:str,context:dict[str,Any]|None=None,provider_id:str="openai",capability:str="text",model_id:str|None=None)->dict[str,Any]:
  if not isinstance(task,str) or not task.strip():raise ValueError("AI_TASK_REQUIRED")
  if context is not None and not isinstance(context,dict):raise ValueError("AI_CONTEXT_MUST_BE_OBJECT")
  payload={"provider_id":provider_id,"capability":capability,"task":task,"context":context or {}}
  if model_id is not None:payload["model_id"]=model_id
  validate_ai_request(payload)
  if model_id is not None and (not isinstance(model_id,str) or not model_id.strip() or len(model_id)>160):raise ValueError("AI_MODEL_ID_INVALID")
  result=self._executor(provider_id=provider_id,capability=capability,model_id=model_id,task=task.strip(),context=context or {})
  if not isinstance(result,dict) or not result.get("output"):raise RuntimeError("AI_ENGINE_RETURNED_INVALID_RESULT")
  return {"success":True,"system":"GLOBAL AI ECOSYSTEM","provider":result.get("provider",provider_id),"model":result.get("model"),"output":result["output"],"live_verified":bool(result.get("live_verified",False)),"usage":result.get("usage")}
