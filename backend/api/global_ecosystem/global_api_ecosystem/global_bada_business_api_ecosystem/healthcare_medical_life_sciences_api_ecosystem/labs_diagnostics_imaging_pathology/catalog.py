"""Catalog metadata for Laboratories, Diagnostics & Medical Imaging."""
CATEGORY_ID = "labs_diagnostics_imaging_pathology"
CATEGORY_NAME = "Laboratories, Diagnostics & Medical Imaging"
DESCRIPTION = "Pathology, laboratory testing, radiology, imaging, screening and diagnostic workflows."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
