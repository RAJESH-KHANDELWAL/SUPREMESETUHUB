"""Structural and behavior tests for the Kamasutra Core ecosystem."""
from __future__ import annotations

import importlib
from pathlib import Path

from .catalog import list_products
from .domain_catalog import DOMAINS, list_domains
from .manager import get_manager
from .policy import get_policy

DOMAIN_PACKAGES = {
    "RELATIONSHIPS_AND_COMPATIBILITY": "global_relationships_compatibility_core_ecosystem",
    "SEXUAL_EDUCATION_AND_TRADITIONAL_KNOWLEDGE": "global_sexual_education_traditional_knowledge_core_ecosystem",
    "HEALTHCARE_AND_RESEARCH": "global_sexual_reproductive_healthcare_research_core_ecosystem",
    "COACHING_AND_COUNSELLING": "global_relationship_intimacy_coaching_counselling_core_ecosystem",
    "ADULT_MEDIA_AND_CREATOR_ECONOMY": "global_adult_media_creator_economy_core_ecosystem",
    "BUSINESS_WORK_AND_TRAINING": "global_adult_business_work_training_core_ecosystem",
    "COMMERCE_AND_MARKETPLACES": "global_adult_wellness_commerce_marketplace_core_ecosystem",
    "TECHNOLOGY_AND_INFRASTRUCTURE": "global_adult_technology_infrastructure_core_ecosystem",
    "LAW_SAFETY_AND_COMPLIANCE": "global_adult_law_safety_compliance_core_ecosystem",
    "PAYMENTS_AND_BILLING": "global_adult_payments_billing_core_ecosystem",
    "ADVERTISING_AND_DISTRIBUTION": "global_adult_advertising_distribution_core_ecosystem",
    "GLOBAL_AND_REGIONAL_GOVERNANCE": "global_adult_wellness_governance_partnerships_core_ecosystem"
}

def test_all_registered_products_are_unique_and_enabled() -> None:
    products = list_products()
    ids = [item["ecosystem_id"] for item in products]
    assert len(products) == 62
    assert len(set(ids)) == 62
    assert all(item["enabled"] is True for item in products)
    assert all(item["connected"] is False for item in products)

def test_every_existing_product_folder_is_in_the_catalog() -> None:
    root = Path(__file__).parent
    domain_folders = set(DOMAIN_PACKAGES.values())
    actual_product_folders = {
        item.name for item in root.iterdir()
        if item.is_dir() and item.name not in domain_folders
    }
    catalog_product_folders = {item["package_name"] for item in list_products()}
    assert actual_product_folders == catalog_product_folders

def test_every_domain_package_exposes_a_working_manager() -> None:
    package_root = __package__
    assert len(DOMAINS) == 12
    assert set(DOMAIN_PACKAGES) == set(DOMAINS)
    for domain_id, package_name in DOMAIN_PACKAGES.items():
        package = importlib.import_module(f"{package_root}.{package_name}")
        manager = package.get_manager()
        status = manager.status()
        assert status["domain_id"] == domain_id
        assert status["connected"] is False
        assert len(manager.list_products()) == len(DOMAINS[domain_id]["product_ids"])

def test_all_62_products_are_classified_once() -> None:
    ids = [product_id for domain in list_domains() for product_id in domain["product_ids"]]
    assert len(ids) == 62
    assert len(set(ids)) == 62
    assert set(ids) == {item["ecosystem_id"] for item in list_products()}

def test_root_manager_reports_complete_inventory() -> None:
    manager = get_manager()
    assert manager.status()["status"] == "CATALOG_ONLY"
    assert manager.inventory()["registered_package_count"] == 62
    assert manager.health()["connected"] is False

def test_adult_safety_policy_is_explicit() -> None:
    policy = get_policy()
    assert policy["adult_only"] is True
    assert policy["minimum_age"] == 18
    assert policy["age_assurance_required"] is True
    assert policy["informed_consent_required"] is True
    assert policy["non_consensual_intimate_content_prohibited"] is True
    assert policy["minors_and_child_sexual_abuse_material_prohibited"] is True
