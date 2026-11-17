"""Catalog metadata for Digital Health, Telemedicine & Health AI."""
CATEGORY_ID = "digital_health_telemedicine_ai_records"
CATEGORY_NAME = "Digital Health, Telemedicine & Health AI"
DESCRIPTION = "Telehealth, health software, AI decision support, electronic records, interoperability and cybersecurity."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
