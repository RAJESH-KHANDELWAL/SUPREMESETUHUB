"""Canonical Adobe Core inventory derived from the existing Adobe runtime catalog.

This is descriptive Core metadata. It does not create product packages, perform
provider API calls, or imply API entitlement or live connectivity.
"""
from __future__ import annotations

from typing import Any

_SOURCE = (
    ("creative_cloud", "Adobe Creative Cloud", "Creative Cloud account, app, sync and storage service catalog."),
    ("photoshop", "Adobe Photoshop", "Imaging, layers, masks, actions and generative workflow catalog."),
    ("illustrator", "Adobe Illustrator", "Vector design, artwork and export workflow catalog."),
    ("premiere_pro", "Adobe Premiere Pro", "Video editing, timelines, media and export workflow catalog."),
    ("after_effects", "Adobe After Effects", "Motion graphics, compositing and render workflow catalog."),
    ("acrobat_pdf", "Adobe Acrobat and PDF", "PDF creation, editing, forms, signatures and accessibility workflows."),
    ("indesign", "Adobe InDesign", "Page layout, publishing, preflight and print workflows."),
    ("lightroom", "Adobe Lightroom", "Photo library, editing, presets and delivery workflows."),
    ("adobe_express", "Adobe Express", "Templates, social content and quick design workflows."),
    ("adobe_fonts", "Adobe Fonts", "Typography, licensing metadata and font activation workflows."),
    ("adobe_stock", "Adobe Stock", "Stock assets, licensing metadata, attribution and asset management."),
    ("substance_3d", "Substance 3D", "Materials, assets, modeling and texture workflows."),
    ("adobe_xd", "Adobe XD", "Design files, prototypes and handoff catalog; availability requires verification."),
    ("frame_io", "Frame.io", "Review, comments, approvals and video collaboration workflows."),
    ("collaboration", "Adobe Collaboration", "Creative review, coediting, sharing, approvals and team handoff."),
    ("firefly", "Adobe Firefly", "Generative AI workflow metadata, provenance and usage policy checks."),
    ("experience_cloud", "Adobe Experience Cloud", "Product and enterprise workflow catalog."),
    ("commerce", "Adobe Commerce", "Catalog, storefront, checkout and integration metadata."),
    ("analytics", "Adobe Analytics", "Reporting, event taxonomy and measurement workflow catalog."),
    ("marketo", "Marketo Engage", "Campaign, lead lifecycle and consent-aware automation catalog."),
    ("aem", "Adobe Experience Manager", "Content, assets, sites and publishing workflow catalog."),
    ("admin_console", "Adobe Admin Console", "Users, groups, products and license assignment metadata."),
    ("identity_and_access", "Adobe Identity and Access", "Identity federation, SSO, provisioning and access review metadata."),
    ("licensing_and_entitlements", "Adobe Licensing and Entitlements", "Plans, entitlements, seats, renewals and usage governance."),
    ("developer_platform", "Adobe Developer Platform", "Developer projects, OAuth scopes, APIs, webhooks and integration registry."),
    ("automation_and_workflows", "Adobe Automation and Workflows", "Cross-product creative workflow orchestration specifications."),
    ("assets_and_dam", "Adobe Assets and DAM", "Digital asset management, metadata, rights, versions and retention workflows."),
    ("publishing_and_delivery", "Adobe Publishing and Delivery", "Export, packaging, publishing, distribution and delivery workflows."),
    ("accessibility", "Adobe Accessibility", "Accessible documents, captions, contrast, keyboard workflows and validation."),
    ("localization", "Adobe Localization", "Language, locale, script and regional publishing metadata."),
    ("security_and_compliance", "Adobe Security and Compliance", "Data protection, security controls, privacy and compliance mapping."),
    ("regional", "Adobe Regional Services", "Regional product availability, language and compliance metadata."),
)

def get_adobe_core_catalog() -> dict[str, Any]:
    children = []
    for key, name, description in _SOURCE:
        ecosystem_id = f"ADOBE-{key.upper().replace('_', '-')}-CORE-ECOSYSTEM"
        children.append({
            "ecosystem_id": ecosystem_id,
            "name": name,
            "product_key": key,
            "description": description,
            "core_module": f"adobe_{key}_core_ecosystem",
            "api_catalog_ref": f"backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/{key}",
            "capabilities": [],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "package_scaffolded": key == "creative_cloud",
            "live_connection_verified": False,
        })
    return {
        "ecosystem_id": "ADOBE-CORE-ECOSYSTEM",
        "name": "ADOBE CORE ECOSYSTEM",
        "provider": "adobe",
        "status": "CORE_CATALOG_AVAILABLE",
        "source_catalog": "backend/global_ecosystem/adobe_ecosystem/catalog.py",
        "product_domain_count": len(children),
        "package_scaffolded_count": sum(item["package_scaffolded"] for item in children),
        "live_connections_verified": 0,
        "children": children,
    }
