"""Safe, read-only diagnostics for the Python process hosting the APP."""
import os,platform,sys,time
from datetime import datetime,timezone
_STARTED_MONOTONIC=time.monotonic();_STARTED_AT=datetime.now(timezone.utc).isoformat()
def runtime_status():
    return {"status":"PROCESS_RUNNING","python_version":platform.python_version(),"platform":sys.platform,"process_id":os.getpid(),"started_at":_STARTED_AT,"uptime_seconds":max(0,int(time.monotonic()-_STARTED_MONOTONIC)),"deployment_environment":"RENDER" if os.getenv("RENDER_SERVICE_NAME") else "DOCKER" if os.path.exists("/.dockerenv") else "SELF_HOSTED","secrets_exposed":False}
__all__=["runtime_status"]
