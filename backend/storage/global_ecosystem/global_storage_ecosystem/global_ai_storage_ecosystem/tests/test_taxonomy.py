"""Offline tests for grouped GLOBAL AI taxonomy."""
from ..ecosystem_taxonomy import load_taxonomy,list_ecosystems,find_ecosystem
def test_grouped_taxonomy_and_names():
    data=load_taxonomy(); assert data["provider"]=="GLOBAL_AI"
    rows=list_ecosystems(); assert len(rows)==13
    assert all(row["name"].startswith("GLOBAL_AI_") and row["name"].endswith("_STORAGE_ECOSYSTEM") for row in rows)
def test_category_lookup():
    assert find_ecosystem("MODEL_ARTIFACTS") is not None
    assert find_ecosystem("GOVERNANCE_AND_AUDIT") is not None
