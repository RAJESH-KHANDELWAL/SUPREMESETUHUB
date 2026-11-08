"""Catalog metadata for Pharmacy, Medicines, Vaccines & Devices."""
CATEGORY_ID = "pharmacy_medicines_vaccines_devices"
CATEGORY_NAME = "Pharmacy, Medicines, Vaccines & Devices"
DESCRIPTION = "Pharmacies, medicines, vaccines, medical devices, equipment and pharmacovigilance."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
