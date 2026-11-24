"""Catalog metadata for Irrigation & Water Management."""
CATEGORY_ID = "irrigation_water_management"
CATEGORY_NAME = "Irrigation & Water Management"
DESCRIPTION = "Irrigation infrastructure, water-use efficiency, watershed and farm water systems."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
