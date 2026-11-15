"""Catalog metadata for Hospitals, Clinics, Doctors & Nursing."""
CATEGORY_ID = "hospitals_clinics_doctors_nursing"
CATEGORY_NAME = "Hospitals, Clinics, Doctors & Nursing"
DESCRIPTION = "Healthcare facilities, medical professionals, nurses, clinical departments, appointments and care operations."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
