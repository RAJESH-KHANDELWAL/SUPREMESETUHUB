PROVIDER_ID="cerebras"
def validate_product_payload(payload):
 if not isinstance(payload,dict):raise ValueError("PRODUCT_PAYLOAD_MUST_BE_OBJECT")
 if payload.get("provider_id",PROVIDER_ID)!=PROVIDER_ID:raise ValueError("PROVIDER_ID_MISMATCH")
 if not isinstance(payload.get("capability"),str) or not payload["capability"].strip():raise ValueError("CAPABILITY_REQUIRED")
 return {"valid":True,"api_call_performed":False}
