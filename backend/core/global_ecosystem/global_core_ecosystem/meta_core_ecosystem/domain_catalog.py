"""Meta Core cross-product domain taxonomy with explicit product mappings."""
from __future__ import annotations
from typing import Any
DOMAIN_DEFINITIONS={
    "PROVIDER_GOVERNANCE":{"name":"Provider Governance","purpose":"Provider identity, product-family registration, lifecycle, readiness and ownership.","product_ids":["meta_graph_core","meta_facebook_pages","meta_instagram","meta_whatsapp_business","meta_messenger","meta_threads","meta_marketing_ads","meta_login_identity","meta_business_management","meta_webhooks","meta_ai"]},
    "GRAPH_PLATFORM_AND_OBJECT_MODEL":{"name":"Graph Platform and Object Model","purpose":"Graph nodes, edges, fields, object identifiers, API versions, paging and error contracts.","product_ids":["meta_graph_core"]},
    "FACEBOOK_PAGES_AND_PUBLISHING":{"name":"Facebook Pages and Publishing","purpose":"Page discovery, Page-owned assets, supported publishing, moderation and Page insights.","product_ids":["meta_facebook_pages","meta_graph_core","meta_business_management"]},
    "INSTAGRAM_CREATOR_AND_PROFESSIONAL":{"name":"Instagram Creator and Professional Accounts","purpose":"Professional account discovery, media publishing, comments, mentions and insights subject to eligibility.","product_ids":["meta_instagram","meta_graph_core","meta_business_management"]},
    "WHATSAPP_BUSINESS_MESSAGING":{"name":"WhatsApp Business Messaging","purpose":"Business phone numbers, templates, Cloud API messaging, quality and webhook lifecycle.","product_ids":["meta_whatsapp_business","meta_webhooks","meta_business_management"]},
    "MESSENGER_CONVERSATIONS":{"name":"Messenger Conversations","purpose":"Page-linked conversations, send/receive boundaries, event subscriptions and messaging policy.","product_ids":["meta_messenger","meta_webhooks","meta_facebook_pages"]},
    "THREADS_SOCIAL_NETWORK":{"name":"Threads Social Network","purpose":"Threads profiles, publishing, replies, discovery and insights where supported.","product_ids":["meta_threads","meta_graph_core"]},
    "MARKETING_ADVERTISING_CAMPAIGNS":{"name":"Marketing, Advertising and Campaigns","purpose":"Ad accounts, campaign/ad metadata, authorization, reporting and billing boundaries.","product_ids":["meta_marketing_ads","meta_business_management","meta_login_identity"]},
    "BUSINESS_PORTFOLIO_ASSETS":{"name":"Business Portfolio and Asset Governance","purpose":"Business portfolios, Pages, Instagram accounts, WhatsApp assets, partners, system users and assignments.","product_ids":["meta_business_management","meta_facebook_pages","meta_instagram","meta_whatsapp_business","meta_marketing_ads"]},
    "LOGIN_OAUTH_IDENTITY":{"name":"Login, OAuth and Identity","purpose":"Authorization code flow metadata, redirect/state validation, consent, scopes, token lifecycle and revocation.","product_ids":["meta_login_identity","meta_business_management"]},
    "WEBHOOK_EVENT_DELIVERY":{"name":"Webhook Events and Delivery","purpose":"Subscription metadata, callback verification, signatures, event normalization, retries and delivery status.","product_ids":["meta_webhooks","meta_graph_core","meta_whatsapp_business","meta_messenger"]},
    "META_AI_DISCOVERY":{"name":"Meta AI Discovery","purpose":"Discovery/reference metadata only; does not claim a generally available public Meta AI API.","product_ids":["meta_meta_ai"]},
    "SOCIAL_CONTENT_PUBLISHING":{"name":"Social Content and Publishing","purpose":"Cross-product publishing capability metadata, media constraints, permissions and content lifecycle.","product_ids":["meta_facebook_pages","meta_instagram","meta_threads","meta_whatsapp_business"]},
    "AUDIENCE_INSIGHTS_ANALYTICS":{"name":"Audience Insights and Analytics","purpose":"Page, Instagram and advertising insights metadata, reporting scopes and measurement boundaries.","product_ids":["meta_facebook_pages","meta_instagram","meta_marketing_ads","meta_threads"]},
    "MEDIA_ASSET_MANAGEMENT":{"name":"Media and Asset Management","purpose":"Business-owned media assets, account associations, media references and asset eligibility.","product_ids":["meta_business_management","meta_facebook_pages","meta_instagram","meta_whatsapp_business"]},
    "PRIVACY_DATA_PROTECTION":{"name":"Privacy and Data Protection","purpose":"Personal data minimization, retention, deletion boundaries, consent and data-protection controls.","product_ids":["meta_graph_core","meta_login_identity","meta_business_management","meta_webhooks"]},
    "APP_REVIEW_PERMISSION_COMPLIANCE":{"name":"App Review, Permissions and Compliance","purpose":"App mode, permissions, review, business verification, policy compliance and service eligibility.","product_ids":["meta_login_identity","meta_business_management","meta_marketing_ads","meta_whatsapp_business"]},
    "TENANT_ACCOUNT_ASSET_GOVERNANCE":{"name":"Tenant, Account and Asset Governance","purpose":"Tenant isolation, Meta app/account context, asset ownership, region/product availability and quotas.","product_ids":["meta_login_identity","meta_business_management","meta_marketing_ads","meta_facebook_pages","meta_instagram","meta_whatsapp_business"]},
}
def list_meta_domain_inventory()->list[dict[str,Any]]:
    return [{"domain_id":key,**value} for key,value in DOMAIN_DEFINITIONS.items()]
def get_meta_domain(domain_id:str)->dict[str,Any]|None:
    needle=str(domain_id).strip().upper()
    return next((x for x in list_meta_domain_inventory() if x["domain_id"]==needle),None)
def meta_domain_summary()->dict[str,Any]:
    items=list_meta_domain_inventory()
    mapped={p for d in items for p in d["product_ids"]}
    return {"domain_count":len(items),"domain_ids":[x["domain_id"] for x in items],"mapped_product_count":len(mapped)}
