"""Conservative OpenAI profile adapter.

Only the official corporate website is registered as a source. This module does
not scrape, infer legal identifiers, or claim a live registry connection.
"""
COMPANY_ID = "openai"
CANONICAL_NAME = "OpenAI"
OFFICIAL_WEBSITE = "https://openai.com/"

def get_company_profile() -> dict:
    return {
        "success": True,
        "company_id": COMPANY_ID,
        "canonical_name": CANONICAL_NAME,
        "record_type": "company",
        "profile_status": "source_registered_unverified",
        "data_status": "no_verified_profile_record",
        "description": None,
        "sources": [{
            "source_id": "openai_official_website",
            "source_type": "official_website",
            "url": OFFICIAL_WEBSITE,
            "authority": "company_published_source",
            "live_connection": False,
        }],
        "limitations": [
            "No independently verified legal-entity record is stored in this module.",
            "No live company registry, filing, or provider integration is connected.",
            "The official website is a discovery source, not proof of jurisdiction or legal status.",
        ],
    }

def get_source_registry() -> dict:
    profile = get_company_profile()
    return {"company_id": COMPANY_ID, "count": len(profile["sources"]), "sources": profile["sources"]}
