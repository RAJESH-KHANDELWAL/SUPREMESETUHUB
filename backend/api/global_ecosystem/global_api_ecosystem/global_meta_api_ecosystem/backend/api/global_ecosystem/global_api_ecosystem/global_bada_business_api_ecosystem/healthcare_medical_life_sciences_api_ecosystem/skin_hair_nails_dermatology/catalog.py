"""Catalog metadata for Skin, Hair & Nail Health."""
CATEGORY_ID = "skin_hair_nails_dermatology"
CATEGORY_NAME = "Skin, Hair & Nail Health"
DESCRIPTION = "Dermatology, skin, hair, nails, wound and burn care."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
