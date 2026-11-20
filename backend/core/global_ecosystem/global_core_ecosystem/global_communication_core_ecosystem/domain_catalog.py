"""Communication Core domain taxonomy; metadata only, not live delivery."""
from __future__ import annotations
from typing import Any

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "PROVIDER_GOVERNANCE": {"name": "Provider Governance", "purpose": "Provider identity, directory classification, lifecycle and readiness."},
    "EMAIL_AND_DELIVERY": {"name": "Email and Delivery", "purpose": "Email provider metadata, delivery capability and sender policy boundaries."},
    "MESSAGING_AND_CHAT": {"name": "Messaging and Chat", "purpose": "Person-to-person, team and business messaging capability metadata."},
    "VOICE_AND_TELEPHONY": {"name": "Voice and Telephony", "purpose": "Voice, phone-number and telephony provider metadata."},
    "VIDEO_AND_MEETINGS": {"name": "Video and Meetings", "purpose": "Video meetings, conferencing and real-time session metadata."},
    "COMMUNICATION_APIS": {"name": "Communication APIs", "purpose": "API-based messaging, email, voice and notification service classification."},
    "NOTIFICATIONS_AND_EVENTS": {"name": "Notifications and Events", "purpose": "Notification channels, delivery events and status metadata."},
    "WORKSPACE_AND_COLLABORATION": {"name": "Workspace and Collaboration", "purpose": "Collaboration suites, team workspaces and productivity communications."},
    "INDIA_COMMUNICATION": {"name": "India Communication", "purpose": "India-specific provider discovery and regulatory review boundaries."},
    "PRIVACY_SECURITY_AND_COMPLIANCE": {"name": "Privacy, Security and Compliance", "purpose": "Data minimization, access control, retention, audit and compliance metadata."},
    "TRUST_SAFETY_AND_MODERATION": {"name": "Trust, Safety and Moderation", "purpose": "Abuse prevention, reporting, moderation and user safety controls."},
    "AGE_CONSENT_AND_RESTRICTED_SERVICES": {"name": "Age, Consent and Restricted Services", "purpose": "Age gating, consent, lawful-content boundaries and restricted-service review."},
    "RELATIONSHIPS_AND_WELLNESS_EDUCATION": {"name": "Relationships and Wellness Education", "purpose": "Educational and support taxonomy with privacy and safeguarding boundaries."},
}
def list_domains() -> list[dict[str, Any]]:
    return [{"domain_id": key, **value} for key, value in DOMAIN_DEFINITIONS.items()]
__all__ = ["DOMAIN_DEFINITIONS", "list_domains"]
