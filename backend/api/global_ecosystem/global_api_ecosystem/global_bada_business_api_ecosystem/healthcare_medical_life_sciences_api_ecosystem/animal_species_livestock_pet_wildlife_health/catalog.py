"""Catalog metadata for Pets, Livestock, Wildlife & Species Health."""
CATEGORY_ID = "animal_species_livestock_pet_wildlife_health"
CATEGORY_NAME = "Pets, Livestock, Wildlife & Species Health"
DESCRIPTION = "Species-specific medicine for pets, farm animals, birds, aquatic animals and wildlife."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
