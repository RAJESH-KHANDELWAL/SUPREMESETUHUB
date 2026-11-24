"""Offline tests for GLOBAL APP taxonomy."""
from ..ecosystem_taxonomy import load_taxonomy,list_ecosystems,find_ecosystem
def test_group_count_and_category_count():
 data=load_taxonomy();rows=list_ecosystems()
 assert data["provider"]=="GLOBAL_APP"
 assert len(data["groups"])==18
 assert len(rows)==184
 assert all(row["name"].startswith("GLOBAL_APP_") and row["name"].endswith("_STORAGE_ECOSYSTEM") for row in rows)
def test_lookup():
 assert find_ecosystem("GMAIL") is not None
 assert find_ecosystem("DRIVE") is not None
