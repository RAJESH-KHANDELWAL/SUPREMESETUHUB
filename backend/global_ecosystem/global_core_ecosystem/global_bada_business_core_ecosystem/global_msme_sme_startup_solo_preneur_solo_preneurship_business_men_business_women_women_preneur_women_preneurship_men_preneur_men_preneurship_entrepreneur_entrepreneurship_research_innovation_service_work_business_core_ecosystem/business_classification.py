"""Business service classification without asserting execution."""
from .service_catalog import get_service
def classify_service(key):
 item=get_service(key)
 return None if item is None else {**item,"classification":"service_work_business","execution_status":"not_executed","verification_required":True}
