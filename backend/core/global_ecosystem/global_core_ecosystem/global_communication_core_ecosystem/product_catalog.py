"""Expanded provider and product-family directory for Global Communication Core.

This is a discovery catalog, not a claim of API integration or availability.
Provider names are normalized; overlapping brands and product families are
kept explicit so they can be reviewed without inflating master-catalog counts.
"""
from __future__ import annotations
from typing import Any

BASE = "backend/core/global_ecosystem/global_core_ecosystem/global_communication_core_ecosystem"

# Existing directories only. The larger provider directory below does not imply
# that one folder or adapter exists for every listed organization.
EXISTING_DIRECTORY_INVENTORY: tuple[dict[str, Any], ...] = (
    {"id":"aws_communication","name":"AWS Communication","kind":"provider_family"},
    {"id":"google_communication","name":"Google Communication","kind":"provider_family"},
    {"id":"meta_communication","name":"Meta Communication","kind":"provider_family"},
    {"id":"microsoft_communication","name":"Microsoft Communication","kind":"provider_family"},
    {"id":"slack_communication","name":"Slack Communication","kind":"provider_family"},
    {"id":"twilio_communication","name":"Twilio Communication","kind":"provider_family"},
    {"id":"zoom_communication","name":"Zoom Communication","kind":"provider_family"},
    {"id":"global_communication_providers","name":"Global Communication Providers","kind":"provider_directory"},
    {"id":"india_communication","name":"India Communication","kind":"regional_directory"},
    {"id":"privacy_security","name":"Privacy and Security","kind":"governance_domain"},
    {"id":"moderation_trust_safety","name":"Moderation and Trust Safety","kind":"governance_domain"},
    {"id":"age_verification_safety","name":"Age Verification Safety","kind":"governance_domain"},
    {"id":"adult_creator_business","name":"Adult Creator Business","kind":"restricted_domain"},
    {"id":"adult_platform_directory","name":"Adult Platform Directory","kind":"restricted_directory"},
    {"id":"dating_relationships","name":"Dating and Relationships","kind":"sensitive_domain"},
    {"id":"sexual_wellness_education","name":"Sexual Wellness Education","kind":"education_domain"},
    {"id":"integrations","name":"Communication Integrations","kind":"integration_namespace"},
    {"id":"services","name":"Communication Services","kind":"service_namespace"},
    {"id":"tools","name":"Communication Tools","kind":"tool_namespace"},
)

