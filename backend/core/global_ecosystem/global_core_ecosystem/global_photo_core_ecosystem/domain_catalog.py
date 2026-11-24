"""Canonical responsibility taxonomy for GLOBAL PHOTO CORE ECOSYSTEM."""
from __future__ import annotations
from typing import Any

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "PHOTOGRAPHY_AND_IMAGE_CAPTURE": {"name": "Photography and Image Capture", "purpose": "Cameras, mobile capture, lenses, capture workflows and image metadata."},
    "PHOTO_EDITING_AND_RETOUCHING": {"name": "Photo Editing and Retouching", "purpose": "RAW development, color, retouching, restoration and image correction."},
    "GRAPHIC_DESIGN_AND_COMPOSITION": {"name": "Graphic Design and Composition", "purpose": "Layouts, graphics, compositing, typography and visual design."},
    "IMAGE_FORMATS_AND_PROCESSING": {"name": "Image Formats and Processing", "purpose": "Raster/vector formats, conversion, compression, resizing and processing."},
    "PHOTO_STORAGE_AND_ASSET_MANAGEMENT": {"name": "Photo Storage and Asset Management", "purpose": "Libraries, albums, metadata, backups and digital asset management."},
    "PHOTO_SHARING_AND_COMMUNITIES": {"name": "Photo Sharing and Communities", "purpose": "Photo publishing, galleries, profiles, discovery and communities."},
    "STOCK_PHOTOGRAPHY_AND_MARKETPLACES": {"name": "Stock Photography and Marketplaces", "purpose": "Stock libraries, licensing marketplaces and contributor metadata."},
    "CREATOR_AND_PHOTOGRAPHY_BUSINESS": {"name": "Creator and Photography Business", "purpose": "Professional portfolios, client delivery, bookings and business workflows."},
    "PRINTING_AND_PHOTO_PRODUCTS": {"name": "Printing and Photo Products", "purpose": "Print labs, photo books, merchandise and physical photo products."},
    "IMAGE_SEARCH_AND_DISCOVERY": {"name": "Image Search and Discovery", "purpose": "Visual search, indexing, tagging and discovery metadata."},
    "AI_ASSISTED_IMAGE_WORKFLOWS": {"name": "AI-assisted Image Workflows", "purpose": "AI-assisted editing, enhancement, generation metadata and provenance."},
    "IMAGE_RIGHTS_LICENSING_AND_CONSENT": {"name": "Image Rights, Licensing and Consent", "purpose": "Copyright, model/property releases, usage rights and consent records."},
    "IMAGE_MODERATION_AND_TRUST_SAFETY": {"name": "Image Moderation and Trust & Safety", "purpose": "Age assurance, abuse reporting, privacy and non-consensual image prevention."},
    "ACCESSIBILITY_AND_IMAGE_METADATA": {"name": "Accessibility and Image Metadata", "purpose": "Alt text, captions, EXIF/IPTC metadata and localization."},
    "IMAGE_INFRASTRUCTURE_AND_DELIVERY": {"name": "Image Infrastructure and Delivery", "purpose": "Image CDN, transformations, APIs and delivery dependencies."},
}

def list_domains() -> list[dict[str, str]]:
    return [{"domain_id": key, **value} for key, value in DOMAIN_DEFINITIONS.items()]

def domain_summary() -> dict[str, Any]:
    from .catalog import PROVIDERS
    counts = {key: 0 for key in DOMAIN_DEFINITIONS}
    for provider in PROVIDERS:
        if provider["domain_id"] in counts:
            counts[provider["domain_id"]] += 1
    return {"success": True, "domain_count": len(DOMAIN_DEFINITIONS), "provider_count": len(PROVIDERS), "domains": [{**item, "provider_count": counts[item["domain_id"]]} for item in list_domains()], "live_connections_verified": 0}
