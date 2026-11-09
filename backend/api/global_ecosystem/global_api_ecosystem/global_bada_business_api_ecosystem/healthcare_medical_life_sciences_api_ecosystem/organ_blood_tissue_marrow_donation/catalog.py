"""Catalog metadata for Organ, Blood, Tissue & Marrow Donation."""
CATEGORY_ID = "organ_blood_tissue_marrow_donation"
CATEGORY_NAME = "Organ, Blood, Tissue & Marrow Donation"
DESCRIPTION = "Blood banks, organ and tissue donation, stem-cell and marrow registries, transplant coordination and donor safeguards."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
