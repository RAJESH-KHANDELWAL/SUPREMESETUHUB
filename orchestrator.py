"""Plan-only storage operations. Never transfers, overwrites or deletes data."""
from .catalog import get_provider
from .policy import authorize_plan
SUPPORTED={"LIST","DESCRIBE","UPLOAD","DOWNLOAD","COPY","MOVE","DELETE","RESTORE","BACKUP"}
def build_plan(*,provider_id,tenant_id,actor_id,operation,resource_id=None):
 if get_provider(provider_id) is None: raise ValueError("UNKNOWN_STORAGE_PROVIDER")
 operation=operation.upper()
 if operation not in SUPPORTED: raise ValueError("UNSUPPORTED_STORAGE_OPERATION")
 return {"success":True,"provider_id":provider_id.lower(),"operation":operation,"resource_id":resource_id,"policy":authorize_plan(tenant_id=tenant_id,actor_id=actor_id,operation=operation),"plan_only":True,"provider_call_performed":False,"data_transferred":False}
