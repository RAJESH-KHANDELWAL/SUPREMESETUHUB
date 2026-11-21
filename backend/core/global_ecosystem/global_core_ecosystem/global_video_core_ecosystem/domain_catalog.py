"""Canonical responsibility taxonomy for GLOBAL VIDEO CORE ECOSYSTEM."""
from __future__ import annotations
from typing import Any

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    {"domain_id": "VIDEO_CAPTURE_AND_RECORDING", "name": "Video Capture and Recording", "purpose": "Cameras, capture devices, screen recording and acquisition metadata."},
    {"domain_id": "VIDEO_EDITING_AND_POST_PRODUCTION", "name": "Video Editing and Post-production", "purpose": "Editing, compositing, effects, color, subtitles and post-production tools."},
    {"domain_id": "ENCODING_TRANSCODING_AND_FORMATS", "name": "Encoding, Transcoding and Formats", "purpose": "Codecs, containers, profiles, compression and transcoding metadata."},
    {"domain_id": "VIDEO_HOSTING_AND_STORAGE", "name": "Video Hosting and Storage", "purpose": "Video libraries, hosting, storage and asset lifecycle metadata."},
    {"domain_id": "STREAMING_AND_DELIVERY", "name": "Streaming and Delivery", "purpose": "On-demand delivery, adaptive streaming, CDN and playback metadata."},
    {"domain_id": "LIVE_VIDEO_AND_BROADCAST", "name": "Live Video and Broadcast", "purpose": "Live production, broadcasting, events and real-time video workflows."},
    {"domain_id": "VIDEO_COMMUNICATION_AND_MEETINGS", "name": "Video Communication and Meetings", "purpose": "Meetings, conferencing, webinars and collaboration."},
    {"domain_id": "CREATOR_AND_SUBSCRIPTION_PLATFORMS", "name": "Creator and Subscription Platforms", "purpose": "Creator profiles, subscriptions, memberships and lawful monetization."},
    {"domain_id": "VIDEO_SHARING_AND_COMMUNITIES", "name": "Video Sharing and Communities", "purpose": "Public video sharing, channels, discovery and community features."},
    {"domain_id": "VIDEO_MARKETPLACES_AND_DISTRIBUTION", "name": "Video Marketplaces and Distribution", "purpose": "Licensed distribution, storefronts, syndication and marketplaces."},
    {"domain_id": "VIDEO_ANALYTICS_AND_MEASUREMENT", "name": "Video Analytics and Measurement", "purpose": "Audience, playback, engagement, performance and measurement metadata."},
    {"domain_id": "VIDEO_ADVERTISING_AND_MONETIZATION", "name": "Video Advertising and Monetization", "purpose": "Advertising, revenue models, subscriptions and payout boundaries."},
    {"domain_id": "VIDEO_MODERATION_AND_TRUST_SAFETY", "name": "Video Moderation and Trust & Safety", "purpose": "Content review, age controls, reporting and abuse prevention."},
    {"domain_id": "VIDEO_RIGHTS_LICENSING_AND_CONSENT", "name": "Video Rights, Licensing and Consent", "purpose": "Copyright, licenses, performer consent and release metadata."},
    {"domain_id": "VIDEO_ACCESSIBILITY_AND_LOCALIZATION", "name": "Video Accessibility and Localization", "purpose": "Captions, transcripts, audio description, dubbing and localization."},
    {"domain_id": "VIDEO_INFRASTRUCTURE_AND_PROCESSING", "name": "Video Infrastructure and Processing", "purpose": "Compute, GPU processing, pipelines and delivery dependencies."},
}

def list_domains() -> list[dict[str, str]]:
    return [{"domain_id": key, **value} for key, value in DOMAIN_DEFINITIONS.items()]

def domain_summary() -> dict[str, Any]:
    from .catalog import PROVIDERS
    counts = {key: 0 for key in DOMAIN_DEFINITIONS}
    for provider in PROVIDERS:
        if provider["domain_id"] in counts: counts[provider["domain_id"]] += 1
    return {"success": True, "domain_count": len(DOMAIN_DEFINITIONS), "provider_count": len(PROVIDERS), "domains": [{**item, "provider_count": counts[item["domain_id"]]} for item in list_domains()], "live_connections_verified": 0}
