"""Catalog operations for the company-specific module directory."""
from .registry import get_company_module, list_company_modules, search_company_modules, validate_company_module_registry


def list_catalog():
    return [item.__dict__ if hasattr(item, "__dict__") else {
        "company_id": item.company_id,
        "name": item.name,
        "package_path": item.package_path,
        "module_status": item.module_status,
        "profile_registry_status": item.profile_registry_status,
        "data_status": item.data_status,
    } for item in list_company_modules()]


def get_catalog_entry(company_id: str):
    item = get_company_module(company_id)
    if item is None:
        return None
    return {
        "company_id": item.company_id,
        "name": item.name,
        "package_path": item.package_path,
        "module_status": item.module_status,
        "profile_registry_status": item.profile_registry_status,
        "data_status": item.data_status,
    }


def search_catalog(query: str):
    return [
        {
            "company_id": item.company_id,
            "name": item.name,
            "package_path": item.package_path,
            "module_status": item.module_status,
            "profile_registry_status": item.profile_registry_status,
            "data_status": item.data_status,
        }
        for item in search_company_modules(query)
    ]


def get_catalog_metadata():
    integrity = validate_company_module_registry()
    return {
        "catalog_status": "module_index_only",
        "module_count": integrity["module_count"],
        "profile_records_included": False,
        "live_company_data_connected": False,
        "integrity": integrity,
    }
