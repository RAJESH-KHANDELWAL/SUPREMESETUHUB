"""Canonical catalog for Adobe provider storage ecosystems.

API clients, OAuth and endpoint operations remain owned by Adobe API Ecosystem.
This module records storage-side child ecosystems without claiming live connectivity.
"""
from __future__ import annotations

ADOBE_STORAGE_ECOSYSTEM = {
    "provider_id": "adobe",
    "name": "ADOBE STORAGE ECOSYSTEM",
    "status": "CATALOG_AND_READINESS_FOUNDATION",
    "live_connection_verified": False,
    "api_ecosystem": "backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem",
    "children": [
        {"id": "cloud_storage_and_collaboration", "name": "Adobe Cloud Storage and Collaboration", "folder": "adobe_cloud_storage_and_collaboration_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
        {"id": "creative_cloud", "name": "Adobe Creative Cloud Storage", "folder": "adobe_creative_cloud_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
        {"id": "creative_cloud_assets", "name": "Adobe Creative Cloud Assets Storage", "folder": "adobe_creative_cloud_assets_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
        {"id": "lightroom", "name": "Adobe Lightroom Storage", "folder": "adobe_lightroom_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
        {"id": "express", "name": "Adobe Express Storage", "folder": "adobe_express_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
        {"id": "frameio", "name": "Adobe Frame.io Storage", "folder": "adobe_frameio_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
        {"id": "experience_manager_assets", "name": "Adobe Experience Manager Assets Storage", "folder": "adobe_experience_manager_assets_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
        {"id": "workfront", "name": "Adobe Workfront Storage", "folder": "adobe_workfront_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
        {"id": "document_cloud", "name": "Adobe Document Cloud Storage", "folder": "adobe_document_cloud_storage_ecosystem", "status": "FOUNDATION_INITIALIZED"},
    ],
}


def list_adobe_storage_ecosystems() -> list[dict[str, str]]:
    """Return copies of child catalog records."""
    return [dict(item) for item in ADOBE_STORAGE_ECOSYSTEM["children"]]


PROVIDER_STORAGE_ECOSYSTEM = ADOBE_STORAGE_ECOSYSTEM
__all__ = ["ADOBE_STORAGE_ECOSYSTEM", "PROVIDER_STORAGE_ECOSYSTEM", "list_adobe_storage_ecosystems"]
