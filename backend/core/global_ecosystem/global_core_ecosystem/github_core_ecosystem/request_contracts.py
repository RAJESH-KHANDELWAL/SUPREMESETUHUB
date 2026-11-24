"""Shared safe request-shape validation; does not execute GitHub API calls."""
from collections.abc import Mapping
_SECRET={"token","access_token","refresh_token","authorization","api_key","client_secret","private_key","webhook_secret","password","secret"}
_ALLOWED={"operation","resource_id","owner","repository","organization","installation_id","ref","options","metadata","request_id"}
def _reject_secrets(value):
 if isinstance(value,Mapping):
  for key,item in value.items():
   if isinstance(key,str) and key.casefold() in _SECRET: raise ValueError("SECRET_MATERIAL_FORBIDDEN_IN_CORE")
   _reject_secrets(item)
 elif isinstance(value,(list,tuple)):
  for item in value: _reject_secrets(item)
def validate_family_request(payload,family):
 if not isinstance(payload,Mapping): raise ValueError("PAYLOAD_MUST_BE_A_MAPPING")
 _reject_secrets(payload); unknown=set(payload)-_ALLOWED
 if unknown: raise ValueError("UNSUPPORTED_REQUEST_FIELDS: "+", ".join(sorted(map(str,unknown))))
 if "operation" in payload and (not isinstance(payload["operation"],str) or not payload["operation"].strip()): raise ValueError("OPERATION_MUST_BE_NON_EMPTY")
 for key in ("resource_id","owner","repository","organization","installation_id","ref","request_id"):
  if key in payload and payload[key] is not None and not isinstance(payload[key],str): raise ValueError(key.upper()+"_MUST_BE_STRING")
 for key in ("options","metadata"):
  if key in payload and not isinstance(payload[key],Mapping): raise ValueError(key.upper()+"_MUST_BE_A_MAPPING")
 return {"provider":"github","family":family,"accepted":True,"live_call":False}
