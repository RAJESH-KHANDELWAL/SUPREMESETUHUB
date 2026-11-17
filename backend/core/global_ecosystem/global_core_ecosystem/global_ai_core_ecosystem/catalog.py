"""Global AI Core catalog backed by the existing runtime provider registry."""
from copy import deepcopy
ECOSYSTEM={"ecosystem_id":"GLOBAL-AI-CORE-ECOSYSTEM","name":"GLOBAL AI CORE ECOSYSTEM","provider":"global_ai","ecosystem_type":"GLOBAL_PROVIDER_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","status":"REGISTERED","enabled":True,"runtime_catalog_ref":"backend/global_ecosystem/global_ai_ecosystem/providers.py","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem"}
_API_ONLY_ALIASES={
 "cloudflare":{"id":"cloudflare","name":"Cloudflare AI","vendor":"Cloudflare","category":"api_catalog_only","api_endpoint":None,"integration_status":"catalog_only","core_module":None,"runtime_module":None,"api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/cloudflare_ai_api_ecosystem"},
 "nsfwinfra":{"id":"nsfwinfra","name":"NSFWInfra","vendor":"NSFWInfra","category":"api_catalog_only","api_endpoint":None,"integration_status":"catalog_only","core_module":None,"runtime_module":None,"api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/nsfwinfra_ai_api_ecosystem"}
}
def _source():
 from backend.global_ecosystem.global_ai_ecosystem.providers import list_ai_providers
 return list_ai_providers()
def list_ai_providers(*,category=None,integration_status=None):
 out=[]
 for item in _source():
  x=deepcopy(item); x["core_module"]="backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/"+x["id"]+"_core_ecosystem"; x["runtime_module"]="backend/global_ecosystem/global_ai_ecosystem/"+x["id"]+"_ecosystem"
  if category is not None and x.get("category")!=category: continue
  if integration_status is not None and x.get("integration_status")!=integration_status: continue
  out.append(x)
 return tuple(out)
def get_ai_provider(provider_id):
 key=str(provider_id).strip().casefold()
 aliases={"openai":"openai_chatgpt","anthropic":"anthropic_claude","google":"google_gemini","aws":"aws_bedrock","microsoft":"microsoft_azure_ai","ibm":"ibm_watsonx","meta":"meta_ai","apple":"apple_intelligence","nvidia":"nvidia_ai","oracle":"oracle_cloud_ai","adobe":"adobe_firefly"}
 key=aliases.get(key,key)
 found=next((deepcopy(x) for x in list_ai_providers() if x["id"]==key),None)
 if found is not None:return found
 alias=_API_ONLY_ALIASES.get(key)
 return deepcopy(alias) if alias else None
def get_global_ai_catalog(): return {**deepcopy(ECOSYSTEM),"children":[{k:v for k,v in x.items() if k!="credential_env"} for x in list_ai_providers()]}
def validate_provider_registry():
 errors=[]; seen=set()
 for i,x in enumerate(list_ai_providers()):
  pid=x.get("id")
  if not isinstance(pid,str) or not pid.strip(): errors.append(f"entry[{i}] invalid id"); continue
  if pid in seen: errors.append("duplicate provider id: "+pid)
  seen.add(pid)
  if not x.get("name") or not x.get("category"): errors.append(pid+" missing name/category")
  if x.get("integration_status") not in {"scaffold","catalog_only","integration_in_progress","live"}: errors.append(pid+" invalid integration_status")
  if x.get("integration_status")=="live" and not x.get("api_endpoint"): errors.append(pid+" live without endpoint")
 return tuple(errors)
