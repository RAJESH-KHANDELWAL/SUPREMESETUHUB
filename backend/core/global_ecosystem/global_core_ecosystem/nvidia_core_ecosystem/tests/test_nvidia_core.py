from backend.core.global_ecosystem.global_core_ecosystem.nvidia_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.nvidia_core_ecosystem.product_catalog import list_products
from backend.core.global_ecosystem.global_core_ecosystem.nvidia_core_ecosystem.domain_catalog import list_domains
from backend.core.global_ecosystem.global_core_ecosystem.nvidia_core_ecosystem.master_catalog import reference
def test_products_unique():
 p=list_products();assert len(p)==17 and len({x["product_id"] for x in p})==17
def test_metadata_only_status():
 m=get_manager();assert m.status()["status"]=="CORE_CATALOG_ONLY";assert m.health()["live_connections_verified"]==0
def test_lookup():
 m=get_manager();assert m.get_product("cuda")["name"]=="CUDA";assert m.get_product("NVIDIA-CUDA-CORE-ECOSYSTEM")["slug"]=="cuda";assert m.get_product("unknown") is None
def test_domains_dependency():
 assert len(list_domains())==24;assert len(get_manager().dependency_map()["edges"])==17
def test_catalog_reference():
 r=reference();assert r["target_unique_entries"]==2468 and r["catalog_entries_added"]==0 and r["access_mode"]=="READ_ONLY_ON_DEMAND"
