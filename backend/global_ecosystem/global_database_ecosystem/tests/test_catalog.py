"""Offline tests for global database ecosystem taxonomy."""
from global_database_ecosystem.catalog import (
    MATURITY_LEVELS, WORKLOADS, get_database_ecosystem_catalog,
    validate_database_ecosystem_catalog,
)
from global_database_ecosystem.classification import classify_workload
from global_database_ecosystem.platforms import find_platforms

def test_catalog_is_global_and_covers_india():
    catalog = get_database_ecosystem_catalog()
    assert "bharat" in catalog["regions"]
    assert "global" in catalog["regions"]
    assert MATURITY_LEVELS[0] == "normal"
    assert MATURITY_LEVELS[-1] == "supreme"

def test_adult_workloads_are_lawful_and_safeguarded():
    result = classify_workload("adult_and_sexual_content")
    assert "adult_creator_accounts" in result["workloads"]
    assert "required_guardrails" in result
    assert "consent" in result["required_guardrails"]
    assert "safety" in result["required_guardrails"]

def test_database_catalog_has_multiple_models():
    models = {item["model"] for item in find_platforms()}
    assert {"relational_sql", "document_nosql", "graph", "vector_and_ai_data"} <= models

def test_taxonomy_validation():
    assert validate_database_ecosystem_catalog() == ()
    assert WORKLOADS["adult_and_sexual_content"]
