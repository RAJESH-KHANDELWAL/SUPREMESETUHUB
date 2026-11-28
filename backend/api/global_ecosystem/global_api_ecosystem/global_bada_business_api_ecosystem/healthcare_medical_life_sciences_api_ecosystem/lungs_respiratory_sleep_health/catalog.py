"""Catalog metadata for Lungs, Respiratory & Sleep Health."""
CATEGORY_ID = "lungs_respiratory_sleep_health"
CATEGORY_NAME = "Lungs, Respiratory & Sleep Health"
DESCRIPTION = "Pulmonology, airway, lungs, breathing, respiratory disease and sleep medicine."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
