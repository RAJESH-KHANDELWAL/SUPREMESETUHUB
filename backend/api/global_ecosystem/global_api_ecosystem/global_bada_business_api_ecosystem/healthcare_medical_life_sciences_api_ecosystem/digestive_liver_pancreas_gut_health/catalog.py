"""Catalog metadata for Digestive, Liver & Gut Health."""
CATEGORY_ID = "digestive_liver_pancreas_gut_health"
CATEGORY_NAME = "Digestive, Liver & Gut Health"
DESCRIPTION = "Digestive tract, stomach, intestines, liver, gallbladder, pancreas and gut health."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
