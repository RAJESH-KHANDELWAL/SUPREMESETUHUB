"""Catalog metadata for Organic & Natural Products."""
CATEGORY_ID = "organic_natural_products"
CATEGORY_NAME = "Organic & Natural Products"
DESCRIPTION = "Organic farming, natural produce, regenerative practices and certification."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
