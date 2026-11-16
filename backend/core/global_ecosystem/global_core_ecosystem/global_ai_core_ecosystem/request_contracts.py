"""Provider-neutral AI request validation; never executes inference."""
from collections.abc import Mapping
_SECRET={"token","access_token","refresh_token","authorization","api_key","client_secret","private_key","secret","password"}
_ALLOWED={"provider_id","capability","model_id","task","context","request_id","options","metadata"}
def _reject(value):
 if isinstance(value,Mapping):
  for k,v in value.items():
   if isinstance(k,str) and k.casefold() in _SECRET: raise ValueError("SECRET_MATERIAL_FORBIDDEN_IN_CORE")
   _reject(v)
 elif isinstance(value,(list,tuple)):
  for v in value: _reject(v)
def validate_ai_request(payload):
 if not isinstance(payload,Mapping): raise ValueError("AI_REQUEST_MUST_BE_A_MAPPING")
 _reject(payload); unknown=set(payload)-_ALLOWED
 if unknown: raise ValueError("UNSUPPORTED_AI_REQUEST_FIELDS: "+", ".join(sorted(map(str,unknown))))
 for k in ("provider_id","capability","model_id","task","request_id"):
  if k in payload and payload[k] is not None and (not isinstance(payload[k],str) or not payload[k].strip()): raise ValueError(k.upper()+"_MUST_BE_NON_EMPTY_STRING")
 if "task" in payload and len(payload["task"])>12000: raise ValueError("AI_TASK_TOO_LONG")
 for k in ("context","options","metadata"):
  if k in payload and not isinstance(payload[k],Mapping): raise ValueError(k.upper()+"_MUST_BE_A_MAPPING")
 return {"accepted":True,"execution_performed":False,"provider_authorization_verified":False}
