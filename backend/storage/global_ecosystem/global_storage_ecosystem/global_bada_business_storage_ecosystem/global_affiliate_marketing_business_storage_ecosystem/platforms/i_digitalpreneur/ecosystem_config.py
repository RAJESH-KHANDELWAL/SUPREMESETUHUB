"""Runtime config for I_DIGITALPRENEUR; no embedded platform credentials."""
import os
PLATFORM_ID="I_DIGITALPRENEUR"
def get_config()->dict:return {"enabled":os.getenv("I_DIGITALPRENEUR_ENABLED","true").lower()=="true","connection_state":"NOT_CONFIGURED","credentials_configured":False}
