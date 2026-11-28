SECRET_KEYS=frozenset({"api_key","authorization","token","access_token","refresh_token","client_secret","password","secret"})
def reject_secret_fields(value):
    if isinstance(value,dict):
        for k,v in value.items():
            if isinstance(k,str) and k.casefold() in SECRET_KEYS: raise PermissionError("secret-like field forbidden")
            reject_secret_fields(v)
    elif isinstance(value,list):
        for v in value: reject_secret_fields(v)
