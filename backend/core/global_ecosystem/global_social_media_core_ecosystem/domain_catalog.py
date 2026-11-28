"""Social Media Core platform domain taxonomy."""
from typing import Any
from .product_catalog import list_social_media_platforms
DOMAIN_DEFINITIONS:dict[str,dict[str,str]]={
    "SOCIAL_NETWORKING_AND_MICROBLOGGING": {
        "name": "Social Networking and Microblogging",
        "purpose": "Profiles, feeds, social graphs, public posts, short-form text and network discovery.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_social_networking_core_ecosystem"
    },
    "MESSAGING_AND_COMMUNITY_COMMUNICATION": {
        "name": "Messaging and Community Communication",
        "purpose": "Direct messaging, group communication, community chat and federated messaging metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_messaging_community_core_ecosystem"
    },
    "VIDEO_LIVE_STREAMING_AND_CREATOR_MEDIA": {
        "name": "Video, Live Streaming and Creator Media",
        "purpose": "Short and long video, live-streaming, video communities and distribution metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_video_live_streaming_core_ecosystem"
    },
    "PUBLISHING_BLOGGING_AND_NEWSLETTERS": {
        "name": "Publishing, Blogging and Newsletters",
        "purpose": "Blogs, independent publishing, newsletters, hosted writing and creator publication metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_publishing_blogging_core_ecosystem"
    },
    "VISUAL_ART_DESIGN_AND_IMAGE_COMMUNITIES": {
        "name": "Visual Art, Design and Image Communities",
        "purpose": "Image sharing, visual discovery, art portfolios, design showcases and creative communities.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_visual_art_design_core_ecosystem"
    },
    "PROFESSIONAL_KNOWLEDGE_AND_DISCUSSION": {
        "name": "Professional, Knowledge and Discussion Communities",
        "purpose": "Professional identity, Q&A, discussion forums, product discovery and interest-based reviews.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_professional_knowledge_core_ecosystem"
    },
    "CREATOR_ECONOMY_AND_MONETIZATION": {
        "name": "Creator Economy and Monetization",
        "purpose": "Creator memberships, audience support, influencer storefronts and community commerce metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_creator_economy_core_ecosystem"
    },
    "ADULT_COMMUNITIES_AND_CREATOR_PLATFORMS_18_PLUS": {
        "name": "Adult Communities and Creator Platforms (18+)",
        "purpose": "Age-restricted adult community and creator-platform classification, consent, privacy and compliance metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_adult_platforms_18_plus_core_ecosystem"
    },
    "NEWS_AND_CONTENT_DISCOVERY": {
        "name": "News and Content Discovery",
        "purpose": "News aggregation, short news feeds, regional information discovery and publisher metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_news_discovery_core_ecosystem"
    },
    "MUSIC_AUDIO_AND_PODCAST_COMMUNITIES": {
        "name": "Music, Audio and Podcast Communities",
        "purpose": "Music publishing, audio discovery, creator catalogs and audio-community metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_music_audio_core_ecosystem"
    },
    "SPORTS_FITNESS_AND_ACTIVITY_COMMUNITIES": {
        "name": "Sports, Fitness and Activity Communities",
        "purpose": "Sports fan communities, activity tracking and fitness-social metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_sports_fitness_core_ecosystem"
    },
    "REGIONAL_AND_LOCAL_SOCIAL_COMMUNITIES": {
        "name": "Regional and Local Social Communities",
        "purpose": "Regional-language social networks, local communities, neighborhood networks and India-focused social discovery.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_regional_local_communities_core_ecosystem"
    },
    "DECENTRALIZED_AND_FEDIVERSE_COMMUNITIES": {
        "name": "Decentralized and Fediverse Communities",
        "purpose": "Federated, decentralized and community-hosted social network metadata and interoperability boundaries.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_decentralized_fediverse_core_ecosystem"
    },
    "PLATFORM_GOVERNANCE_AND_CROSS_PLATFORM_DISCOVERY": {
        "name": "Platform Governance and Cross-Platform Discovery",
        "purpose": "Cross-platform identity, taxonomy, discovery, lifecycle, interoperability and policy metadata.",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_social_media_core_ecosystem/social_media_platform_governance_core_ecosystem"
    }
}
def list_social_media_domain_inventory()->list[dict[str,Any]]:
    out=[]
    for key,definition in DOMAIN_DEFINITIONS.items():
        platforms=list_social_media_platforms(domain_id=key);out.append({"domain_id":key,**definition,"platform_count":len(platforms),"platform_ids":[x["platform_id"] for x in platforms]})
    return out
def social_media_domain_summary()->dict[str,Any]:
    domains=list_social_media_domain_inventory();return {"success":True,"domain_count":len(domains),"platform_count":sum(x["platform_count"] for x in domains),"domains":domains}
