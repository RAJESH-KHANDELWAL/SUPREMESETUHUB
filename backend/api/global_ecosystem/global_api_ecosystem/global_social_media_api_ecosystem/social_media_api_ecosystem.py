"""India + worldwide social-media provider directory.

This catalog is discovery metadata, not a claim that every provider exposes a
public API or that any account is already connected. Verify current product
availability, official API documentation, permissions and regional law before
building an integration.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

PROVIDER_ID = "social_media"
PROVIDER_NAME = "GLOBAL SOCIAL MEDIA API ECOSYSTEM"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_social_media_api_ecosystem"

# api_access values are cautious discovery labels, not guarantees:
# official_api = documented developer API exists; restricted = approval/partner
# access may be required; protocol_api = open/federated protocol; verify = check
# current official documentation; none_confirmed = no general public API confirmed.
PROVIDERS: list[dict[str, str]] = [
    # Global: mainstream social networks and microblogging
    {"id":"facebook","folder":"facebook_social_media_api_ecosystem","name":"Facebook","region":"global","category":"social_network","api_access":"official_api"},
    {"id":"instagram","folder":"instagram_social_media_api_ecosystem","name":"Instagram","region":"global","category":"photo_video_social","api_access":"official_api_restricted"},
    {"id":"threads","folder":"threads_social_media_api_ecosystem","name":"Threads","region":"global","category":"text_social","api_access":"official_api"},
    {"id":"x","folder":"x_social_media_api_ecosystem","name":"X","region":"global","category":"microblogging","api_access":"official_api_paid_or_restricted"},
    {"id":"bluesky","folder":"bluesky_social_media_api_ecosystem","name":"Bluesky","region":"global","category":"federated_social","api_access":"public_developer_api"},
    {"id":"mastodon","folder":"mastodon_social_media_api_ecosystem","name":"Mastodon","region":"global","category":"federated_social","api_access":"protocol_api"},
    {"id":"truth_social","folder":"truth_social_social_media_api_ecosystem","name":"Truth Social","region":"global","category":"microblogging","api_access":"none_confirmed"},
    {"id":"gettr","folder":"gettr_social_media_api_ecosystem","name":"GETTR","region":"global","category":"microblogging","api_access":"verify"},
    {"id":"gab","folder":"gab_social_media_api_ecosystem","name":"Gab","region":"global","category":"microblogging","api_access":"verify"},
    {"id":"parler","folder":"parler_social_media_api_ecosystem","name":"Parler","region":"global","category":"social_network","api_access":"verify"},
    {"id":"mewe","folder":"mewe_social_media_api_ecosystem","name":"MeWe","region":"global","category":"social_network","api_access":"restricted_or_partner"},
    {"id":"hive_social","folder":"hive_social_social_media_api_ecosystem","name":"Hive Social","region":"global","category":"social_network","api_access":"verify"},
    {"id":"bereal","folder":"bereal_social_media_api_ecosystem","name":"BeReal","region":"global","category":"photo_social","api_access":"restricted_or_verify"},
    {"id":"nextdoor","folder":"nextdoor_social_media_api_ecosystem","name":"Nextdoor","region":"global","category":"neighborhood_community","api_access":"restricted_or_partner"},
    # Messaging, groups, channels and communities
    {"id":"whatsapp","folder":"whatsapp_social_media_api_ecosystem","name":"WhatsApp","region":"global","category":"messaging","api_access":"official_business_api"},
    {"id":"messenger","folder":"messenger_social_media_api_ecosystem","name":"Facebook Messenger","region":"global","category":"messaging","api_access":"official_api"},
    {"id":"telegram","folder":"telegram_social_media_api_ecosystem","name":"Telegram","region":"global","category":"messaging_channels","api_access":"official_api"},
    {"id":"discord","folder":"discord_social_media_api_ecosystem","name":"Discord","region":"global","category":"community_messaging","api_access":"official_api"},
    {"id":"slack","folder":"slack_social_media_api_ecosystem","name":"Slack","region":"global","category":"community_messaging","api_access":"official_api"},
    {"id":"wechat","folder":"wechat_social_media_api_ecosystem","name":"WeChat","region":"global","category":"messaging_super_app","api_access":"official_api_region_scoped"},
    {"id":"qq","folder":"qq_social_media_api_ecosystem","name":"QQ","region":"global","category":"messaging_social","api_access":"official_api_region_scoped"},
    {"id":"line","folder":"line_social_media_api_ecosystem","name":"LINE","region":"global","category":"messaging_social","api_access":"official_messaging_api"},
    {"id":"kakao","folder":"kakao_social_media_api_ecosystem","name":"KakaoTalk / KakaoStory","region":"global","category":"messaging_social","api_access":"official_api"},
    {"id":"imo","folder":"imo_social_media_api_ecosystem","name":"imo","region":"global","category":"messaging","api_access":"verify"},
    {"id":"viber","folder":"viber_social_media_api_ecosystem","name":"Rakuten Viber","region":"global","category":"messaging","api_access":"official_business_api"},
    {"id":"signal","folder":"signal_social_media_api_ecosystem","name":"Signal","region":"global","category":"private_messaging","api_access":"no_supported_general_public_api"},
    {"id":"snapchat","folder":"snapchat_social_media_api_ecosystem","name":"Snapchat","region":"global","category":"messaging_ephemeral","api_access":"official_api_restricted"},
    {"id":"element_matrix","folder":"element_matrix_social_media_api_ecosystem","name":"Element / Matrix","region":"global","category":"federated_messaging","api_access":"open_protocol_api"},
    {"id":"revolt","folder":"revolt_social_media_api_ecosystem","name":"Revolt","region":"global","category":"community_messaging","api_access":"verify"},
    # Video, short-form, live and streaming
    {"id":"youtube","folder":"youtube_social_media_api_ecosystem","name":"YouTube","region":"global","category":"video","api_access":"official_api"},
    {"id":"tiktok","folder":"tiktok_social_media_api_ecosystem","name":"TikTok","region":"global","category":"short_video","api_access":"official_api_restricted"},
    {"id":"twitch","folder":"twitch_social_media_api_ecosystem","name":"Twitch","region":"global","category":"live_streaming","api_access":"official_api"},
    {"id":"kick","folder":"kick_social_media_api_ecosystem","name":"Kick","region":"global","category":"live_streaming","api_access":"official_api_or_restricted_verify"},
    {"id":"rumble","folder":"rumble_social_media_api_ecosystem","name":"Rumble","region":"global","category":"video","api_access":"official_api_or_restricted_verify"},
    {"id":"vimeo","folder":"vimeo_social_media_api_ecosystem","name":"Vimeo","region":"global","category":"video","api_access":"official_api"},
    {"id":"dailymotion","folder":"dailymotion_social_media_api_ecosystem","name":"Dailymotion","region":"global","category":"video","api_access":"official_api"},
    {"id":"odysee","folder":"odysee_social_media_api_ecosystem","name":"Odysee","region":"global","category":"video_federated","api_access":"official_or_protocol_api_verify"},
    {"id":"peertube","folder":"peertube_social_media_api_ecosystem","name":"PeerTube","region":"global","category":"federated_video","api_access":"open_api"},
    {"id":"bilibili","folder":"bilibili_social_media_api_ecosystem","name":"Bilibili","region":"global","category":"video_community","api_access":"official_api_region_scoped"},
    {"id":"youku","folder":"youku_social_media_api_ecosystem","name":"Youku","region":"global","category":"video","api_access":"region_scoped_verify"},
    {"id":"kuaishou","folder":"kuaishou_social_media_api_ecosystem","name":"Kuaishou","region":"global","category":"short_video","api_access":"official_api_region_scoped"},
    {"id":"kwai","folder":"kwai_social_media_api_ecosystem","name":"Kwai","region":"global","category":"short_video","api_access":"regional_partner_verify"},
    {"id":"9gag","folder":"9gag_social_media_api_ecosystem","name":"9GAG","region":"global","category":"meme_community","api_access":"verify"},
    # Photo, visual discovery, art and creator communities
    {"id":"pinterest","folder":"pinterest_social_media_api_ecosystem","name":"Pinterest","region":"global","category":"visual_discovery","api_access":"official_api"},
    {"id":"flickr","folder":"flickr_social_media_api_ecosystem","name":"Flickr","region":"global","category":"photo_community","api_access":"official_api"},
    {"id":"deviantart","folder":"deviantart_social_media_api_ecosystem","name":"DeviantArt","region":"global","category":"creative_community","api_access":"official_api"},
    {"id":"behance","folder":"behance_social_media_api_ecosystem","name":"Behance","region":"global","category":"creative_community","api_access":"official_api"},
    {"id":"dribbble","folder":"dribbble_social_media_api_ecosystem","name":"Dribbble","region":"global","category":"creative_community","api_access":"official_api_restricted"},
    {"id":"artstation","folder":"artstation_social_media_api_ecosystem","name":"ArtStation","region":"global","category":"creative_community","api_access":"verify"},
    {"id":"cara","folder":"cara_social_media_api_ecosystem","name":"Cara","region":"global","category":"artist_community","api_access":"verify"},
    {"id":"pixelfed","folder":"pixelfed_social_media_api_ecosystem","name":"Pixelfed","region":"global","category":"federated_photo","api_access":"open_protocol_api"},
    {"id":"xiaohongshu","folder":"xiaohongshu_social_media_api_ecosystem","name":"Xiaohongshu / RED","region":"global","category":"lifestyle_discovery","api_access":"partner_or_restricted"},
    {"id":"lemon8","folder":"lemon8_social_media_api_ecosystem","name":"Lemon8","region":"global","category":"lifestyle_photo_video","api_access":"verify"},
    # Professional networks, publishing, Q&A and interest communities
    {"id":"linkedin","folder":"linkedin_social_media_api_ecosystem","name":"LinkedIn","region":"global","category":"professional","api_access":"official_api_restricted"},
    {"id":"medium","folder":"medium_social_media_api_ecosystem","name":"Medium","region":"global","category":"publishing","api_access":"limited_api_verify"},
    {"id":"substack","folder":"substack_social_media_api_ecosystem","name":"Substack","region":"global","category":"publishing_newsletters","api_access":"limited_or_partner"},
    {"id":"wordpress","folder":"wordpress_social_media_api_ecosystem","name":"WordPress","region":"global","category":"publishing","api_access":"official_rest_api"},
    {"id":"blogger","folder":"blogger_social_media_api_ecosystem","name":"Blogger","region":"global","category":"blogging","api_access":"official_api"},
    {"id":"ghost","folder":"ghost_social_media_api_ecosystem","name":"Ghost","region":"global","category":"publishing","api_access":"official_content_admin_api"},
    {"id":"writefreely","folder":"writefreely_social_media_api_ecosystem","name":"WriteFreely","region":"global","category":"federated_publishing","api_access":"open_api"},
    {"id":"tumblr","folder":"tumblr_social_media_api_ecosystem","name":"Tumblr","region":"global","category":"blogging_social","api_access":"official_api"},
    {"id":"quora","folder":"quora_social_media_api_ecosystem","name":"Quora","region":"global","category":"q_and_a","api_access":"none_confirmed"},
    {"id":"stack_exchange","folder":"stack_exchange_social_media_api_ecosystem","name":"Stack Exchange Network","region":"global","category":"q_and_a","api_access":"official_api"},
    {"id":"reddit","folder":"reddit_social_media_api_ecosystem","name":"Reddit","region":"global","category":"community_forums","api_access":"official_api_restricted"},
    {"id":"lemmy","folder":"lemmy_social_media_api_ecosystem","name":"Lemmy","region":"global","category":"federated_community","api_access":"open_api"},
    {"id":"mbin","folder":"mbin_social_media_api_ecosystem","name":"Mbin","region":"global","category":"federated_community","api_access":"open_api"},
    {"id":"hacker_news","folder":"hacker_news_social_media_api_ecosystem","name":"Hacker News","region":"global","category":"technology_community","api_access":"official_firebase_api"},
    {"id":"product_hunt","folder":"product_hunt_social_media_api_ecosystem","name":"Product Hunt","region":"global","category":"startup_community","api_access":"official_api"},
    {"id":"goodreads","folder":"goodreads_social_media_api_ecosystem","name":"Goodreads","region":"global","category":"book_community","api_access":"limited_or_deprecated_verify"},
    {"id":"letterboxd","folder":"letterboxd_social_media_api_ecosystem","name":"Letterboxd","region":"global","category":"film_community","api_access":"limited_or_partner_verify"},
    {"id":"meetup","folder":"meetup_social_media_api_ecosystem","name":"Meetup","region":"global","category":"interest_communities","api_access":"official_api_restricted"},
    {"id":"strava","folder":"strava_social_media_api_ecosystem","name":"Strava","region":"global","category":"activity_community","api_access":"official_api"},
    {"id":"garmin_connect","folder":"garmin_connect_social_media_api_ecosystem","name":"Garmin Connect","region":"global","category":"activity_community","api_access":"partner_or_restricted"},
    {"id":"soundcloud","folder":"soundcloud_social_media_api_ecosystem","name":"SoundCloud","region":"global","category":"music_community","api_access":"official_api_restricted"},
    {"id":"bandcamp","folder":"bandcamp_social_media_api_ecosystem","name":"Bandcamp","region":"global","category":"music_community","api_access":"verify"},
    # India-first and Indian regional-language platforms
    {"id":"sharechat","folder":"sharechat_social_media_api_ecosystem","name":"ShareChat","region":"india","category":"regional_language_social","api_access":"partner_or_restricted"},
    {"id":"moj","folder":"moj_social_media_api_ecosystem","name":"Moj","region":"india","category":"short_video","api_access":"partner_or_restricted"},
    {"id":"josh","folder":"josh_social_media_api_ecosystem","name":"Josh","region":"india","category":"short_video","api_access":"partner_or_restricted"},
    {"id":"chingari","folder":"chingari_social_media_api_ecosystem","name":"Chingari","region":"india","category":"short_video","api_access":"partner_or_restricted_verify"},
    {"id":"roposo","folder":"roposo_social_media_api_ecosystem","name":"Roposo","region":"india","category":"video_social_commerce","api_access":"partner_or_restricted"},
    {"id":"public_app","folder":"public_app_social_media_api_ecosystem","name":"Public App","region":"india","category":"local_video_news","api_access":"partner_or_restricted"},
    {"id":"kutumb","folder":"kutumb_social_media_api_ecosystem","name":"Kutumb","region":"india","category":"community","api_access":"verify"},
    {"id":"lokal","folder":"lokal_social_media_api_ecosystem","name":"Lokal","region":"india","category":"regional_language_community","api_access":"verify"},
    {"id":"apna","folder":"apna_social_media_api_ecosystem","name":"Apna","region":"india","category":"professional_community","api_access":"partner_or_restricted"},
    {"id":"taka_tak","folder":"taka_tak_social_media_api_ecosystem","name":"MX TakaTak","region":"india","category":"short_video","api_access":"status_and_api_verify"},
    {"id":"mitron","folder":"mitron_social_media_api_ecosystem","name":"Mitron","region":"india","category":"short_video","api_access":"verify"},
    {"id":"koo","folder":"koo_social_media_api_ecosystem","name":"Koo (historical listing)","region":"india","category":"microblogging","api_access":"discontinued_verify"},
    {"id":"helo","folder":"helo_social_media_api_ecosystem","name":"Helo (historical listing)","region":"india","category":"regional_language_social","api_access":"discontinued"},
    {"id":"microsoft_kaizala","folder":"microsoft_kaizala_social_media_api_ecosystem","name":"Microsoft Kaizala (historical listing)","region":"india","category":"messaging","api_access":"discontinued"},
    {"id":"way2news","folder":"way2news_social_media_api_ecosystem","name":"Way2News","region":"india","category":"regional_news_community","api_access":"verify"},
    {"id":"dailyhunt","folder":"dailyhunt_social_media_api_ecosystem","name":"Dailyhunt","region":"india","category":"regional_content_community","api_access":"partner_or_restricted"},
    {"id":"inshorts","folder":"inshorts_social_media_api_ecosystem","name":"Inshorts","region":"india","category":"news_community","api_access":"verify"},
    {"id":"fancode_community","folder":"fancode_community_social_media_api_ecosystem","name":"FanCode community","region":"india","category":"sports_community","api_access":"verify"},
    # Creator membership, fan communities and age-restricted adult platforms.
    # Names are directory entries only; legal access varies by country and platform.
    {"id":"patreon","folder":"patreon_social_media_api_ecosystem","name":"Patreon","region":"global","category":"creator_membership","api_access":"official_api_restricted"},
    {"id":"ko_fi","folder":"ko_fi_social_media_api_ecosystem","name":"Ko-fi","region":"global","category":"creator_membership","api_access":"webhooks_and_limited_api"},
    {"id":"buymeacoffee","folder":"buymeacoffee_social_media_api_ecosystem","name":"Buy Me a Coffee","region":"global","category":"creator_membership","api_access":"limited_api_verify"},
    {"id":"onlyfans","folder":"onlyfans_social_media_api_ecosystem","name":"OnlyFans","region":"global","category":"adult_creator_membership","api_access":"no_general_public_api_confirmed"},
    {"id":"fansly","folder":"fansly_social_media_api_ecosystem","name":"Fansly","region":"global","category":"adult_creator_membership","api_access":"no_general_public_api_confirmed"},
    {"id":"manyvids","folder":"manyvids_social_media_api_ecosystem","name":"ManyVids","region":"global","category":"adult_creator_marketplace","api_access":"partner_or_restricted_verify"},
    {"id":"justforfans","folder":"justforfans_social_media_api_ecosystem","name":"JustFor.Fans","region":"global","category":"adult_creator_membership","api_access":"no_general_public_api_confirmed"},
    {"id":"fancentro","folder":"fancentro_social_media_api_ecosystem","name":"FanCentro","region":"global","category":"adult_creator_membership","api_access":"partner_or_restricted_verify"},
    {"id":"loyalfans","folder":"loyalfans_social_media_api_ecosystem","name":"LoyalFans","region":"global","category":"adult_creator_membership","api_access":"partner_or_restricted_verify"},
    {"id":"pornhub","folder":"pornhub_social_media_api_ecosystem","name":"Pornhub","region":"global","category":"adult_video_community","api_access":"restricted_or_partner_verify"},
    {"id":"xvideos","folder":"xvideos_social_media_api_ecosystem","name":"XVideos","region":"global","category":"adult_video_community","api_access":"no_general_public_api_confirmed"},
    {"id":"xhamster","folder":"xhamster_social_media_api_ecosystem","name":"xHamster","region":"global","category":"adult_video_community","api_access":"no_general_public_api_confirmed"},
    {"id":"redtube","folder":"redtube_social_media_api_ecosystem","name":"RedTube","region":"global","category":"adult_video_community","api_access":"restricted_or_partner_verify"},
    {"id":"youporn","folder":"youporn_social_media_api_ecosystem","name":"YouPorn","region":"global","category":"adult_video_community","api_access":"restricted_or_partner_verify"},
    {"id":"spankbang","folder":"spankbang_social_media_api_ecosystem","name":"SpankBang","region":"global","category":"adult_video_community","api_access":"no_general_public_api_confirmed"},
    {"id":"bellesa","folder":"bellesa_social_media_api_ecosystem","name":"Bellesa","region":"global","category":"adult_creator_community","api_access":"verify"},
    {"id":"adult_community_platforms","folder":"adult_community_platforms_social_media_api_ecosystem","name":"Other lawful age-restricted creator and adult communities","region":"global","category":"adult_social","api_access":"review_each_provider"},
    # Social commerce and marketplace communities
    {"id":"amazon_influencer","folder":"amazon_influencer_social_media_api_ecosystem","name":"Amazon Influencer / Inspire","region":"global","category":"social_commerce","api_access":"official_api_restricted"},
    {"id":"etsy_community","folder":"etsy_community_social_media_api_ecosystem","name":"Etsy","region":"global","category":"marketplace_community","api_access":"official_api"},
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
    "verify_current_docs_and_product_status": True,
    "respect_platform_terms_rate_limits_and_app_review": True,
    "require_user_authorization_and_minimum_scopes": True,
    "adult_platforms": (
        "Directory metadata only for lawful, consensual, age-restricted services. "
        "Apply age assurance, consent, privacy and local-law controls. No explicit "
        "media generation, hosting, scraping, or distribution is provided."
    ),
    "regional_compliance": (
        "Provider availability and legality vary by jurisdiction. Check current "
        "Indian law, applicable court/government orders, geo-restrictions and each "
        "platform's terms before enabling access."
    ),
    "privacy": "Minimize personal data; honor consent, deletion and retention requirements.",
}

SOCIAL_MEDIA_API_ECOSYSTEM: dict[str, Any] = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "provider_catalog_path": PROVIDER_CATALOG_PATH,
    "regions": ["india", "global"],
    "coverage": (
        "Mainstream, Indian regional, professional, creator, publishing, messaging, "
        "community, federated, social-commerce and age-restricted adult platforms."
    ),
    "provider_count": len(PROVIDERS),
    "categories": CATEGORIES,
    "providers": PROVIDERS,
    "implementation_rules": IMPLEMENTATION_RULES,
    "live_connections_verified": False,
}

def get_social_media_api_ecosystem() -> dict[str, Any]:
    """Return a defensive copy of the provider catalog."""
    return deepcopy(SOCIAL_MEDIA_API_ECOSYSTEM)

def list_social_media_providers(
    region: str | None = None, category: str | None = None
) -> list[dict[str, str]]:
    """Filter by region; India results also include globally available providers."""
    result = [dict(item) for item in PROVIDERS]
    if region:
        normalized_region = region.strip().lower()
        if normalized_region == "india":
            result = [item for item in result if item["region"] in ("india", "global")]
        elif normalized_region == "global":
            result = [item for item in result if item["region"] == "global"]
        else:
            result = [item for item in result if item["region"] == normalized_region]
    if category:
        result = [item for item in result if item["category"] == category.strip().lower()]
    return result

__all__ = [
    "PROVIDER_ID", "PROVIDER_NAME", "PROVIDER_CATALOG_PATH", "PROVIDERS",
    "CATEGORIES", "IMPLEMENTATION_RULES", "SOCIAL_MEDIA_API_ECOSYSTEM",
    "get_social_media_api_ecosystem", "list_social_media_providers",
]
