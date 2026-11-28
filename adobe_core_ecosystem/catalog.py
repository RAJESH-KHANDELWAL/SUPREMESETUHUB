"""Canonical Adobe Core inventory derived from the Adobe runtime catalog."""
from __future__ import annotations
from typing import Any

_SOURCE = (
    ("creative_cloud", "Adobe Creative Cloud", "Creative apps, shared libraries, collaboration and cloud services."),
    ("photoshop", "Adobe Photoshop", "Raster imaging, compositing, generative edits and export workflows."),
    ("illustrator", "Adobe Illustrator", "Vector illustration, typography and artwork workflows."),
    ("premiere_pro", "Adobe Premiere Pro", "Video editing, timelines, captions and delivery workflows."),
    ("after_effects", "Adobe After Effects", "Motion graphics, compositing and rendering workflows."),
    ("acrobat_pdf", "Adobe Acrobat and PDF", "PDF authoring, editing, conversion, accessibility and document workflows."),
    ("indesign", "Adobe InDesign", "Page layout, preflight, publishing and print production."),
    ("lightroom", "Adobe Lightroom", "Photo organization, editing, presets, sync and delivery."),
    ("adobe_express", "Adobe Express", "Template-based design, social content and quick creation."),
    ("adobe_fonts", "Adobe Fonts", "Font discovery, activation, licensing metadata and typography."),
    ("adobe_stock", "Adobe Stock", "Stock asset discovery, licensing, attribution and management."),
    ("substance_3d", "Adobe Substance 3D", "3D material authoring, painting, modeling, staging and rendering."),
    ("adobe_xd", "Adobe XD", "UX design, prototypes and handoff; lifecycle requires verification."),
    ("frame_io", "Frame.io", "Media collaboration, review, comments and approvals."),
    ("collaboration", "Adobe Collaboration", "Cross-product sharing, coediting, review and approvals."),
    ("firefly", "Adobe Firefly", "Generative AI capabilities, model metadata and usage policy."),
    ("experience_cloud", "Adobe Experience Cloud", "Enterprise customer experience, data, content and journeys."),
    ("commerce", "Adobe Commerce", "B2B/B2C catalog, storefront, checkout and operations."),
    ("analytics", "Adobe Analytics", "Digital analytics, event taxonomies, reporting and measurement."),
    ("marketo", "Marketo Engage", "Lead management, account-based marketing and campaign automation."),
    ("aem", "Adobe Experience Manager", "Sites, assets, forms, guides, content and publishing."),
    ("admin_console", "Adobe Admin Console", "Enterprise users, groups, product profiles and administration."),
    ("identity_and_access", "Adobe Identity and Access", "Identity federation, SSO, provisioning and access reviews."),
    ("licensing_and_entitlements", "Adobe Licensing and Entitlements", "Plans, seats, usage, renewals and license governance."),
    ("developer_platform", "Adobe Developer Platform", "Developer projects, API products, OAuth scopes and webhooks."),
    ("automation_and_workflows", "Adobe Automation and Workflows", "Cross-product workflow definitions and orchestration."),
    ("assets_and_dam", "Adobe Assets and DAM", "Asset metadata, rights, versions, renditions and retention."),
    ("publishing_and_delivery", "Adobe Publishing and Delivery", "Export, packaging, publishing, distribution and delivery."),
    ("accessibility", "Adobe Accessibility", "Accessible documents, captions, contrast and validation."),
    ("localization", "Adobe Localization", "Locales, languages, scripts, translation and regional publishing."),
    ("security_and_compliance", "Adobe Security and Compliance", "Security, privacy, governance, audit and compliance."),
    ("regional", "Adobe Regional Services", "Regional availability, language and data residency metadata."),
)
_MODULE_OVERRIDES = {
    "creative_cloud":"adobe_creative_cloud_core_ecosystem",
    "acrobat_pdf":"adobe_pdf_services_core_ecosystem",
    "frame_io":"adobe_video_frameio_core_ecosystem",
    "firefly":"adobe_firefly_services_core_ecosystem",
    "experience_cloud":"adobe_experience_platform_core_ecosystem",
    "commerce":"adobe_commerce_core_ecosystem",
    "identity_and_access":"adobe_oauth_identity_core_ecosystem",
    "assets_and_dam":"adobe_creative_cloud_assets_core_ecosystem",
}

def get_adobe_core_catalog() -> dict[str, Any]:
    children=[]
    for key,name,description in _SOURCE:
        module=_MODULE_OVERRIDES.get(key, f"adobe_{key.removeprefix('adobe_')}_core_ecosystem")
        api_family_map = {
            "acrobat_pdf": ("adobe_pdf_services_api_ecosystem",),
            "frame_io": ("adobe_video_frameio_api_ecosystem",),
            "firefly": ("adobe_firefly_services_api_ecosystem",),
            "experience_cloud": ("adobe_experience_platform_api_ecosystem",),
            "analytics": ("adobe_experience_platform_api_ecosystem",),
            "marketo": ("adobe_experience_platform_api_ecosystem",),
            "aem": ("adobe_experience_platform_api_ecosystem",),
            "commerce": ("adobe_commerce_api_ecosystem",),
            "assets_and_dam": ("adobe_creative_cloud_assets_api_ecosystem",),
            "creative_cloud": ("adobe_creative_cloud_assets_api_ecosystem",),
            "identity_and_access": ("adobe_oauth_identity_ecosystem",),
        }
        api_families = api_family_map.get(key, ())
        api_refs = [f"backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/{family}" for family in api_families]
        children.append({"ecosystem_id":f"ADOBE-{key.upper().replace('_','-')}-CORE-ECOSYSTEM","name":name,"product_key":key,"description":description,"core_module":module,"api_catalog_refs":api_refs,"api_catalog_ref":api_refs[0] if api_refs else None,"api_mapping_status":"FAMILY_CATALOG_MAPPED_NOT_ENTITLEMENT_VERIFIED" if api_refs else "NO_DIRECT_API_FAMILY_MAPPED","capabilities":[],"status":"CORE_SCAFFOLDED","enabled":True,"package_scaffolded":True,"live_connection_verified":False})
    return {"ecosystem_id":"ADOBE-CORE-ECOSYSTEM","name":"ADOBE CORE ECOSYSTEM","provider":"adobe","status":"CORE_CATALOG_AVAILABLE","source_catalog":"backend/global_ecosystem/adobe_ecosystem/catalog.py","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem","product_domain_count":len(children),"package_scaffolded_count":len(children),"live_connections_verified":0,"children":children}
