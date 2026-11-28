"""Unified GitHub family inventory."""
from .catalog import list_github_families
def list_github_offerings(): return list_github_families()
def get_github_offering(family):
 needle=str(family).strip().casefold()
 return next((x for x in list_github_families() if x["family"].casefold()==needle),None)
def github_offerings_summary():
 items=list_github_families(); return {"provider":"github","family_count":len(items),"families":[x["family"] for x in items]}
