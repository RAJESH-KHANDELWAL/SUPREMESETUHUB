"""Canonical hospitality industry taxonomy."""
DOMAINS = {
  "lodging": [
    "Hotels",
    "Resorts",
    "Motels",
    "Hostels",
    "Serviced apartments",
    "Homestays",
    "Vacation rentals",
    "Guest houses"
  ],
  "dining": [
    "Fine dining",
    "Casual dining",
    "Quick service",
    "Cafes",
    "Bakeries",
    "Cloud kitchens",
    "Catering",
    "Food trucks"
  ],
  "food_beverage": [
    "Menu engineering",
    "Kitchen operations",
    "Food sourcing",
    "Inventory",
    "Allergen information",
    "Food safety",
    "Beverage programs"
  ],
  "guest_experience": [
    "Reservations",
    "Check-in",
    "Concierge",
    "Housekeeping",
    "Accessibility",
    "Guest feedback",
    "Loyalty",
    "Service recovery"
  ],
  "events_venues": [
    "Banquets",
    "Meetings",
    "Conferences",
    "Weddings",
    "Exhibitions",
    "Event catering"
  ],
  "workforce": [
    "Front office",
    "Housekeeping teams",
    "Kitchen teams",
    "Maintenance",
    "Security",
    "Scheduling",
    "Training"
  ],
  "safety_compliance": [
    "Fire safety",
    "Food hygiene",
    "Guest privacy",
    "Licensing checks",
    "Incident management",
    "Emergency readiness"
  ],
  "sustainability": [
    "Energy",
    "Water",
    "Waste",
    "Responsible sourcing",
    "Local community",
    "Biodiversity"
  ],
  "geography": [
    "Country",
    "State or province",
    "District or county",
    "City",
    "Locality",
    "Tourism region"
  ]
}

def list_domains():
    return [{"id": key, "capabilities": list(values)} for key, values in DOMAINS.items()]

def get_domain(domain_id):
    values = DOMAINS.get(str(domain_id or "").strip().lower())
    return {"id": str(domain_id).strip().lower(), "capabilities": list(values)} if values is not None else None
