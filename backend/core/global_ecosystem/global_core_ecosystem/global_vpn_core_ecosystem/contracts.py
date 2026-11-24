"""VPN Core metadata contracts; never accepts secret material or executes tunnels."""
from typing import Any
SECRET_FIELDS={"token","access_token","refresh_token","api_key","client_secret","password","secret","authorization","private_key","privatekey","psk","pre_shared_key","wireguard_private_key","ovpn_private_key"}
ALLOWED_FIELDS={"provider_id","operation","profile_id","device_id","protocol","region","exit_location","peer_id","route_policy","dns_policy","metadata","options","request_id"}
def _reject_secrets(value:Any)->None:
 if isinstance(value,dict):
  for key,item in value.items():
   if isinstance(key,str) and key.casefold() in SECRET_FIELDS:raise ValueError("SECRET_MATERIAL_FORBIDDEN_IN_CORE")
   _reject_secrets(item)
 elif isinstance(value,(list,tuple)):
  for item in value:_reject_secrets(item)
def validate_request(payload:dict[str,Any],*,provider_id:str|None=None)->dict[str,Any]:
 if not isinstance(payload,dict):raise ValueError("PAYLOAD_MUST_BE_MAPPING")
 _reject_secrets(payload);unknown=set(payload)-ALLOWED_FIELDS
 if unknown:raise ValueError("UNSUPPORTED_FIELDS: "+", ".join(sorted(map(str,unknown))))
 selected=payload.get("provider_id",provider_id)
 if not isinstance(selected,str) or not selected.strip():raise ValueError("PROVIDER_ID_REQUIRED")
 from .catalog import get_provider
 if get_provider(selected) is None:raise ValueError("UNKNOWN_VPN_PROVIDER")
 if provider_id is not None and selected!=provider_id:raise ValueError("PROVIDER_CONTEXT_MISMATCH")
 for key in ("operation","profile_id","device_id","protocol","region","exit_location","peer_id","request_id"):
  if key in payload and (not isinstance(payload[key],str) or not payload[key].strip()):raise ValueError(key.upper()+"_MUST_BE_NONEMPTY_STRING")
 for key in ("route_policy","dns_policy","metadata","options"):
  if key in payload and not isinstance(payload[key],dict):raise ValueError(key.upper()+"_MUST_BE_MAPPING")
 return {"success":True,"provider_id":selected,"accepted":True,"validated_only":True,"live_tunnel_operation":False}
