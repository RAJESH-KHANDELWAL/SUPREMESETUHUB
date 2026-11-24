"""Catalog metadata for Cancer, Oncology & Palliative Care."""
CATEGORY_ID = "cancer_oncology_palliative_care"
CATEGORY_NAME = "Cancer, Oncology & Palliative Care"
DESCRIPTION = "Cancer prevention, screening, diagnosis, oncology, survivorship, pain and palliative care."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
