"""Canonical responsibility taxonomy for GLOBAL VIDEO CORE ECOSYSTEM."""
from __future__ import annotations
from typing import Any

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "VIDEO_CAPTURE_AND_RECORDING": {"name": "Video Capture and Recording", "purpose": "Cameras, capture devices, screen recording and acquisition metadata."},
    "VIDEO_EDITING_AND_POST_PRODUCTION": {"name": "Video Editing and Post-production", "purpose": "Editing, compositing, effects, color, subtitles and post-production tools."},
    "ENCODING_TRANSCODING_AND_FORMATS": {"name": "Encoding, Transcoding and Formats", "purpose": "Codecs, containers, profiles, compression and transcoding metadata."},
    "VIDEO_HOSTING_AND_STORAGE": {"name": "Video Hosting and Storage", "purpose": "Video libraries, hosting, storage and asset lifecycle metadata."},
    "STREAMING_AND_DELIVERY": {"name": "Streaming and Delivery", "purpose": "On-demand delivery, adaptive streaming, CDN and playback metadata."},
    "LIVE_VIDEO_AND_BROADCAST": {"name": "Live Video and Broadcast", "purpose": "Live production, broadcasting, events and real-time video workflows."},
    "VIDEO_COMMUNICATION_AND_MEETINGS": {"name": "Video Communication and Meetings", "purpose": "Meetings, conferencing, webinars and collaboration."},
    "CREATOR_AND_SUBSCRIPTION_PLATFORMS": {"name": "Creator and Subscription Platforms", "purpose": "Creator profiles, subscriptions, memberships and lawful monetization."},
    "VIDEO_SHARING_AND_COMMUNITIES": {"name": "Video Sharing and Communities", "purpose": "Public video sharing, channels, discovery and community features."},
    "VIDEO_MARKETPLACES_AND_DISTRIBUTION": {"name": "Video Marketplaces and Distribution", "purpose": "Licensed distribution, storefronts, syndication and marketplaces."},
    "VIDEO_ANALYTICS_AND_MEASUREMENT": {"name": "Video Analytics and Measurement", "purpose": "Audience, playback, engagement, performance and measurement metadata."},
    "VIDEO_ADVERTISING_AND_MONETIZATION": {"name": "Video Advertising and Monetization", "purpose": "Advertising, revenue models, subscriptions and payout boundaries."},
    "VIDEO_MODERATION_AND_TRUST_SAFETY": {"name": "Video Moderation and Trust & Safety", "purpose": "Content review, age controls, reporting and abuse prevention."},
    "VIDEO_RIGHTS_LICENSING_AND_CONSENT": {"name": "Video Rights, Licensing and Consent", "purpose": "Copyright, licenses, performer consent and release metadata."},
    "VIDEO_ACCESSIBILITY_AND_LOCALIZATION": {"name": "Video Accessibility and Localization", "purpose": "Captions, transcripts, audio description, dubbing and localization."},
    "VIDEO_INFRASTRUCTURE_AND_PROCESSING": {"name": "Video Infrastructure and Processing", "purpose": "Compute, GPU processing, pipelines and delivery dependencies."},
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
