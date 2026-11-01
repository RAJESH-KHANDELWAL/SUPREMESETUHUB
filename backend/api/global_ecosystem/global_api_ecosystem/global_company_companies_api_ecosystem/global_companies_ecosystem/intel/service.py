"""Source-aware service layer for Intel company profile discovery."""
COMPANY_ID = "intel"
CANONICAL_NAME = "Intel"
OFFICIAL_WEBSITE = "https://www.intel.com/"

def get_profile() -> dict:
    return {
        "company_id": COMPANY_ID,
        "canonical_name": CANONICAL_NAME,
        "record_type": "company",
        "profile_status": "source_registered_unverified",
        "data_status": "no_verified_legal_entity_record",
        "sources": [{
            "source_id": f"{COMPANY_ID}_official_website",
            "source_type": "official_website",
            "url": OFFICIAL_WEBSITE,
            "authority": "company_published_source",
            "live_connection": False,
        }],
        "limitations": [
            "This entry identifies a company brand, not a verified legal entity.",
            "No jurisdiction-specific registry record or filing has been independently verified.",
            "No live API, scraping, cloud-provider, or government-registry connection is enabled.",
            "The official website is a discovery source and does not prove legal status or ownership.",
        ],
    }

def get_sources() -> dict:
    profile = get_profile()
    return {"company_id": COMPANY_ID, "count": len(profile["sources"]), "sources": profile["sources"]}

def get_adapter_status() -> dict:
    return {
        "company_id": COMPANY_ID,
        "adapter": "metadata_only",
        "configured": True,
        "live_connection": False,
        "authentication_configured": False,
        "last_sync": None,
        "status": "not_connected",
    }
