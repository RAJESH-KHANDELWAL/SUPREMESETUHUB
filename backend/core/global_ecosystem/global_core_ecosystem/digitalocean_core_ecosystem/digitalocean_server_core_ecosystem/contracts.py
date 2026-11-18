"""server request contract; no transport or credential access."""
SECRET={"api_key","authorization","token","access_token","refresh_token","client_secret","password","secret"}
def _walk(value):
    if isinstance(value,dict):
        for key,item in value.items():
            if isinstance(key,str) and key.casefold() in SECRET: raise ValueError("secret-like fields are forbidden in CORE")
            _walk(item)
    elif isinstance(value,list):
        for item in value: _walk(item)
def _unknown(payload,allowed):
    extra=set(payload)-allowed
    if extra: raise ValueError("unsupported request fields: "+", ".join(sorted(map(str,extra))))
def validate_request(payload):
    if not isinstance(payload,dict): raise ValueError("payload must be a mapping")
    _walk(payload)
    allowed={"operation","resource_id","region","project_id","options","metadata"}
    _unknown(payload,allowed)
    if "operation" in payload and (not isinstance(payload["operation"],str) or not payload["operation"].strip()): raise ValueError("operation must be non-empty")
    if "resource_id" in payload and not isinstance(payload["resource_id"],str): raise ValueError("resource_id must be a string")
    if "region" in payload and not isinstance(payload["region"],str): raise ValueError("region must be a string")
    for key in ("project_id","options","metadata"):
        if key in payload and not isinstance(payload[key],dict): raise ValueError(key+" must be a mapping")
    return {"capability":"server","accepted":True,"live_call":False}
