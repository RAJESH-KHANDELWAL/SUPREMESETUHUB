"""Catalog metadata for Agriculture & Farming."""
CATEGORY_ID = "agriculture_farming_primary_production"
CATEGORY_NAME = "Agriculture & Farming"
DESCRIPTION = "Crop production, farm operations, horticulture, protected cultivation and farm services."
STATUS = "taxonomy_scaffold"


def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
