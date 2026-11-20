"""Structural and behavior tests for the Google Core domain packages."""
from __future__ import annotations

import importlib

from .domain_catalog import DOMAIN_DEFINITIONS, google_domain_summary
from .domain_runtime import GoogleCoreDomainManager


DOMAIN_PACKAGES = {
    "PROVIDER_GOVERNANCE": "provider_governance",
    "IDENTITY_ACCESS_AND_ADMIN": "identity_access",
    "WORKSPACE_AND_COLLABORATION": "workspace_collaboration",
    "CLOUD_INFRASTRUCTURE_AND_NETWORK": "cloud_infrastructure",
    "STORAGE_DATABASE_AND_DATA": "storage_database",
    "AI_ML_AND_INTELLIGENCE": "ai_machine_learning",
    "ANALYTICS_AND_OBSERVABILITY": "analytics_observability",
    "MAPS_GEOSPATIAL_AND_TRAVEL": "maps_geospatial",
    "DEVELOPER_AND_APPLICATION_PLATFORM": "developer_platform",
    "ANDROID_AND_MOBILE": "android_mobile",
    "SECURITY_PRIVACY_AND_COMPLIANCE": "security_privacy",
    "ADVERTISING_COMMERCE_AND_MONETIZATION": "advertising_commerce",
    "SEARCH_PUBLISHING_AND_DISCOVERY": "search_publishing",
    "MEDIA_VIDEO_AND_AUDIO": "media_video_audio",
    "BUSINESS_EDUCATION_AND_LOCAL": "business_education",
    "PAYMENTS_WALLET_AND_SUBSCRIPTIONS": "payments_wallet",
    "CONSUMER_DEVICES_AND_SMART_HOME": "devices_smart_home",
    "LANGUAGE_ACCESSIBILITY_AND_PRODUCTIVITY": "language_accessibility",
    "SPECIALTY_AND_CROSS_PRODUCT": "specialty_services",
}


def test_all_nineteen_domain_packages_are_registered():
    assert len(DOMAIN_DEFINITIONS) == 19
    assert len(DOMAIN_PACKAGES) == 19
    assert set(DOMAIN_PACKAGES) == set(DOMAIN_DEFINITIONS)


def test_each_domain_package_exports_a_working_manager():
    for domain_id, package_name in DOMAIN_PACKAGES.items():
        package = importlib.import_module(f".{package_name}", package=__package__)
        manager = package.get_manager()
        assert manager.DOMAIN_ID == domain_id
        assert manager.status()["domain_id"] == domain_id
        assert manager.list_offerings()["success"] is True


def test_domain_offerings_match_the_canonical_inventory():
    summary = google_domain_summary()
    assert summary["domain_count"] == 19
    for domain in summary["domains"]:
        manager = GoogleCoreDomainManagerForTest(domain["domain_id"])
        assert manager.list_offerings()["count"] == domain["offering_count"]


class GoogleCoreDomainManagerForTest(GoogleCoreDomainManager):
    def __init__(self, domain_id: str) -> None:
        self.DOMAIN_ID = domain_id
        super().__init__()
