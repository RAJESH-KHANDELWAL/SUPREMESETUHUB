"""Adapter reference registry; intentionally contains no SDK clients or secrets."""
from __future__ import annotations
from typing import Any
from ..catalog import list_storage_providers

def list_adapter_registry()->list[dict[str,Any]]:
 return [{"provider_id":p["provider_id"],"adapter_ref":p.get("adapter_ref"),"configured":bool(p.get("adapter_ref")),"status":"NOT_CONFIGURED" if not p.get("adapter_ref") else "REFERENCE_REGISTERED"} for p in list_storage_providers()]
