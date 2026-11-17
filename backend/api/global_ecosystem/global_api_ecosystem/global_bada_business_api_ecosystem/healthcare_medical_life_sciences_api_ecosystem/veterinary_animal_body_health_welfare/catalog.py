"""Catalog metadata for Veterinary, Animal Anatomy & Welfare."""
CATEGORY_ID = "veterinary_animal_body_health_welfare"
CATEGORY_NAME = "Veterinary, Animal Anatomy & Welfare"
DESCRIPTION = "Animal body systems, veterinary doctors, clinics, hospitals, diagnosis, surgery and welfare."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
