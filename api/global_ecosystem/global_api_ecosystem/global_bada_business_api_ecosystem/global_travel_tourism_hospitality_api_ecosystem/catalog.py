"""Travel, tourism and hospitality taxonomy."""
CATEGORIES = [
  {
    "id": "travel_agencies",
    "name": "Travel Agencies & Tour Operators",
    "subcategories": [
      "domestic_tours",
      "international_tours",
      "custom_itineraries",
      "group_tours"
    ]
  },
  {
    "id": "accommodation",
    "name": "Accommodation & Lodging",
    "subcategories": [
      "hotels",
      "resorts",
      "hostels",
      "serviced_apartments"
    ]
  },
  {
    "id": "airlines_and_air_services",
    "name": "Airlines & Air Services",
    "subcategories": [
      "commercial_airlines",
      "charter_services",
      "flight_support",
      "airport_services"
    ]
  },
  {
    "id": "tourist_attractions",
    "name": "Tourist Attractions & Experiences",
    "subcategories": [
      "heritage_sites",
      "museums",
      "theme_parks",
      "adventure_attractions"
    ]
  },
  {
    "id": "hospitality_food_services",
    "name": "Hospitality & Food Services",
    "subcategories": [
      "restaurants",
      "cafes",
      "catering",
      "hotel_dining"
    ]
  },
  {
    "id": "meetings_and_events",
    "name": "Meetings, Incentives, Conferences & Events",
    "subcategories": [
      "conference_venues",
      "corporate_events",
      "incentive_travel",
      "event_management"
    ]
  },
  {
    "id": "destination_management",
    "name": "Destination Management",
    "subcategories": [
      "destination_marketing",
      "visitor_information",
      "local_experiences",
      "tourism_boards"
    ]
  },
  {
    "id": "transport_for_travellers",
    "name": "Travel Transport & Transfers",
    "subcategories": [
      "airport_transfers",
      "car_rentals",
      "tourist_coaches",
      "cruise_services"
    ]
  },
  {
    "id": "travel_technology",
    "name": "Travel Technology & Booking Platforms",
    "subcategories": [
      "online_travel_agencies",
      "booking_engines",
      "travel_management_software",
      "channel_managers"
    ]
  },
  {
    "id": "wellness_and_retreats",
    "name": "Wellness Tourism & Retreats",
    "subcategories": [
      "wellness_retreats",
      "yoga_retreats",
      "spa_destinations",
      "medical_travel_support"
    ]
  },
  {
    "id": "eco_and_adventure_tourism",
    "name": "Eco, Cultural & Adventure Tourism",
    "subcategories": [
      "eco_tourism",
      "wildlife_tours",
      "trekking_and_outdoors",
      "cultural_tours"
    ]
  },
  {
    "id": "hospitality_operations",
    "name": "Hospitality Operations & Support",
    "subcategories": [
      "hotel_management",
      "housekeeping_services",
      "hospitality_training",
      "revenue_management"
    ]
  }
]
def list_categories(): return [dict(x, subcategories=list(x["subcategories"])) for x in CATEGORIES]
def get_category(category_id: str):
    for x in CATEGORIES:
        if x["id"] == category_id: return dict(x, subcategories=list(x["subcategories"]))
    return None
