"""Catalog metadata for Kidney, Urinary & Urology Health."""
CATEGORY_ID = "kidney_urinary_urology_health"
CATEGORY_NAME = "Kidney, Urinary & Urology Health"
DESCRIPTION = "Kidneys, bladder, urinary tract, urology and renal replacement care."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
