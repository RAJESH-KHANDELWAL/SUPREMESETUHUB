"""Global communication domain taxonomy."""
from __future__ import annotations
from typing import Any

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "PROVIDER_GOVERNANCE": {"name": "Provider Governance", "purpose": "Provider identity, ownership, lifecycle, geography, status and source verification."},
    "TELECOMMUNICATIONS_NETWORKS": {"name": "Telecommunications Networks", "purpose": "Mobile, fixed-line, broadband, carrier, satellite and enterprise connectivity operators."},
    "EMAIL_SERVICES": {"name": "Email Services", "purpose": "Consumer email, hosted business email, mail protocols and mailbox services."},
    "EMAIL_DELIVERY_MARKETING": {"name": "Email Delivery and Marketing", "purpose": "Transactional email, bulk delivery, campaigns, deliverability and sender reputation."},
    "OTT_MESSAGING": {"name": "OTT and Instant Messaging", "purpose": "Consumer messaging applications, channels, groups, bots and encrypted messaging."},
    "SMS_MMS_RCS": {"name": "SMS MMS and RCS", "purpose": "Person-to-person and application-to-person messaging, rich messaging and carrier interconnect."},
    "SOCIAL_MESSAGING": {"name": "Social Messaging", "purpose": "Messaging embedded in social networks and creator/community platforms."},
    "VOICE_TELEPHONY_VOIP": {"name": "Voice Telephony and VoIP", "purpose": "PSTN, VoIP, SIP, DID, toll-free numbers, voicemail and call routing."},
    "VIDEO_CONFERENCING": {"name": "Video Conferencing", "purpose": "Meetings, webinars, video rooms, conferencing and real-time media."},
    "UCaaS_COLLABORATION": {"name": "Unified Communications and Collaboration", "purpose": "Enterprise chat, presence, meetings, calling and workplace collaboration."},
    "CPaaS_COMMUNICATION_APIS": {"name": "CPaaS and Communication APIs", "purpose": "Programmable messaging, voice, video, number provisioning, verification and SDKs."},
    "CCaaS_CONTACT_CENTERS": {"name": "CCaaS and Contact Centers", "purpose": "Inbound/outbound contact centers, IVR, agent desktop, queues and workforce tools."},
    "CUSTOMER_ENGAGEMENT_CRM": {"name": "Customer Engagement and CRM Communication", "purpose": "Customer journeys, support messaging, CRM-connected conversations and engagement."},
    "PUSH_NOTIFICATIONS": {"name": "Push Notifications", "purpose": "Mobile/web push, in-app messaging, delivery receipts and notification preferences."},
    "REALTIME_COMMUNICATION_SDKS": {"name": "Real-time Communication SDKs", "purpose": "RTC infrastructure, media servers, chat SDKs, streaming and embedded communication."},
    "WEBINARS_LIVE_STREAMING": {"name": "Webinars and Live Streaming", "purpose": "Broadcast, interactive livestreams, event communication and audience interaction."},
    "AI_CONVERSATIONAL_VOICE": {"name": "AI Conversational and Voice Systems", "purpose": "Conversational agents, voice bots, speech interfaces, transcription and synthesis."},
    "IDENTITY_VERIFICATION_OTP": {"name": "Identity Verification and OTP", "purpose": "OTP, MFA, number verification, anti-fraud and identity confirmation channels."},
    "NOTIFICATION_ORCHESTRATION": {"name": "Notification Orchestration", "purpose": "Multi-channel routing, templates, preferences, retries, event triggers and workflow engines."},
    "FAX_VOICEMAIL_LEGACY": {"name": "Fax Voicemail and Legacy Communication", "purpose": "Fax gateways, voicemail, audiotex, paging and legacy enterprise channels."},
    "SATELLITE_EMERGENCY_IOT": {"name": "Satellite Emergency and IoT Communication", "purpose": "Satellite messaging, emergency alerting, public warning and machine communication."},
    "COMMUNICATION_ANALYTICS": {"name": "Communication Analytics and Observability", "purpose": "Delivery analytics, call quality, logs, metrics, tracing and campaign insights."},
    "PRIVACY_SECURITY_COMPLIANCE": {"name": "Privacy Security and Compliance", "purpose": "Encryption, consent, data minimization, retention, audit and lawful processing."},
    "TRUST_SAFETY_MODERATION": {"name": "Trust Safety and Moderation", "purpose": "Abuse prevention, spam controls, reporting, content moderation and user protection."},
    "ACCESSIBILITY_MULTILINGUAL": {"name": "Accessibility and Multilingual Communication", "purpose": "Captions, assistive communication, translation, localization and accessible channels."},
    "INDIA_COMMUNICATION_REGULATORY": {"name": "India Communication and Regulatory", "purpose": "India-specific telecom, DLT, sender registration, TRAI/DoT authorisation and compliance."},
    "RESTRICTED_SERVICES_AGE_CONSENT": {"name": "Restricted Services Age and Consent", "purpose": "Age-gated service discovery and safeguards; legal, consent and platform-policy review required."},
    "RELATIONSHIPS_WELLNESS_EDUCATION": {"name": "Relationships and Wellness Education", "purpose": "Educational and support communications with privacy, safeguarding and consent boundaries."},
}

def list_domains() -> list[dict[str, Any]]:
    return [{"domain_id": key, **value} for key, value in DOMAIN_DEFINITIONS.items()]

__all__ = ["DOMAIN_DEFINITIONS", "list_domains"]
