"""Shared VPS request contract; rejects secret material and performs no transport."""
from typing import Any
SECRET_FIELDS={"token","access_token","refresh_token","api_key","client_secret","password","secret","authorization","private_key"}
ALLOWED_FIELDS={"provider_id","operation","resource_id","region","zone","image_id","size_id","project_id","network_id","volume_id","metadata","options","request_id"}
def _reject(value:Any)->None:
 if isinstance(value,dict):
  for k,v in value.items():
   if isinstance(k,str) and k.casefold() in SECRET_FIELDS: raise ValueError("SECRET_MATERIAL_FORBIDDEN_IN_CORE")
   _reject(v)
 elif isinstance(value,(list,tuple)):
  for v in value:_reject(v)
def validate_request(payload:dict[str,Any],*,provider_id:str|None=None)->dict[str,Any]:
 if not isinstance(payload,dict): raise ValueError("PAYLOAD_MUST_BE_MAPPING")
 _reject(payload); extra=set(payload)-ALLOWED_FIELDS
 if extra: raise ValueError("UNSUPPORTED_FIELDS: "+", ".join(sorted(map(str,extra))))
 selected=payload.get("provider_id",provider_id)
 if not isinstance(selected,str) or not selected.strip(): raise ValueError("PROVIDER_ID_REQUIRED")
 from .catalog import get_provider
 if get_provider(selected) is None: raise ValueError("UNKNOWN_VPS_PROVIDER")
 if provider_id is not None and selected!=provider_id: raise ValueError("PROVIDER_CONTEXT_MISMATCH")
 if "operation" in payload and (not isinstance(payload["operation"],str) or not payload["operation"].strip()): raise ValueError("INVALID_OPERATION")
 for k in ("metadata","options","project_id"):
  if k in payload and not isinstance(payload[k],dict): raise ValueError(k.upper()+"_MUST_BE_MAPPING")
 for k in ("resource_id","region","zone","image_id","size_id","network_id","volume_id","request_id"):
  if k in payload and not isinstance(payload[k],str): raise ValueError(k.upper()+"_MUST_BE_STRING")
 return {"success":True,"provider_id":selected,"accepted":True,"validated_only":True,"live_call":False}
