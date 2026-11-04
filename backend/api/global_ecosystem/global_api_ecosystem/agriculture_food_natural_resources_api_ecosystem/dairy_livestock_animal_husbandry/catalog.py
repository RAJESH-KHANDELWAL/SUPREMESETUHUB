"""Catalog metadata for Dairy & Animal Husbandry."""
CATEGORY_ID = "dairy_livestock_animal_husbandry"
CATEGORY_NAME = "Dairy & Animal Husbandry"
DESCRIPTION = "Dairy, livestock, poultry, animal nutrition, veterinary and allied services."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
