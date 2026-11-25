"""Unified AI provider offering inventory."""
from .catalog import list_ai_providers
def list_ai_offerings():
 return [{"id":x["id"],"name":x["name"],"vendor":x.get("vendor"),"category":x["category"],"integration_status":x["integration_status"],"core_module":x["core_module"],"runtime_module":x["runtime_module"],"api_endpoint":x.get("api_endpoint"),"models_or_services":list(x.get("models_or_services",[]))} for x in list_ai_providers()]
def get_ai_offering(provider_id):
 return next((x for x in list_ai_offerings() if x["id"]==str(provider_id).strip().casefold()),None)
def ai_offerings_summary():
 items=list_ai_offerings(); counts={}
 for x in items:counts[x["integration_status"]]=counts.get(x["integration_status"],0)+1
 return {"success":True,"count":len(items),"integration_status_counts":counts,"offerings":items}
