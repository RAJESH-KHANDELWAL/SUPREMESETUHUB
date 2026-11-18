"""Canonical DeepSeek CORE catalog; metadata only."""
from copy import deepcopy
_C={"provider":"deepseek","layer":"CORE","status":"INTERFACE_ONLY","live_provider_calls_enabled":False,"api_ecosystem_ref":"backend/api/global_ecosystem/global_api_ecosystem/deepseek_api_ecosystem","capabilities":{
"chat_completions":{"package":"deepseek_chat_completions_core_ecosystem","endpoint":"POST /chat/completions","status":"CONTRACT_ONLY","live_enabled":False},
"responses":{"package":"deepseek_responses_core_ecosystem","endpoint":"POST /responses","status":"CONTRACT_ONLY","live_enabled":False},
"search":{"package":"deepseek_search_core_ecosystem","endpoint":"POST /v1/tools/search","status":"CONTRACT_ONLY","live_enabled":False},
"fetch":{"package":"deepseek_fetch_core_ecosystem","endpoint":"POST /v1/tools/fetch","status":"CONTRACT_ONLY","live_enabled":False}
}}
def get_catalog(): return deepcopy(_C)
def list_capabilities(): return deepcopy(_C["capabilities"])
