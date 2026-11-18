DESTRUCTIVE={"delete","publish","billing","admin","write"}
def evaluate(capability,authorized=False,consent=False):
 if not authorized:return {"allowed":False,"reason":"APPLICATION_AUTHORIZATION_REQUIRED"}
 if capability in DESTRUCTIVE and not consent:return {"allowed":False,"reason":"EXPLICIT_CONSENT_REQUIRED"}
 return {"allowed":True,"reason":"APPLICATION_LAYER_AUTHORIZED"}
