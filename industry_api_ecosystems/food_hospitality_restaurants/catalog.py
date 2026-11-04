"""Catalog for Food Services, Restaurants & Hospitality."""
CATEGORIES=(
    {"id": "restaurants_dining", "name": "Restaurants & Dining", "subcategories": ["fine_dining","casual_dining","family_restaurants","themed_restaurants"]},
    {"id": "quick_service_food", "name": "Quick Service & Street Food", "subcategories": ["quick_service_restaurants","street_food","food_stalls","takeaway_counters"]},
    {"id": "cafes_bakeries", "name": "Cafes & Bakeries", "subcategories": ["coffee_shops","tea_shops","bakeries","dessert_shops"]},
    {"id": "catering_services", "name": "Catering Services", "subcategories": ["corporate_catering","event_catering","institutional_catering","wedding_catering"]},
    {"id": "food_delivery", "name": "Food Delivery & Takeaway", "subcategories": ["online_food_delivery","cloud_kitchens","meal_delivery","takeaway_services"]},
    {"id": "food_trucks_popups", "name": "Food Trucks & Pop-ups", "subcategories": ["food_trucks","pop_up_kitchens","food_festivals","mobile_catering"]},
    {"id": "institutional_food", "name": "Institutional Food Services", "subcategories": ["school_meals","hospital_food_services","canteens","workplace_dining"]},
    {"id": "hospitality_accommodation", "name": "Hospitality & Accommodation", "subcategories": ["hotels","hostels","guest_houses","serviced_apartments"]},
    {"id": "banquet_event_venues", "name": "Banquet & Event Venues", "subcategories": ["banquet_halls","convention_centres","wedding_venues","event_spaces"]},
    {"id": "food_beverage_supply", "name": "Food & Beverage Supply", "subcategories": ["restaurant_suppliers","beverage_distribution","commercial_kitchens","food_equipment"]},
    {"id": "restaurant_technology", "name": "Restaurant Technology", "subcategories": ["pos_systems","table_reservations","kitchen_automation","restaurant_management_software"]},
    {"id": "food_safety_quality", "name": "Food Safety & Quality Services", "subcategories": ["food_hygiene","food_testing","quality_audits","food_safety_training"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for item in CATEGORIES:
  if item["id"]==category_id: return dict(item)
 return None
