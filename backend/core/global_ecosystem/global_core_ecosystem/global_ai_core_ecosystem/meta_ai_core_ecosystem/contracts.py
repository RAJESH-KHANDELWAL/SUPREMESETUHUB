"""Meta AI provider-neutral request contract."""
from ..request_contracts import validate_ai_request
def validate_request(payload):
 result=validate_ai_request(payload)
 if payload.get("provider_id","meta")!="meta": raise ValueError("PROVIDER_ID_MISMATCH")
 return {**result,"provider_id":"meta"}
