"""Adobe ecosystem catalog; descriptive metadata, not a live Adobe API client."""

from __future__ import annotations

ADOBE_PRODUCTS = {
    "creative_cloud": "Creative Cloud account, app, sync and storage service catalog.",
    "photoshop": "Photoshop imaging, layers, masks, actions and generative workflow catalog.",
    "illustrator": "Illustrator vector design, artwork and export workflow catalog.",
    "premiere_pro": "Premiere Pro video editing, timelines, media and export workflow catalog.",
    "after_effects": "After Effects motion graphics, compositing and render workflow catalog.",
    "acrobat_pdf": "Acrobat, PDF creation, editing, forms, signatures and accessibility workflows.",
    "indesign": "InDesign page layout, publishing, preflight and print workflows.",
    "lightroom": "Lightroom photo library, editing, presets and delivery workflows.",
    "adobe_express": "Adobe Express templates, social content and quick design workflows.",
    "adobe_fonts": "Fonts, typography, licensing metadata and font activation workflows.",
    "adobe_stock": "Stock assets, licensing metadata, attribution and asset management workflows.",
    "substance_3d": "Substance 3D materials, assets, modeling and texture workflows.",
    "adobe_xd": "Adobe XD design files, prototypes and handoff catalog; availability must be verified.",
    "frame_io": "Frame.io review, comments, approvals and video collaboration workflows.",
    "collaboration": "Creative review, coediting, sharing, approvals and team handoff.",
    "firefly": "Firefly generative AI workflow metadata, provenance and usage policy checks.",
    "experience_cloud": "Adobe Experience Cloud product and enterprise workflow catalog.",
    "commerce": "Adobe Commerce catalog, storefront, checkout and integration metadata.",
    "analytics": "Adobe Analytics reporting, event taxonomy and measurement workflow catalog.",
    "marketo": "Marketo Engage campaign, lead lifecycle and consent-aware automation catalog.",
    "aem": "Adobe Experience Manager content, assets, sites and publishing workflow catalog.",
    "admin_console": "Enterprise Admin Console users, groups, products and license assignment metadata.",
    "identity_and_access": "Adobe identity federation, SSO, provisioning and access review metadata.",
    "licensing_and_entitlements": "Plans, entitlements, seats, renewals and usage governance.",
    "developer_platform": "Adobe developer projects, OAuth scopes, APIs, webhooks and integration registry.",
    "automation_and_workflows": "Cross-product creative workflow orchestration specifications.",
    "assets_and_dam": "Digital asset management, metadata, rights, versions and retention workflows.",
    "publishing_and_delivery": "Export, packaging, publishing, distribution and delivery workflows.",
    "accessibility": "Accessible documents, captions, contrast, keyboard workflows and validation.",
    "localization": "India-to-global language, locale, script and regional publishing metadata.",
    "security_and_compliance": "Data protection, security controls, privacy and compliance mapping.",
    "regional": "Regional product availability, language and compliance metadata.",
}

MATURITY_LEVELS = ("basic", "standard", "professional", "enterprise", "supreme")
REGIONS = ("India", "Global")


def list_products() -> list[dict[str, str]]:
    """Return stable product/domain descriptors for discovery."""
    return [
        {"key": key, "description": description}
        for key, description in sorted(ADOBE_PRODUCTS.items())
    ]


def get_product(key: str) -> dict[str, str] | None:
    """Look up one product domain by its canonical key."""
    description = ADOBE_PRODUCTS.get(key.strip().lower())
    if description is None:
        return None
    return {"key": key.strip().lower(), "description": description}
