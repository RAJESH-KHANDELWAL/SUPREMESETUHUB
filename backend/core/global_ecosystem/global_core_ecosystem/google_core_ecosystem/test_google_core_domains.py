"""Structural and behavior tests for the Google Core domain packages."""
from __future__ import annotations

import importlib

from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.domain_catalog import (
    DOMAIN_DEFINITIONS,
    google_domain_summary,
)
from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.domain_runtime import (
    GoogleCoreDomainManager,
)

DOMAIN_PACKAGES = {
    "PROVIDER_GOVERNANCE": "google_provider_governance_core_ecosystem",
    "IDENTITY_ACCESS_AND_ADMIN": "google_identity_access_core_ecosystem",
    "WORKSPACE_AND_COLLABORATION": "google_workspace_collaboration_core_ecosystem",
    "CLOUD_INFRASTRUCTURE_AND_NETWORK": "google_cloud_infrastructure_core_ecosystem",
    "STORAGE_DATABASE_AND_DATA": "google_storage_database_core_ecosystem",
    "AI_ML_AND_INTELLIGENCE": "google_ai_machine_learning_core_ecosystem",
    "ANALYTICS_AND_OBSERVABILITY": "google_analytics_observability_core_ecosystem",
    "MAPS_GEOSPATIAL_AND_TRAVEL": "google_maps_geospatial_core_ecosystem",
    "DEVELOPER_AND_APPLICATION_PLATFORM": "google_developer_platform_core_ecosystem",
    "ANDROID_AND_MOBILE": "google_android_mobile_core_ecosystem",
    "SECURITY_PRIVACY_AND_COMPLIANCE": "google_security_privacy_core_ecosystem",
    "ADVERTISING_COMMERCE_AND_MONETIZATION": "google_advertising_commerce_core_ecosystem",
    "SEARCH_PUBLISHING_AND_DISCOVERY": "google_search_publishing_core_ecosystem",
    "MEDIA_VIDEO_AND_AUDIO": "google_media_video_audio_core_ecosystem",
    "BUSINESS_EDUCATION_AND_LOCAL": "google_business_education_core_ecosystem",
    "PAYMENTS_WALLET_AND_SUBSCRIPTIONS": "google_payments_wallet_core_ecosystem",
    "CONSUMER_DEVICES_AND_SMART_HOME": "google_devices_smart_home_core_ecosystem",
    "LANGUAGE_ACCESSIBILITY_AND_PRODUCTIVITY": "google_language_accessibility_core_ecosystem",
    "SPECIALTY_AND_CROSS_PRODUCT": "google_specialty_services_core_ecosystem",
}


def test_all_nineteen_domain_packages_are_registered():
    assert len(DOMAIN_DEFINITIONS) == 19
    assert len(DOMAIN_PACKAGES) == 19
    assert set(DOMAIN_PACKAGES) == set(DOMAIN_DEFINITIONS)


def test_each_domain_package_exports_a_working_manager():
    package_root = (
        "backend.core.global_ecosystem.global_core_ecosystem."
        "google_core_ecosystem"
    )
    for domain_id, package_name in DOMAIN_PACKAGES.items():
        package = importlib.import_module(f"{package_root}.{package_name}")
        manager = package.get_manager()
        assert manager.DOMAIN_ID == domain_id
        assert manager.status()["domain_id"] == domain_id
        assert manager.list_offerings()["success"] is True


def test_domain_offerings_match_the_canonical_inventory():
    summary = google_domain_summary()
    assert summary["domain_count"] == 19
    for domain in summary["domains"]:
        manager = GoogleCoreDomainManager(domain["domain_id"])
        assert manager.list_offerings()["count"] == domain["offering_count"]
