"""Catalog metadata for Sexual, Reproductive & Fertility Medicine."""
CATEGORY_ID = "sexual_reproductive_fertility_ivf"
CATEGORY_NAME = "Sexual, Reproductive & Fertility Medicine"
DESCRIPTION = "Clinical sexual medicine, reproductive health, fertility, infertility, IVF and assisted reproduction."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
