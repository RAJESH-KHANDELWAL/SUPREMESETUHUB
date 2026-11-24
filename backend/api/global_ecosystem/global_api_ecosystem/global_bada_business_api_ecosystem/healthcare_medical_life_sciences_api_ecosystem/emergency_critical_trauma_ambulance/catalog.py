"""Catalog metadata for Emergency, Critical, Trauma & Ambulance."""
CATEGORY_ID = "emergency_critical_trauma_ambulance"
CATEGORY_NAME = "Emergency, Critical, Trauma & Ambulance"
DESCRIPTION = "Emergency departments, intensive care, trauma systems, paramedics, ambulance and disaster medicine."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
