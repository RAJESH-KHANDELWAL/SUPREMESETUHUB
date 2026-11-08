"""Catalog metadata for Sperm, Egg, Embryo & Donor Services."""
CATEGORY_ID = "sperm_egg_embryo_donor_services"
CATEGORY_NAME = "Sperm, Egg, Embryo & Donor Services"
DESCRIPTION = "Consent-based donor screening, gamete and embryo donation, matching, storage, eligibility and traceability under applicable law."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
