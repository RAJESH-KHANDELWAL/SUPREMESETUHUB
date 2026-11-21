"""Unified Mistral offerings derived from the canonical provider catalog."""
from __future__ import annotations
from typing import Any
from .catalog import get_mistral_core_catalog

def list_mistral_offerings()->list[dict[str,Any]]:
 return [{"id":p["key"],"ecosystem_id":p["ecosystem_id"],"name":p["name"],
  "capabilities":list(p["capabilities"]),"domains":list(p["domains"]),
  "core_module":p["core_module"],"api_catalog_ref":p["api_catalog_ref"],
  "status":p["status"],"connected":False,"live_connection_verified":False}
  for p in get_mistral_core_catalog()["children"]]

def mistral_offerings_summary()->dict[str,Any]:
 rows=list_mistral_offerings()
 return {"success":True,"count":len(rows),"offerings":rows}

__all__=["list_mistral_offerings","mistral_offerings_summary"]
