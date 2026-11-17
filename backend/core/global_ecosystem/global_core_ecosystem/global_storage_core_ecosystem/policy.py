"""Metadata-only storage policy gates; never accept credentials or file bytes."""
SENSITIVE={"access_token","refresh_token","password","secret","secret_key","signed_url","encryption_key","file_bytes","content"}
def validate_resource_metadata(payload):
 if not isinstance(payload,dict): raise ValueError("RESOURCE_METADATA_MUST_BE_OBJECT")
 required=("tenant_id","resource_id","provider_id","resource_type")
 missing=[k for k in required if not isinstance(payload.get(k),str) or not payload[k].strip()]
 if missing: raise ValueError("MISSING_REQUIRED_FIELDS:"+",".join(missing))
 leaked=sorted(k for k in payload if k.lower() in SENSITIVE)
 if leaked: raise ValueError("SENSITIVE_PAYLOAD_NOT_ALLOWED:"+",".join(leaked))
 if payload.get("encryption_at_rest") not in (None,True,False): raise ValueError("INVALID_ENCRYPTION_METADATA")
 return {"success":True,"metadata_only":True,"execution_performed":False}
def authorize_plan(*,tenant_id,actor_id,operation):
 if not all(isinstance(x,str) and x.strip() for x in (tenant_id,actor_id,operation)): raise ValueError("TENANT_ACTOR_AND_OPERATION_REQUIRED")
 return {"allowed_for_planning":True,"authorization_verified":False,"execution_performed":False}