# id, canonical display name, service family, geographic scope, representative products.
PROVIDER_DIRECTORY: tuple[dict[str, Any], ...] = (
    {"id":"aws","name":"Amazon Web Services","family":"cloud_communication_platform","region":"GLOBAL","products":"Amazon Chime SDK; Amazon Connect; Amazon SES; Pinpoint (service lifecycle to be checked)","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"google","name":"Google","family":"cloud_workspace","region":"GLOBAL","products":"Gmail; Google Meet; Google Chat; Google Voice; Firebase Cloud Messaging","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"meta","name":"Meta","family":"messaging_social","region":"GLOBAL","products":"WhatsApp; Messenger; Instagram Direct","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"microsoft","name":"Microsoft","family":"cloud_workspace","region":"GLOBAL","products":"Exchange Online; Teams; Outlook; Skype for Business (legacy lifecycle check)","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"slack","name":"Slack","family":"team_collaboration","region":"GLOBAL","products":"Slack messaging; huddles; enterprise collaboration","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"twilio","name":"Twilio","family":"cpaas","region":"GLOBAL","products":"Programmable Messaging; Voice; Video; Verify; SendGrid","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"zoom","name":"Zoom","family":"ucaas_video","region":"GLOBAL","products":"Zoom Meetings; Zoom Phone; Team Chat; Video SDK","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"vonage","name":"Vonage","family":"cpaas_ucaas","region":"GLOBAL","products":"Communications APIs; Contact Center; Business Communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"infobip","name":"Infobip","family":"cpaas","region":"GLOBAL","products":"SMS; Voice; Email; RCS; WhatsApp","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"sinch","name":"Sinch","family":"cpaas","region":"GLOBAL","products":"SMS; Voice; Email; RCS; Conversation API","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"bird","name":"Bird","family":"cpaas_customer_engagement","region":"GLOBAL","products":"Messaging; Email; Voice; Customer Engagement","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"telnyx","name":"Telnyx","family":"cpaas_telecom","region":"GLOBAL","products":"Voice; Messaging; SIP trunking; numbers","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"bandwidth","name":"Bandwidth","family":"cpaas_telecom","region":"NORTH_AMERICA","products":"Voice; Messaging; emergency services APIs","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"plivo","name":"Plivo","family":"cpaas","region":"GLOBAL","products":"SMS; Voice; SIP trunking","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"route_mobile","name":"Route Mobile","family":"cpaas","region":"INDIA_GLOBAL","products":"Messaging; Voice; Email; CPaaS","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"tanla","name":"Tanla Platforms","family":"cpaas","region":"INDIA_GLOBAL","products":"Wisely; enterprise messaging; CPaaS","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"tata_communications","name":"Tata Communications","family":"telecom_cpaas","region":"INDIA_GLOBAL","products":"Global SIP Connect; Kaleyra communication platform","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"gupshup","name":"Gupshup","family":"conversational_messaging","region":"INDIA_GLOBAL","products":"WhatsApp Business; SMS; conversational engagement","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"cm_com","name":"CM.com","family":"cpaas","region":"GLOBAL","products":"Messaging; Voice; Payments; conversational AI","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"syniverse","name":"Syniverse","family":"telecom_messaging","region":"GLOBAL","products":"A2P messaging; roaming; network APIs","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"jio","name":"Reliance Jio","family":"telecom_operator","region":"INDIA","products":"Mobile; fixed broadband; enterprise connectivity","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"airtel","name":"Bharti Airtel","family":"telecom_operator","region":"INDIA","products":"Mobile; broadband; enterprise voice; messaging","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"vodafone_idea","name":"Vodafone Idea","family":"telecom_operator","region":"INDIA","products":"Mobile; enterprise connectivity","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"bsnl","name":"BSNL","family":"telecom_operator","region":"INDIA","products":"Mobile; fixed line; broadband; enterprise services","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"att","name":"AT&T","family":"telecom_operator","region":"NORTH_AMERICA","products":"Mobile; fixed network; enterprise communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"verizon","name":"Verizon","family":"telecom_operator","region":"NORTH_AMERICA","products":"Mobile; fixed network; enterprise voice","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"t_mobile","name":"T-Mobile","family":"telecom_operator","region":"NORTH_AMERICA","products":"Mobile; messaging; fixed wireless","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"orange","name":"Orange","family":"telecom_operator","region":"EUROPE_GLOBAL","products":"Mobile; fixed network; enterprise services","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"telefonica","name":"Telefonica","family":"telecom_operator","region":"EUROPE_LATAM","products":"Mobile; fixed network; enterprise communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"deutsche_telekom","name":"Deutsche Telekom","family":"telecom_operator","region":"EUROPE_GLOBAL","products":"Mobile; fixed network; enterprise communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"bt_group","name":"BT Group","family":"telecom_operator","region":"UK_GLOBAL","products":"Fixed network; mobile; enterprise voice","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"vodafone_group","name":"Vodafone Group","family":"telecom_operator","region":"EUROPE_GLOBAL","products":"Mobile; fixed network; IoT connectivity","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"verizon_business","name":"Verizon Business","family":"enterprise_telecom","region":"NORTH_AMERICA","products":"Unified communications; voice; network services","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"ringcentral","name":"RingCentral","family":"ucaas_ccaas","region":"GLOBAL","products":"RingEX; Contact Center; video; messaging","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"8x8","name":"8x8","family":"ucaas_ccaas","region":"GLOBAL","products":"UCaaS; Contact Center; CPaaS","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"cisco","name":"Cisco","family":"ucaas_collaboration","region":"GLOBAL","products":"Webex; calling; meetings; contact center","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"webex","name":"Cisco Webex","family":"video_collaboration","region":"GLOBAL","products":"Meetings; Calling; Messaging; Contact Center","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"mitel","name":"Mitel","family":"ucaas_telephony","region":"GLOBAL","products":"Business telephony; UC; contact center","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"avaya","name":"Avaya","family":"ucaas_ccaas","region":"GLOBAL","products":"Avaya Experience Platform; enterprise communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"genesys","name":"Genesys","family":"ccaas","region":"GLOBAL","products":"Genesys Cloud CX; contact center","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"five9","name":"Five9","family":"ccaas","region":"GLOBAL","products":"Intelligent CX Platform; contact center","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"nice","name":"NICE","family":"ccaas","region":"GLOBAL","products":"CXone; contact center; workforce engagement","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"talkdesk","name":"Talkdesk","family":"ccaas","region":"GLOBAL","products":"Cloud contact center; customer experience","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"amazon_connect","name":"Amazon Connect","family":"ccaas","region":"GLOBAL","products":"Cloud contact center service","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"freshworks","name":"Freshworks","family":"customer_engagement","region":"GLOBAL","products":"Freshdesk; customer support communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"intercom","name":"Intercom","family":"customer_engagement","region":"GLOBAL","products":"Customer messaging; support automation","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"hubspot","name":"HubSpot","family":"crm_customer_engagement","region":"GLOBAL","products":"Email; live chat; customer communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"salesforce","name":"Salesforce","family":"crm_customer_engagement","region":"GLOBAL","products":"Service Cloud; Marketing Cloud; digital engagement","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"customer_io","name":"Customer.io","family":"customer_engagement","region":"GLOBAL","products":"Lifecycle messaging; email; push","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"brevo","name":"Brevo","family":"email_marketing","region":"GLOBAL","products":"Email; SMS; WhatsApp; marketing automation","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"mailchimp","name":"Mailchimp","family":"email_marketing","region":"GLOBAL","products":"Email marketing; customer journeys","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"sendgrid","name":"Twilio SendGrid","family":"email_delivery","region":"GLOBAL","products":"Transactional and marketing email delivery","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"mailgun","name":"Mailgun","family":"email_delivery","region":"GLOBAL","products":"Email API; validation; deliverability","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"postmark","name":"Postmark","family":"email_delivery","region":"GLOBAL","products":"Transactional email delivery","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"resend","name":"Resend","family":"email_delivery","region":"GLOBAL","products":"Developer email API","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"zoho","name":"Zoho","family":"business_workspace","region":"GLOBAL","products":"Zoho Mail; Cliq; Meeting; Voice; CRM","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"proton","name":"Proton","family":"secure_email","region":"GLOBAL","products":"Proton Mail; encrypted communication","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"fastmail","name":"Fastmail","family":"email_provider","region":"GLOBAL","products":"Hosted email; calendar; contacts","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"yahoo","name":"Yahoo","family":"email_provider","region":"GLOBAL","products":"Yahoo Mail","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"apple","name":"Apple","family":"messaging_workspace","region":"GLOBAL","products":"iMessage; FaceTime; Mail; Business Chat (availability/lifecycle check)","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"telegram","name":"Telegram","family":"ott_messaging","region":"GLOBAL","products":"Telegram Messenger; Bots; Channels","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"signal","name":"Signal Foundation","family":"ott_messaging","region":"GLOBAL","products":"Signal encrypted messaging and calls","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"line","name":"LY Corporation LINE","family":"ott_messaging","region":"ASIA","products":"LINE messaging; calls; official accounts","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"wechat","name":"Tencent","family":"ott_messaging_social","region":"CHINA_GLOBAL","products":"WeChat; WeCom; Tencent Meeting","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"viber","name":"Rakuten Viber","family":"ott_messaging","region":"GLOBAL","products":"Viber messaging; calls; business messaging","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"kakao","name":"Kakao","family":"ott_messaging","region":"SOUTH_KOREA","products":"KakaoTalk; business messaging","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"discord","name":"Discord","family":"community_voice_video","region":"GLOBAL","products":"Text; voice; video; communities","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"mattermost","name":"Mattermost","family":"team_collaboration","region":"GLOBAL","products":"Team messaging; workflow collaboration","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"rocket_chat","name":"Rocket.Chat","family":"team_collaboration","region":"GLOBAL","products":"Omnichannel messaging; team collaboration","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"element","name":"Element","family":"team_collaboration","region":"GLOBAL","products":"Matrix-based secure collaboration","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"livekit","name":"LiveKit","family":"realtime_comms_sdk","region":"GLOBAL","products":"Real-time audio; video; data SDK","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"agora","name":"Agora","family":"realtime_comms_sdk","region":"GLOBAL","products":"Real-time voice; video; interactive streaming","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"daily","name":"Daily","family":"realtime_comms_sdk","region":"GLOBAL","products":"Video and audio APIs","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"whereby","name":"Whereby","family":"video_meetings","region":"GLOBAL","products":"Video meetings; embedded video APIs","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"gotomeeting","name":"GoTo","family":"video_ucaas","region":"GLOBAL","products":"GoTo Meeting; GoTo Connect","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"jitsi","name":"Jitsi","family":"video_meetings_open_source","region":"GLOBAL","products":"Jitsi Meet; conferencing stack","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"onesignal","name":"OneSignal","family":"push_notifications","region":"GLOBAL","products":"Push; email; in-app messaging; SMS","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"firebase","name":"Google Firebase","family":"push_notifications","region":"GLOBAL","products":"Firebase Cloud Messaging","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"pusher","name":"Pusher","family":"realtime_messaging","region":"GLOBAL","products":"Channels; Beams push notifications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"knock","name":"Knock","family":"notification_orchestration","region":"GLOBAL","products":"Notification infrastructure and workflows","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"novu","name":"Novu","family":"notification_orchestration","region":"GLOBAL","products":"Open-source notification infrastructure","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"routee","name":"Routee","family":"cpaas","region":"GLOBAL","products":"SMS; Voice; verification APIs","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"kaleyra","name":"Kaleyra","family":"cpaas","region":"INDIA_GLOBAL","products":"Messaging; voice; video APIs","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"wati","name":"WATI","family":"whatsapp_business_platform","region":"GLOBAL","products":"WhatsApp Business API platform","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"respond_io","name":"respond_io","family":"customer_messaging","region":"GLOBAL","products":"Omnichannel customer conversation platform","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"zendesk","name":"Zendesk","family":"ccaas_customer_support","region":"GLOBAL","products":"Support messaging; voice; contact center","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"kustomer","name":"Kustomer","family":"ccaas_customer_support","region":"GLOBAL","products":"Customer service CRM and messaging","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"telkomsel","name":"Telkomsel","family":"telecom_operator","region":"INDONESIA","products":"Mobile; enterprise connectivity","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"singtel","name":"Singtel","family":"telecom_operator","region":"SINGAPORE_GLOBAL","products":"Mobile; fixed; enterprise communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"ntt","name":"NTT Group","family":"telecom_operator","region":"JAPAN_GLOBAL","products":"Telecom; network; enterprise communication","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"china_mobile","name":"China Mobile","family":"telecom_operator","region":"CHINA","products":"Mobile; fixed; enterprise services","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"china_telecom","name":"China Telecom","family":"telecom_operator","region":"CHINA_GLOBAL","products":"Fixed; mobile; cloud communication","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"tencent_cloud","name":"Tencent Cloud","family":"cloud_communication_platform","region":"GLOBAL","products":"Tencent RTC; IM; meeting services","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"oracle","name":"Oracle","family":"cloud_communication_platform","region":"GLOBAL","products":"Oracle Communications; enterprise communications","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
    {"id":"messagebird_legacy","name":"Bird (formerly MessageBird)","family":"cpaas_customer_engagement","region":"GLOBAL","products":"Bird messaging and customer engagement","record_type":"provider_reference","catalog_status":"REFERENCE_ONLY","live_connection_verified":False},
)

def list_products(*, enabled_only: bool = False) -> list[dict[str, Any]]:
    """Compatibility API: return provider reference records, never live integrations."""
    records = [dict(item, enabled=False, implementation_status="NOT_IMPLEMENTED") for item in PROVIDER_DIRECTORY]
    return [item for item in records if item["enabled"]] if enabled_only else records

def get_product(product_id: str) -> dict[str, Any] | None:
    return next((dict(item) for item in PROVIDER_DIRECTORY if item["id"] == product_id), None)

def list_providers(*, family: str | None = None, region: str | None = None) -> list[dict[str, Any]]:
    items = [dict(item) for item in PROVIDER_DIRECTORY]
    if family:
        items = [item for item in items if item["family"] == family]
    if region:
        items = [item for item in items if item["region"] == region]
    return items

def inventory_summary() -> dict[str, Any]:
    return {
        "provider_reference_count": len(PROVIDER_DIRECTORY),
        "existing_directory_count": len(EXISTING_DIRECTORY_INVENTORY),
        "service_family_count": len({item["family"] for item in PROVIDER_DIRECTORY}),
        "live_integrations_verified": 0,
        "providers": list(PROVIDER_DIRECTORY),
    }

__all__ = ["BASE", "EXISTING_DIRECTORY_INVENTORY", "PROVIDER_DIRECTORY", "list_products", "get_product", "list_providers", "inventory_summary"]
