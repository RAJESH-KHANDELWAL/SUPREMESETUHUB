"""Catalog metadata for Biotechnology, Genomics & Life Sciences."""
CATEGORY_ID = "biotechnology_genomics_life_sciences"
CATEGORY_NAME = "Biotechnology, Genomics & Life Sciences"
DESCRIPTION = "Biotech, genetics, genomics, molecular medicine, bioinformatics and life-science platforms."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
