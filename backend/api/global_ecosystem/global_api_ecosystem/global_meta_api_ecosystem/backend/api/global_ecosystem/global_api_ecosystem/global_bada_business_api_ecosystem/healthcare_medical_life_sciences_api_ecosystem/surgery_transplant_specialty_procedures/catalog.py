"""Catalog metadata for Surgery, Transplant & Specialist Procedures."""
CATEGORY_ID = "surgery_transplant_specialty_procedures"
CATEGORY_NAME = "Surgery, Transplant & Specialist Procedures"
DESCRIPTION = "Surgical specialties, anaesthesia, operating theatres, transplant surgery and post-operative care."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
