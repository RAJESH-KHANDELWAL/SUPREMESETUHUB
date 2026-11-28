"""Catalog metadata for Forestry & Natural Resources."""
CATEGORY_ID = "forestry_mining_natural_resources"
CATEGORY_NAME = "Forestry & Natural Resources"
DESCRIPTION = "Forestry, biodiversity-linked enterprise, land resources and responsible extraction."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
