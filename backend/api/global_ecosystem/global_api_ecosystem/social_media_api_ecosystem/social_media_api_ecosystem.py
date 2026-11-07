"""Global and India social-media provider ecosystem catalog.

This is a provider directory and capability map, not a claim that every provider
has a public API or that live connectivity is enabled. Use only official APIs,
documented partner programs, and lawful user-authorized integrations.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

PROVIDER_ID = "social_media"
PROVIDER_NAME = "SOCIAL MEDIA API ECOSYSTEM"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/social_media_api_ecosystem"

PROVIDERS = [
    # Global mainstream and creator networks
    {"id":"facebook","name":"Facebook","region":"global","category":"social_network","api_status":"official_api"},
    {"id":"instagram","name":"Instagram","region":"global","category":"photo_video_social","api_status":"official_api"},
    {"id":"threads","name":"Threads","region":"global","category":"text_social","api_status":"official_api"},
    {"id":"whatsapp","name":"WhatsApp","region":"global","category":"messaging","api_status":"official_business_api"},
    {"id":"messenger","name":"Facebook Messenger","region":"global","category":"messaging","api_status":"official_platform_api"},
    {"id":"youtube","name":"YouTube","region":"global","category":"video","api_status":"official_api"},
    {"id":"tiktok","name":"TikTok","region":"global","category":"short_video","api_status":"official_api_restricted"},
    {"id":"x","name":"X","region":"global","category":"microblogging","api_status":"official_api_paid_tiers"},
    {"id":"linkedin","name":"LinkedIn","region":"global","category":"professional","api_status":"official_api_restricted"},
    {"id":"pinterest","name":"Pinterest","region":"global","category":"visual_discovery","api_status":"official_api"},
    {"id":"snapchat","name":"Snapchat","region":"global","category":"messaging_ephemeral","api_status":"official_api_restricted"},
    {"id":"reddit","name":"Reddit","region":"global","category":"community_forums","api_status":"official_api"},
    {"id":"discord","name":"Discord","region":"global","category":"community_messaging","api_status":"official_api"},
    {"id":"telegram","name":"Telegram","region":"global","category":"messaging_channels","api_status":"official_api"},
    {"id":"twitch","name":"Twitch","region":"global","category":"live_streaming","api_status":"official_api"},
    {"id":"tumblr","name":"Tumblr","region":"global","category":"blogging_social","api_status":"official_api"},
    {"id":"mastodon","name":"Mastodon","region":"global","category":"federated_social","api_status":"open_protocol_api"},
    {"id":"bluesky","name":"Bluesky","region":"global","category":"federated_social","api_status":"public_developer_api"},
    {"id":"truth_social","name":"Truth Social","region":"global","category":"microblogging","api_status":"no_general_public_api_confirmed"},
    {"id":"bereal","name":"BeReal","region":"global","category":"photo_social","api_status":"limited_or_no_general_public_api"},
    {"id":"clubhouse","name":"Clubhouse","region":"global","category":"audio_social","api_status":"limited_or_no_general_public_api"},
    {"id":"medium","name":"Medium","region":"global","category":"publishing","api_status":"limited_api"},
    {"id":"substack","name":"Substack","region":"global","category":"publishing_newsletters","api_status":"limited_or_partner_access"},
    {"id":"quora","name":"Quora","region":"global","category":"q_and_a","api_status":"no_general_public_api_confirmed"},
    {"id":"wechat","name":"WeChat","region":"global","category":"messaging_super_app","api_status":"official_platform_api_region_scope"},
    {"id":"qq","name":"QQ","region":"global","category":"messaging_social","api_status":"official_platform_api_region_scope"},
    {"id":"weibo","name":"Weibo","region":"global","category":"microblogging","api_status":"official_platform_api_region_scope"},
    {"id":"xiaohongshu","name":"Xiaohongshu / RED","region":"global","category":"lifestyle_discovery","api_status":"partner_or_restricted_api"},
    {"id":"line","name":"LINE","region":"global","category":"messaging_social","api_status":"official_messaging_api"},
    {"id":"kakao","name":"KakaoTalk / KakaoStory","region":"global","category":"messaging_social","api_status":"official_platform_api"},
    {"id":"vk","name":"VK","region":"global","category":"social_network","api_status":"official_api"},
    {"id":"ok","name":"Odnoklassniki","region":"global","category":"social_network","api_status":"official_api"},
    {"id":"imo","name":"imo","region":"global","category":"messaging","api_status":"limited_or_no_general_public_api"},
    {"id":"nextdoor","name":"Nextdoor","region":"global","category":"neighborhood_community","api_status":"partner_or_restricted_api"},
    {"id":"meetup","name":"Meetup","region":"global","category":"interest_communities","api_status":"official_api_restricted"},
    {"id":"flickr","name":"Flickr","region":"global","category":"photo_community","api_status":"official_api"},
    {"id":"deviantart","name":"DeviantArt","region":"global","category":"creative_community","api_status":"official_api"},
    {"id":"pixelfed","name":"Pixelfed","region":"global","category":"federated_photo","api_status":"open_protocol_api"},
    {"id":"peertube","name":"PeerTube","region":"global","category":"federated_video","api_status":"open_api"},
    {"id":"lemmy","name":"Lemmy","region":"global","category":"federated_community","api_status":"open_api"},
    {"id":"kbin_mbin","name":"Mbin","region":"global","category":"federated_community","api_status":"open_api"},
    {"id":"hive","name":"Hive Social","region":"global","category":"social_network","api_status":"public_api_unverified"},
    {"id":"cara","name":"Cara","region":"global","category":"artist_community","api_status":"public_api_unverified"},
    {"id":"cohost","name":"Cohost","region":"global","category":"social_publishing","api_status":"closed_or_discontinued_verify"},
    {"id":" ello","name":"Ello","region":"global","category":"creative_community","api_status":"public_api_unverified"},
    {"id":"mewe","name":"MeWe","region":"global","category":"social_network","api_status":"partner_or_restricted_api"},
    {"id":"gab","name":"Gab","region":"global","category":"microblogging","api_status":"public_api_unverified"},
    {"id":"gettr","name":"GETTR","region":"global","category":"microblogging","api_status":"public_api_unverified"},
    {"id":"parler","name":"Parler","region":"global","category":"social_network","api_status":"status_and_api_to_verify"},
    {"id":"opensea_social","name":"Farcaster","region":"global","category":"decentralized_social","api_status":"protocol_api"},
    {"id":"lens","name":"Lens","region":"global","category":"decentralized_social","api_status":"protocol_api"},
    # India-focused platforms, communities and consumer apps
    {"id":"sharechat","name":"ShareChat","region":"india","category":"regional_language_social","api_status":"partner_or_restricted_api"},
    {"id":"moj","name":"Moj","region":"india","category":"short_video","api_status":"partner_or_restricted_api"},
    {"id":"josh","name":"Josh","region":"india","category":"short_video","api_status":"partner_or_restricted_api"},
    {"id":"chingari","name":"Chingari","region":"india","category":"short_video","api_status":"partner_or_restricted_api"},
    {"id":"roposo","name":"Roposo","region":"india","category":"video_social_commerce","api_status":"partner_or_restricted_api"},
    {"id":"koo","name":"Koo","region":"india","category":"microblogging","api_status":"discontinued_verify"},
    {"id":"kutumb","name":"Kutumb","region":"india","category":"community","api_status":"public_api_unverified"},
    {"id":"public_app","name":"Public App","region":"india","category":"local_video_news","api_status":"partner_or_restricted_api"},
    {"id":"taka tak","name":"TakaTak","region":"india","category":"short_video","api_status":"status_and_api_to_verify"},
    {"id":"mitron","name":"Mitron","region":"india","category":"short_video","api_status":"public_api_unverified"},
    {"id":"microsoft_kaizala","name":"Microsoft Kaizala","region":"india","category":"messaging","api_status":"discontinued"},
    {"id":"sharechat_moj","name":"ShareChat / Moj Creator Ecosystem","region":"india","category":"creator_platform","api_status":"partner_or_restricted_api"},
    {"id":"fauji_social","name":"Fauji / Indian community platforms","region":"india","category":"community","api_status":"verify_individual_product"},
    # Publishing, creator, live and community platforms
    {"id":"wordpress","name":"WordPress","region":"global","category":"publishing","api_status":"official_rest_api"},
    {"id":"blogger","name":"Blogger","region":"global","category":"blogging","api_status":"official_api"},
    {"id":"ghost","name":"Ghost","region":"global","category":"publishing","api_status":"official_admin_content_api"},
    {"id":"writefreely","name":"WriteFreely","region":"global","category":"federated_publishing","api_status":"open_api"},
    {"id":" Patreon","name":"Patreon","region":"global","category":"creator_membership","api_status":"official_api_restricted"},
    {"id":"ko_fi","name":"Ko-fi","region":"global","category":"creator_membership","api_status":"webhooks_and_limited_api"},
    {"id":"buymeacoffee","name":"Buy Me a Coffee","region":"global","category":"creator_membership","api_status":"limited_api"},
    {"id":"onlyfans","name":"OnlyFans","region":"global","category":"adult_creator_membership","api_status":"no_general_public_api_confirmed"},
    {"id":"fansly","name":"Fansly","region":"global","category":"adult_creator_membership","api_status":"no_general_public_api_confirmed"},
    {"id":"manyvids","name":"ManyVids","region":"global","category":"adult_creator_marketplace","api_status":"partner_or_restricted_api"},
    {"id":"justforfans","name":"JustForFans","region":"global","category":"adult_creator_membership","api_status":"no_general_public_api_confirmed"},
    {"id":"fancentro","name":"FanCentro","region":"global","category":"adult_creator_membership","api_status":"partner_or_restricted_api"},
    {"id":"loyalfans","name":"LoyalFans","region":"global","category":"adult_creator_membership","api_status":"partner_or_restricted_api"},
    {"id":"adult_community_platforms","name":"Age-Restricted Creator & Adult Community Platforms","region":"global","category":"adult_social","api_status":"individual_platform_review_required"},
    # Social commerce and reviews/community
    {"id":"amazon_influencer","name":"Amazon Influencer / Inspire","region":"global","category":"social_commerce","api_status":"official_api_restricted"},
    {"id":"etsy_community","name":"Etsy Community","region":"global","category":"marketplace_community","api_status":"official_api_for_marketplace"},
    {"id":"goodreads","name":"Goodreads","region":"global","category":"book_community","api_status":"limited_or_deprecated_api_verify"},
    {"id":"letterboxd","name":"Letterboxd","region":"global","category":"film_community","api_status":"limited_or_partner_api"},
    {"id":"strava","name":"Strava","region":"global","category":"activity_community","api_status":"official_api"},
    {"id":"garmin_connect","name":"Garmin Connect","region":"global","category":"activity_community","api_status":"partner_or_restricted_api"},
]

CATEGORIES = [
    "mainstream_social_networks", "microblogging_and_text", "messaging_and_channels",
    "photo_and_video", "short_video_and_reels", "live_streaming_and_audio",
    "professional_and_business", "creator_and_influencer", "blogs_and_publishing",
    "forums_qa_and_communities", "federated_and_decentralized_social",
    "regional_language_and_india_first", "social_commerce_and_reviews",
    "adult_creator_and_age_restricted_communities",
]

IMPLEMENTATION_RULES = {
    "catalog_is_not_connector": True,
    "official_api_only_for_automated_integrations": True,
    "respect_platform_terms_rate_limits_and_app_review": True,
    "require_user_authorization_and_minimum_scopes": True,
    "adult_platforms": "Only lawful, consensual, age-restricted platform metadata and compliant account integrations; no explicit media hosting, generation, scraping, or distribution.",
    "privacy": "Do not collect or infer sensitive personal data; honor deletion, consent and data-retention requirements.",
}

SOCIAL_MEDIA_API_ECOSYSTEM: dict[str, Any] = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "provider_catalog_path": PROVIDER_CATALOG_PATH,
    "regions": ["india", "global"],
    "coverage": "Mainstream, regional, professional, creator, publishing, community, federated and age-restricted adult creator platforms.",
    "provider_count": len(PROVIDERS),
    "categories": CATEGORIES,
    "providers": PROVIDERS,
    "implementation_rules": IMPLEMENTATION_RULES,
    "live_connections_verified": False,
}

def get_social_media_api_ecosystem() -> dict[str, Any]:
    """Return a defensive copy of the social-media ecosystem catalog."""
    return deepcopy(SOCIAL_MEDIA_API_ECOSYSTEM)

def list_social_media_providers(region: str | None = None, category: str | None = None) -> list[dict[str, str]]:
    """Filter provider metadata by region and/or category."""
    result = [dict(item) for item in PROVIDERS]
    if region:
        result = [item for item in result if item["region"] in (region.lower(), "global")]
    if category:
        result = [item for item in result if item["category"] == category.lower()]
    return result

__all__ = [
    "PROVIDER_ID", "PROVIDER_NAME", "PROVIDER_CATALOG_PATH", "PROVIDERS",
    "CATEGORIES", "IMPLEMENTATION_RULES", "SOCIAL_MEDIA_API_ECOSYSTEM",
    "get_social_media_api_ecosystem", "list_social_media_providers",
]
