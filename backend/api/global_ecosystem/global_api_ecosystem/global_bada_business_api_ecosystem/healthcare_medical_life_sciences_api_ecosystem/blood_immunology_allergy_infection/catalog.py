"""Catalog metadata for Blood, Immunology, Allergy & Infection."""
CATEGORY_ID = "blood_immunology_allergy_infection"
CATEGORY_NAME = "Blood, Immunology, Allergy & Infection"
DESCRIPTION = "Haematology, immune system, allergies, infectious diseases and clinical immunology."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
