"""Pure provider lifecycle transition rules."""
ALLOWED={"CATALOG_ONLY":{"CONFIGURED","DISABLED"},"CONFIGURED":{"CONNECTED","DEGRADED","DISABLED","CATALOG_ONLY"},"CONNECTED":{"DEGRADED","DISABLED","CONFIGURED"},"DEGRADED":{"CONFIGURED","CONNECTED","DISABLED"},"DISABLED":{"CATALOG_ONLY"}}
def transition(current,target):
 if current not in ALLOWED or target not in ALLOWED[current]: raise ValueError("INVALID_STORAGE_PROVIDER_LIFECYCLE_TRANSITION")
 return {"from":current,"to":target,"state_changed":False,"requires_external_verification":target=="CONNECTED"}
