"""Industry catalogue operations."""
from .registry import get_industry,list_industries,search_industries,validate_industry_registry
def list_catalog(): return list_industries()
def get_catalog_entry(industry_id): return get_industry(industry_id)
def search_catalog(query): return search_industries(query)
def get_catalog_metadata(): return validate_industry_registry()
