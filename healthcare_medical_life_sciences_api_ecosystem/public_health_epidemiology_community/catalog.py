"""Catalog metadata for Public Health, Epidemiology & Community Care."""
CATEGORY_ID = "public_health_epidemiology_community"
CATEGORY_NAME = "Public Health, Epidemiology & Community Care"
DESCRIPTION = "Population health, epidemiology, vaccination, sanitation, community and occupational health."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
