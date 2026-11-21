"""Meta Core product inventory sourced from the canonical Meta API catalog."""
from __future__ import annotations
from typing import Any
from backend.api.global_ecosystem.global_api_ecosystem.meta_api_ecosystem.meta_api_ecosystem import META_API_ECOSYSTEM

_PRODUCT_MAP={
    "graph_core":{"name":"META Graph API","core_module":"meta_graph_core_core_ecosystem","api_module":"meta_graph_api_ecosystem","engine_module":"meta_graph_engine_ecosystem","capabilities":["GRAPH_OBJECTS_FIELDS_EDGES","GRAPH_API_VERSIONING","PAGING_AND_ERROR_CONTRACTS"],"readiness":"CORE_CATALOG_ONLY"},
    "facebook_pages":{"name":"META Facebook Pages","core_module":"meta_facebook_pages_core_ecosystem","api_module":"meta_facebook_pages_api_ecosystem","engine_module":"meta_facebook_pages_engine_ecosystem","capabilities":["PAGE_DISCOVERY","PAGE_CONTENT_PUBLISHING","PAGE_INSIGHTS_AND_MODERATION"],"readiness":"CORE_CATALOG_ONLY"},
    "instagram":{"name":"META Instagram","core_module":"meta_instagram_core_ecosystem","api_module":"meta_instagram_api_ecosystem","engine_module":"meta_instagram_engine_ecosystem","capabilities":["PROFESSIONAL_ACCOUNT_METADATA","MEDIA_PUBLISHING","COMMENTS_MENTIONS_INSIGHTS"],"readiness":"CORE_CATALOG_ONLY"},
    "whatsapp_business":{"name":"META WhatsApp Business","core_module":"meta_whatsapp_business_core_ecosystem","api_module":"meta_whatsapp_business_api_ecosystem","engine_module":"meta_whatsapp_business_engine_ecosystem","capabilities":["BUSINESS_PHONE_NUMBER_METADATA","MESSAGE_TEMPLATE_GOVERNANCE","CLOUD_API_AND_WEBHOOK_BOUNDARY"],"readiness":"CORE_CATALOG_ONLY"},
    "messenger":{"name":"META Messenger","core_module":"meta_messenger_core_ecosystem","api_module":"meta_messenger_api_ecosystem","engine_module":"meta_messenger_engine_ecosystem","capabilities":["PAGE_LINKED_CONVERSATIONS","MESSAGE_SEND_RECEIVE_BOUNDARY","MESSENGER_WEBHOOK_EVENTS"],"readiness":"CORE_CATALOG_ONLY"},
    "threads":{"name":"META Threads","core_module":"meta_threads_core_ecosystem","api_module":"meta_threads_api_ecosystem","engine_module":"meta_threads_engine_ecosystem","capabilities":["THREADS_PROFILE_METADATA","THREADS_PUBLISHING_REPLIES","THREADS_INSIGHTS_DISCOVERY"],"readiness":"CORE_CATALOG_ONLY"},
    "marketing_ads":{"name":"META Marketing and Ads","core_module":"meta_marketing_ads_core_ecosystem","api_module":"meta_marketing_ads_api_ecosystem","engine_module":"meta_marketing_ads_engine_ecosystem","capabilities":["AD_ACCOUNT_METADATA","CAMPAIGN_AND_AD_GOVERNANCE","AD_INSIGHTS_AND_BILLING_BOUNDARY"],"readiness":"CORE_CATALOG_ONLY"},
    "login_identity":{"name":"META Login and Identity","core_module":"meta_login_identity_core_ecosystem","api_module":"meta_login_identity_api_ecosystem","engine_module":"meta_login_identity_engine_ecosystem","capabilities":["OAUTH_AUTHORIZATION_METADATA","CONSENT_AND_SCOPE_POLICY","TOKEN_LIFECYCLE_BOUNDARY"],"readiness":"CORE_CATALOG_ONLY"},
    "business_management":{"name":"META Business Management","core_module":"meta_business_management_core_ecosystem","api_module":"meta_business_management_api_ecosystem","engine_module":"meta_business_management_engine_ecosystem","capabilities":["BUSINESS_PORTFOLIO_METADATA","ASSET_ASSIGNMENT_BOUNDARY","PARTNER_AND_SYSTEM_USER_GOVERNANCE"],"readiness":"CORE_CATALOG_ONLY"},
    "webhooks":{"name":"META Webhooks","core_module":"meta_webhooks_core_ecosystem","api_module":"meta_webhooks_api_ecosystem","engine_module":"meta_webhooks_engine_ecosystem","capabilities":["WEBHOOK_SUBSCRIPTION_METADATA","CALLBACK_CHALLENGE_VALIDATION","EVENT_SIGNATURE_AND_RETRY_POLICY"],"readiness":"CORE_CATALOG_ONLY"},
    "meta_ai":{"name":"META AI Discovery","core_module":"meta_meta_ai_core_ecosystem","api_module":"meta_ai_ecosystem","engine_module":"meta_ai_ecosystem","capabilities":["META_AI_DISCOVERY_ONLY","PUBLIC_API_AVAILABILITY_NOT_ASSERTED","PRODUCT_REFERENCE_METADATA"],"readiness":"DISCOVERY_ONLY"},
}
def list_meta_products()->list[dict[str,Any]]:
    result=[]
    for source in META_API_ECOSYSTEM["children"]:
        family_id=source["id"]
        mapping=_PRODUCT_MAP.get(family_id)
        if mapping is None:
            continue
        result.append({
            "product_id":"meta_"+family_id,
            "family_id":family_id,
            "name":mapping["name"],
            "core_module":mapping["core_module"],
            "api_module":mapping["api_module"],
            "api_path":f'{META_API_ECOSYSTEM["provider_id"]}_api_ecosystem/{mapping["api_module"]}',
            "engine_module":mapping["engine_module"],
            "capabilities":list(mapping["capabilities"]),
            "status":mapping["readiness"],
            "enabled":True,
            "connected":False,
            "live_connection_verified":False,
            "remote_operations_enabled":False,
            "api_calls_performed":0,
            "source_api_catalog_status":source.get("status","catalog_only"),
        })
    return result
def get_meta_product(product_id:str)->dict[str,Any]|None:
    needle=str(product_id).strip().lower()
    return next((x for x in list_meta_products() if x["product_id"]==needle or x["family_id"]==needle or x["core_module"]==needle),None)
def meta_product_summary()->dict[str,Any]:
    items=list_meta_products()
    return {"product_count":len(items),"product_ids":[x["product_id"] for x in items]}
