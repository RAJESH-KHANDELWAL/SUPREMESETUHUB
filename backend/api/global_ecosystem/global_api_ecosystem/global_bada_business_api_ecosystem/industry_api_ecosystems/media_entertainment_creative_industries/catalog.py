"""Media, entertainment and creative industries taxonomy."""
CATEGORIES = [
  {
    "id": "film_and_video",
    "name": "Film & Video Production",
    "subcategories": [
      "film_production",
      "video_production",
      "post_production",
      "visual_effects"
    ]
  },
  {
    "id": "television_and_broadcasting",
    "name": "Television & Broadcasting",
    "subcategories": [
      "television_channels",
      "broadcast_production",
      "streaming_broadcast",
      "broadcast_services"
    ]
  },
  {
    "id": "music_and_audio",
    "name": "Music & Audio",
    "subcategories": [
      "music_production",
      "record_labels",
      "audio_post_production",
      "music_distribution"
    ]
  },
  {
    "id": "digital_content_and_creators",
    "name": "Digital Content & Creator Economy",
    "subcategories": [
      "creator_management",
      "influencer_content",
      "podcast_production",
      "digital_publishing"
    ]
  },
  {
    "id": "news_and_publishing",
    "name": "News, Journalism & Publishing",
    "subcategories": [
      "news_media",
      "magazine_publishing",
      "book_publishing",
      "editorial_services"
    ]
  },
  {
    "id": "advertising_and_marketing",
    "name": "Advertising & Creative Marketing",
    "subcategories": [
      "advertising_agencies",
      "creative_campaigns",
      "media_buying",
      "brand_content"
    ]
  },
  {
    "id": "design_and_visual_arts",
    "name": "Design & Visual Arts",
    "subcategories": [
      "graphic_design",
      "illustration",
      "motion_design",
      "photography"
    ]
  },
  {
    "id": "gaming_and_esports",
    "name": "Gaming & Esports",
    "subcategories": [
      "game_development",
      "game_publishing",
      "esports_events",
      "gaming_content"
    ]
  },
  {
    "id": "live_events_and_performance",
    "name": "Live Events & Performing Arts",
    "subcategories": [
      "concerts",
      "theatre",
      "live_performances",
      "event_production"
    ]
  },
  {
    "id": "animation_and_vfx",
    "name": "Animation & Visual Effects",
    "subcategories": [
      "2d_animation",
      "3d_animation",
      "visual_effects_studios",
      "character_design"
    ]
  },
  {
    "id": "media_technology",
    "name": "Media Technology & Distribution",
    "subcategories": [
      "content_delivery",
      "media_asset_management",
      "streaming_platforms",
      "digital_rights_management"
    ]
  },
  {
    "id": "talent_and_artist_services",
    "name": "Talent & Artist Services",
    "subcategories": [
      "artist_management",
      "casting_services",
      "talent_agencies",
      "creative_recruitment"
    ]
  }
]
def list_categories(): return [dict(x, subcategories=list(x["subcategories"])) for x in CATEGORIES]
def get_category(category_id: str):
    for x in CATEGORIES:
        if x["id"] == category_id: return dict(x, subcategories=list(x["subcategories"]))
    return None
