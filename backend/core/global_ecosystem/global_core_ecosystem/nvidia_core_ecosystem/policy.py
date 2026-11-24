FORBIDDEN={"API_TRANSPORT","AUTHENTICATION","SECRET_STORAGE","REMOTE_EXECUTION","PERSISTENCE"}
def check(action):
 x=str(action).strip().upper();return {"allowed":x not in FORBIDDEN,"scope":"CORE_METADATA_ONLY","action":x}
def safe_summary(p):return {k:v for k,v in p.items() if k not in {"secret","token","credential","private_key"}}
