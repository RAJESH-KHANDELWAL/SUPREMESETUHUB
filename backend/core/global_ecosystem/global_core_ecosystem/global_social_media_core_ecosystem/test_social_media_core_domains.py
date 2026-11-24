"""Structural and behavior tests for Global Social Media Core packages."""
import importlib,json
from pathlib import Path
from .domain_catalog import DOMAIN_DEFINITIONS,social_media_domain_summary
from .product_catalog import get_social_media_product_index,list_social_media_platforms
from .manager import get_manager
ROOT=Path(__file__).parent
def test_platform_catalog_and_manifests_are_complete():
    index=get_social_media_product_index();items=index["platform_ecosystems"]
    assert index["platform_count"]==113 and len(items)==113
    assert len({x["platform_id"] for x in items})==113
    for item in items:
        package=ROOT/f'{item["platform_id"]}_social_media_core_ecosystem'
        manifest=json.loads((package/"ecosystem_manifest.json").read_text(encoding="utf-8"))
        assert manifest["platform_id"]==item["platform_id"] and manifest["core_path"]==item["core_path"]
        assert (package/"__init__.py").is_file()
def test_all_domain_packages_export_working_managers():
    prefix="backend.core.global_ecosystem.global_core_ecosystem.global_social_media_core_ecosystem"
    assert len(DOMAIN_DEFINITIONS)==14
    for key,definition in DOMAIN_DEFINITIONS.items():
        package=importlib.import_module(f'{prefix}.{definition["package_path"].split("/")[-1]}')
        manager=package.get_manager();assert manager.DOMAIN_ID==key and manager.status()["domain_id"]==key
def test_all_platform_packages_export_working_managers():
    prefix="backend.core.global_ecosystem.global_core_ecosystem.global_social_media_core_ecosystem"
    for item in get_social_media_product_index()["platform_ecosystems"]:
        package=importlib.import_module(f'{prefix}.{item["platform_id"]}_social_media_core_ecosystem')
        manager=package.get_manager();assert manager.status()["platform_id"]==item["platform_id"]
        assert manager.status()["live_connection_verified"] is False
def test_domain_assignments_cover_each_platform_exactly_once():
    summary=social_media_domain_summary();ids=[p for d in summary["domains"] for p in d["platform_ids"]]
    assert summary["domain_count"]==14 and summary["platform_count"]==113
    assert len(ids)==len(set(ids))==113
def test_adult_platforms_are_explicitly_age_classified():
    adults=list_social_media_platforms(adult_only=True)
    assert len(adults)==14 and all(x["age_classification"]=="ADULT_18_PLUS" for x in adults)
    assert all(x["live_connection_verified"] is False for x in adults)
def test_manager_inventory_is_metadata_only():
    status=get_manager().status();assert status["platform_count"]==113 and status["api_calls_performed"]==0
