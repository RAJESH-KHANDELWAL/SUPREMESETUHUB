"""Broad business-domain taxonomy; catalogue entries are scope, not provider claims."""
from copy import deepcopy

GEOGRAPHIC_SCOPES = (
    "bharat_india", "south_asia", "asia_pacific", "middle_east", "africa",
    "europe", "north_america", "latin_america_caribbean", "oceania",
    "global_cross_border",
)
MATURITY_LEVELS = (
    "basic_normal", "standard", "professional", "advanced", "expert",
    "enterprise_industrial", "research_frontier", "supreme_long_horizon",
)

BUSINESS_VERTICALS = {
    "agriculture": {"name": "Agriculture & Farming", "areas": ["crops", "soil", "seeds", "irrigation", "machinery", "livestock", "fisheries", "agri-finance", "farm supply chains"]},
    "food": {"name": "Food & Beverage", "areas": ["production", "processing", "food safety", "nutrition", "restaurants", "grocery", "distribution"]},
    "manufacturing": {"name": "Manufacturing & Industry", "areas": ["factories", "materials", "industrial automation", "quality", "maintenance", "industrial IoT"]},
    "retail_commerce": {"name": "Retail & Commerce", "areas": ["wholesale", "retail", "e-commerce", "marketplaces", "franchising", "consumer brands"]},
    "finance_fintech": {"name": "Finance & Fintech", "areas": ["accounting", "payments", "lending", "insurance", "financial technology", "risk"]},
    "education": {"name": "Education & Training", "areas": ["schools", "higher education", "vocational skills", "coaching", "online courses", "research"]},
    "health_wellness": {"name": "Health & Wellness", "areas": ["healthcare services", "diagnostics", "medical devices", "fitness", "wellness", "health technology"]},
    "real_estate_construction": {"name": "Real Estate & Construction", "areas": ["residential", "commercial", "property services", "construction", "architecture", "facilities"]},
    "technology_ai": {"name": "Technology, AI & Software", "areas": ["AI", "SaaS", "websites", "apps", "cloud", "cybersecurity", "developer tools"]},
    "media_entertainment": {"name": "Media & Entertainment", "areas": ["film", "music", "publishing", "broadcasting", "OTT", "events", "creator businesses"]},
    "travel_hospitality": {"name": "Travel & Hospitality", "areas": ["tourism", "hotels", "restaurants", "travel services", "events", "guest operations"]},
    "transport_logistics": {"name": "Transport & Logistics", "areas": ["road", "rail", "aviation", "maritime", "warehousing", "freight", "courier"]},
    "energy_environment": {"name": "Energy & Environment", "areas": ["renewables", "power", "storage", "water", "climate", "waste", "circular economy"]},
    "professional_services": {"name": "Professional & Business Services", "areas": ["consulting", "legal services", "accounting", "HR", "marketing", "design", "outsourcing"]},
    "network_marketing_direct_selling": {"name": "Network Marketing & Direct Selling", "areas": ["direct selling", "multi-level distribution", "affiliate models", "referrals", "distributor education", "compliance"]},
    "sports_fitness": {"name": "Sports & Fitness", "areas": ["sports clubs", "coaching", "fitness centres", "sports technology", "events", "equipment"]},
    "fashion_lifestyle": {"name": "Fashion & Lifestyle", "areas": ["apparel", "textiles", "footwear", "beauty", "cosmetics", "personal care", "luxury"]},
    "social_cultural_enterprise": {"name": "Social, Cultural & Heritage Enterprise", "areas": ["artisan commerce", "heritage services", "community ventures", "cultural education", "responsible tourism"]},
    "adult_relationship_intimacy": {"name": "Adult Relationship, Intimacy & Sexual Wellness Business", "areas": ["adult relationship education", "sexual wellness products", "consent education", "couples services", "adult health information"]},
    "adult_entertainment_industry": {"name": "Lawful Adult Entertainment Industry", "areas": ["adult-only production services", "performer representation", "licensed distribution", "subscription platforms", "age assurance", "content moderation", "rights and royalties"]},
    "public_civic_services": {"name": "Public & Civic Services", "areas": ["public service vendors", "civic technology", "emergency resilience", "accessibility", "digital public infrastructure"]},
    "research_frontier": {"name": "Research & Frontier Ventures", "areas": ["biotechnology", "robotics", "quantum", "space", "advanced materials", "research commercialisation"]},
}

def geographic_scopes():
    return list(GEOGRAPHIC_SCOPES)

def maturity_levels():
    return list(MATURITY_LEVELS)

def list_verticals():
    """Return detached catalogue records."""
    return [{"id": key, **deepcopy(value)} for key, value in BUSINESS_VERTICALS.items()]

def get_vertical(vertical_id: str):
    key = str(vertical_id or "").strip().casefold()
    value = BUSINESS_VERTICALS.get(key)
    return {"id": key, **deepcopy(value)} if value else None

def search_verticals(term: str):
    needle = str(term or "").strip().casefold()
    if not needle:
        return []
    return [
        item for item in list_verticals()
        if needle in item["id"].casefold()
        or needle in item["name"].casefold()
        or any(needle in area.casefold() for area in item["areas"])
    ]
