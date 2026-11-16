"""fetch request contract; no provider transport."""
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
    a={"urls","max_pages","extract"}; _unknown(p,a)
    v=p.get("urls")
    if not isinstance(v,list) or not v or any(not isinstance(x,str) or not x.startswith(("https://","http://")) for x in v): raise ValueError("urls must be HTTP(S) URL list")
    return {"capability":"fetch","accepted":True,"live_call":False}
