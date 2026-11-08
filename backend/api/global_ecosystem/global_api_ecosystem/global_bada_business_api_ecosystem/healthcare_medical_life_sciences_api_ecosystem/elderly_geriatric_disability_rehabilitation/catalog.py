"""Catalog metadata for Elderly, Geriatric & Rehabilitation Care."""
CATEGORY_ID = "elderly_geriatric_disability_rehabilitation"
CATEGORY_NAME = "Elderly, Geriatric & Rehabilitation Care"
DESCRIPTION = "Ageing, geriatric medicine, disability support, physiotherapy, occupational and rehabilitation care."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
