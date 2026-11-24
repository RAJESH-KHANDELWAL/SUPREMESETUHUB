SECRET_KEYS=frozenset({"api_key","authorization","token","access_token","refresh_token","client_secret","password","secret"})
def reject_secret_fields(value):
    if isinstance(value,dict):
        for key,item in value.items():
            if isinstance(key,str) and key.casefold() in SECRET_KEYS: raise PermissionError("secret-like field forbidden")
            reject_secret_fields(item)
    elif isinstance(value,list):
        for item in value: reject_secret_fields(item)
