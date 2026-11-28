"""Catalog for Sports, Recreation & Community."""
CATEGORIES=(
    {"id": "professional_sports", "name": "Professional Sports", "subcategories": ["sports_teams","professional_leagues","athlete_management","sports_franchises"]},
    {"id": "sports_facilities", "name": "Sports Facilities", "subcategories": ["stadiums","sports_complexes","courts","swimming_pools"]},
    {"id": "fitness_recreation", "name": "Fitness & Recreation", "subcategories": ["recreation_centres","fitness_clubs","outdoor_fitness","community_fitness"]},
    {"id": "sports_coaching", "name": "Sports Coaching & Academies", "subcategories": ["sports_academies","coaching_centres","talent_development","sports_camps"]},
    {"id": "sports_equipment", "name": "Sports Equipment & Apparel", "subcategories": ["sports_goods","athletic_apparel","equipment_manufacturing","sports_retail"]},
    {"id": "sports_events", "name": "Sports Events & Tournaments", "subcategories": ["tournaments","marathons","competitions","event_management"]},
    {"id": "sports_media", "name": "Sports Media & Content", "subcategories": ["sports_broadcasting","sports_journalism","digital_sports_content","sports_streaming"]},
    {"id": "sports_technology", "name": "Sports Technology & Analytics", "subcategories": ["performance_analytics","wearables","sports_software","video_analysis"]},
    {"id": "adventure_recreation", "name": "Adventure & Outdoor Recreation", "subcategories": ["trekking","climbing","cycling","water_sports"]},
    {"id": "community_clubs", "name": "Community Clubs & Associations", "subcategories": ["local_clubs","sports_associations","recreation_groups","youth_clubs"]},
    {"id": "sports_health", "name": "Sports Health & Performance", "subcategories": ["sports_physiotherapy","sports_nutrition","injury_prevention","performance_recovery"]},
    {"id": "esports", "name": "Esports & Gaming", "subcategories": ["esports_teams","gaming_tournaments","gaming_arenas","esports_training"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for item in CATEGORIES:
  if item["id"]==category_id: return dict(item)
 return None
