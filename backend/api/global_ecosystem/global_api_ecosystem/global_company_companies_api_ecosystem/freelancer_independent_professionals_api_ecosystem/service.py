"""Category facade over the shared parent registry; no duplicated profile storage."""
from ..service import get_company, search_companies
from .catalog import CATEGORY, RECORD_TYPE
def list_profiles(q=None, country=None, industry=None, limit=50, offset=0):
    return search_companies(q=q, country=country, industry=industry, limit=limit, offset=offset, category=RECORD_TYPE)
def search_profiles(q=None, country=None, industry=None, limit=50, offset=0):
    return list_profiles(q=q, country=country, industry=industry, limit=limit, offset=offset)
def get_profile(profile_id):
    record = get_company(profile_id)
    return record if record is not None and record.get("record_type") == RECORD_TYPE else None
def get_catalog():
    return dict(CATEGORY)
