"""Catalog metadata for Food Processing & Manufacturing."""
CATEGORY_ID = "food_processing_manufacturing"
CATEGORY_NAME = "Food Processing & Manufacturing"
DESCRIPTION = "Food transformation, packaging, quality systems and food manufacturing."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
