"""Catalog metadata for Women, Gynaecology & Maternity."""
CATEGORY_ID = "women_obgyn_pregnancy_maternity"
CATEGORY_NAME = "Women, Gynaecology & Maternity"
DESCRIPTION = "Women's health, gynaecology, pregnancy, childbirth, postpartum and maternal medicine."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
