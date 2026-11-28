"""Unified online, offline and hybrid marketing, media and entertainment taxonomy."""

CATEGORIES = [
    {"id": "marketing_strategy_research", "name": "Marketing Strategy, Research & Consulting", "channels": ["online", "offline", "hybrid"], "subcategories": ["marketing_strategy", "market_research", "customer_insights", "marketing_planning", "go_to_market", "campaign_strategy", "marketing_consulting"]},
    {"id": "digital_marketing", "name": "Digital & Online Marketing", "channels": ["online", "hybrid"], "subcategories": ["seo", "search_engine_optimisation", "sem", "search_engine_marketing", "social_media_marketing", "content_marketing", "email_marketing", "affiliate_marketing", "influencer_marketing", "performance_marketing", "mobile_marketing", "marketing_automation", "web_analytics", "online_reputation_management"]},
    {"id": "offline_marketing_advertising", "name": "Offline Marketing & Advertising", "channels": ["offline", "hybrid"], "subcategories": ["print_advertising", "outdoor_and_hoarding_advertising", "radio_advertising", "television_advertising", "direct_mail_marketing", "in_store_promotions", "trade_show_marketing", "exhibition_promotions", "field_marketing", "sampling_and_activation"]},
    {"id": "branding_public_relations", "name": "Branding, Public Relations & Communications", "channels": ["online", "offline", "hybrid"], "subcategories": ["brand_identity", "brand_positioning", "public_relations", "media_relations", "corporate_communications", "crisis_communications", "reputation_management"]},
    {"id": "creative_design_content", "name": "Creative Design, Photography & Content Production", "channels": ["online", "offline", "hybrid"], "subcategories": ["graphic_design", "creative_campaigns", "copywriting", "commercial_photography", "motion_design", "visual_arts", "advertising_creatives", "print_creative_services"]},
    {"id": "film_and_video", "name": "Film & Video Production", "channels": ["online", "offline", "hybrid"], "subcategories": ["film_production", "video_production", "post_production", "visual_effects", "corporate_video", "advertising_films"]},
    {"id": "television_and_broadcasting", "name": "Television & Broadcasting", "channels": ["offline", "hybrid"], "subcategories": ["television_channels", "broadcast_production", "streaming_broadcast", "broadcast_services", "radio_broadcasting"]},
    {"id": "music_and_audio", "name": "Music & Audio", "channels": ["online", "offline", "hybrid"], "subcategories": ["music_production", "record_labels", "audio_post_production", "music_distribution", "audio_streaming", "sound_design"]},
    {"id": "digital_content_and_creators", "name": "Digital Content & Creator Economy", "channels": ["online", "hybrid"], "subcategories": ["creator_management", "influencer_content", "podcast_production", "digital_publishing", "video_channels", "creator_services"]},
    {"id": "news_and_publishing", "name": "News, Journalism & Publishing", "channels": ["online", "offline", "hybrid"], "subcategories": ["news_media", "magazine_publishing", "book_publishing", "editorial_services", "digital_news", "print_publications"]},
    {"id": "gaming_and_esports", "name": "Gaming & Esports", "channels": ["online", "offline", "hybrid"], "subcategories": ["game_development", "game_publishing", "esports_events", "gaming_content", "gaming_streaming", "gaming_communities"]},
    {"id": "live_events_and_performance", "name": "Live Events & Performing Arts", "channels": ["offline", "hybrid"], "subcategories": ["concerts", "theatre", "live_performances", "event_production", "artist_shows", "cultural_events"]},
    {"id": "animation_and_vfx", "name": "Animation & Visual Effects", "channels": ["online", "offline", "hybrid"], "subcategories": ["2d_animation", "3d_animation", "visual_effects_studios", "character_design", "cgi_production", "animated_content"]},
    {"id": "media_technology", "name": "Media Technology & Distribution", "channels": ["online", "offline", "hybrid"], "subcategories": ["content_delivery", "media_asset_management", "streaming_platforms", "digital_rights_management", "broadcast_technology", "media_distribution"]},
    {"id": "talent_and_artist_services", "name": "Talent & Artist Services", "channels": ["online", "offline", "hybrid"], "subcategories": ["artist_management", "casting_services", "talent_agencies", "creative_recruitment", "talent_booking", "artist_representation"]},
    {"id": "media_buying_ad_operations", "name": "Media Buying, Ad Operations & Campaign Management", "channels": ["online", "offline", "hybrid"], "subcategories": ["digital_media_buying", "traditional_media_buying", "programmatic_advertising", "ad_operations", "campaign_management", "media_planning", "ad_measurement"]},
]


def list_categories():
    """Return a defensive copy of all categories."""
    return [dict(item, channels=list(item["channels"]), subcategories=list(item["subcategories"])) for item in CATEGORIES]


def get_category(category_id: str):
    """Return a category by stable identifier, or None."""
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item, channels=list(item["channels"]), subcategories=list(item["subcategories"]))
    return None
