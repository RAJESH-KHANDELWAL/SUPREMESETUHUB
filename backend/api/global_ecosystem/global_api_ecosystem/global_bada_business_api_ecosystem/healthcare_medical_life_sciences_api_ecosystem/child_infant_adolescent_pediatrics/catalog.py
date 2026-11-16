"""Catalog metadata for Infant, Child & Adolescent Healthcare."""
CATEGORY_ID = "child_infant_adolescent_pediatrics"
CATEGORY_NAME = "Infant, Child & Adolescent Healthcare"
DESCRIPTION = "Neonatal care, paediatrics, growth, development, adolescent medicine and child health."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
