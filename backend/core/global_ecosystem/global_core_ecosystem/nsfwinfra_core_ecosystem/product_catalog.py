"""Provider product inventory derived from canonical Core catalog."""
from __future__ import annotations
from typing import Any
from .catalog import get_nsfwinfra_core_catalog
def list_products()->list[dict[str,Any]]:
 return [dict(item) for item in get_nsfwinfra_core_catalog()["children"]]
def get_product(ecosystem_id:str)->dict[str,Any]|None:
 return next((dict(p) for p in list_products() if p["ecosystem_id"]==ecosystem_id),None)
