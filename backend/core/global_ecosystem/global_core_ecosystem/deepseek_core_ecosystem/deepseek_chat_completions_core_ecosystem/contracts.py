"""chat_completions request contract; no provider transport."""
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
    a={"model","messages","stream","temperature","max_tokens"}; _unknown(p,a)
    v=p.get("messages")
    if not isinstance(v,list) or not v or any(not isinstance(m,dict) or not isinstance(m.get("role"),str) or not isinstance(m.get("content"),(str,list)) for m in v): raise ValueError("invalid messages")
    if "stream" in p and not isinstance(p["stream"],bool): raise ValueError("stream must be boolean")
    return {"capability":"chat_completions","accepted":True,"live_call":False}
