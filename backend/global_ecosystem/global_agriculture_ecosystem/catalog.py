"""Discoverable agriculture capabilities and their maturity boundaries."""
from copy import deepcopy

MODULES = {
    "crop_production": {"name": "Crop Production", "features": ["crop planning", "season calendar", "yield records", "pest and disease observations"]},
    "soil": {"name": "Soil Management", "features": ["soil test records", "pH and nutrient observations", "soil health history"]},
    "seeds": {"name": "Seeds", "features": ["seed varieties", "seed lot records", "germination test records", "traceability"]},
    "irrigation": {"name": "Irrigation & Water Management", "features": ["water requirement estimates", "irrigation schedules", "water-use records"]},
    "farm_machinery": {"name": "Farm Machinery", "features": ["equipment inventory", "maintenance schedules", "usage logs"]},
    "livestock": {"name": "Livestock", "features": ["animal records", "feeding records", "health and vaccination logs"]},
    "fisheries": {"name": "Fisheries & Aquaculture", "features": ["stock records", "pond or tank observations", "water-quality records"]},
    "agri_fintech": {"name": "Agricultural Finance", "features": ["farm budgets", "expense records", "loan and insurance reference records"]},
    "agricultural_supply_chains": {"name": "Agricultural Supply Chains", "features": ["harvest lots", "storage records", "transport and buyer traceability"]},
}

def list_modules():
    """Return all agriculture modules as detached dictionaries."""
    return [{"id": key, **deepcopy(value)} for key, value in MODULES.items()]

def get_module(module_id: str):
    """Return one module profile, or None for an unknown module."""
    key = str(module_id or "").strip().casefold()
    value = MODULES.get(key)
    return {"id": key, **deepcopy(value)} if value else None
