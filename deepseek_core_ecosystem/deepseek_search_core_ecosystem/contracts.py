"""search request contract; no provider transport."""
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
    a={"query","max_results","filters"}; _unknown(p,a)
    if not isinstance(p.get("query"),str) or not p["query"].strip(): raise ValueError("query must be non-empty")
    if "max_results" in p and (isinstance(p["max_results"],bool) or not isinstance(p["max_results"],int) or p["max_results"]<1): raise ValueError("max_results must be positive")
    return {"capability":"search","accepted":True,"live_call":False}
