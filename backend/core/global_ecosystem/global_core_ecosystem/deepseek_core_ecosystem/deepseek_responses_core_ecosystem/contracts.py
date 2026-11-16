"""responses request contract; no provider transport."""
SECRET={"api_key","authorization","token","access_token","refresh_token","client_secret","password","secret"}
def _walk(v):
    if isinstance(v,dict):
        for k,x in v.items():
            if isinstance(k,str) and k.casefold() in SECRET: raise ValueError("secret-like field forbidden in CORE")
            _walk(x)
    elif isinstance(v,list):
        for x in v: _walk(x)
def _unknown(p,a):
    u=set(p)-a
    if u: raise ValueError("unsupported fields: "+", ".join(sorted(map(str,u))))
def validate_request(p):
    if not isinstance(p,dict): raise ValueError("payload must be a mapping")
    _walk(p)
    a={"model","input","stream","instructions","max_output_tokens"}; _unknown(p,a)
    v=p.get("input")
    if not ((isinstance(v,str) and v.strip()) or (isinstance(v,list) and v)): raise ValueError("input must be non-empty")
    if "stream" in p and not isinstance(p["stream"],bool): raise ValueError("stream must be boolean")
    return {"capability":"responses","accepted":True,"live_call":False}
