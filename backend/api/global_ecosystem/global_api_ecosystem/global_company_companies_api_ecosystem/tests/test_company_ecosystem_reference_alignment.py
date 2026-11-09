"""Structural tests for Company Companies taxonomy architecture."""
from importlib import import_module
from ..classification_registry import list_record_classes, validate_record_class_registry
from ..domain_registry import list_domains, validate_domain_registry

def test_record_classes_are_company_enterprise_and_group_only():
    assert {x["record_type"] for x in list_record_classes()} == {"company", "enterprise", "corporate_group"}
    result = validate_record_class_registry()
    assert result["structurally_valid"] is True
    assert result["freelancer_is_company_record_class"] is False

def test_domain_registry_is_valid_and_company_specific():
    assert validate_domain_registry()["structurally_valid"] is True
    assert {x["record_type"] for x in list_domains()} == {"company", "enterprise", "corporate_group"}

def test_corporate_group_package_contract():
    package = import_module("..corporate_groups_api_ecosystem", package=__package__)
    assert package.DOMAIN_ID == "corporate_groups"
    assert len(package.SUBCATEGORY_IDS) == len(set(package.SUBCATEGORY_IDS))
    assert len(package.list_subcategories()) == len(package.SUBCATEGORY_IDS)
