"""Stable identity and master catalog reference."""
ECOSYSTEM_ID = "GLOBAL-DIGITAL-INFRASTRUCTURE-TELECOMMUNICATIONS-TECHNOLOGY-IT-AI-SERVICE-WORK-BUSINESS-CORE"
PARENT_ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM"
VERSION = "1.0.0"

def get_catalog() -> dict:
    return {"ecosystem_id": ECOSYSTEM_ID, "name": "Global Digital Infrastructure Telecommunications Technology IT AI Service Work Business CORE Ecosystem", "parent_id": PARENT_ECOSYSTEM_ID, "version": VERSION, "master_catalog": {"catalogue_id": "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM", "source_path": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json", "target_unique_entries": 2468, "access_mode": "READ_ONLY_ON_DEMAND"}}
