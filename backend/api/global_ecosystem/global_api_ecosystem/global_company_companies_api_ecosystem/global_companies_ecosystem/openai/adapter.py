"""Functional, source-aware adapter for the OpenAI company directory entry."""
from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl
COMPANY_ID = "openai"
DISPLAY_NAME = "OpenAI"
OFFICIAL_WEBSITE = "https://openai.com/"
class SourceRecord(BaseModel):
    source_id: str
    source_type: str
    url: HttpUrl
    authority: str
    live_connection: bool = False
class CompanyProfile(BaseModel):
    success: bool = True
    company_id: str
    display_name: str
    record_class_candidate: str = "company"
    verification_status: str = "unverified"
    profile_status: str = "source_registered_unverified"
    data_status: str = "no_verified_profile_record"
    sources: list[SourceRecord]
    capabilities: list[str]
    limitations: list[str]
def get_profile() -> dict:
    return {"success": True, "company_id": COMPANY_ID, "display_name": DISPLAY_NAME,
        "record_class_candidate": "company", "verification_status": "unverified",
        "profile_status": "source_registered_unverified", "data_status": "no_verified_profile_record",
        "sources": [{"source_id": f"{COMPANY_ID}_official_website", "source_type": "official_website",
            "url": OFFICIAL_WEBSITE, "authority": "company_published_discovery_source", "live_connection": False}],
        "capabilities": ["profile_metadata", "source_provenance", "verification_state"],
        "limitations": ["This directory entry is not proof of a registered legal entity.",
            "No government registry, filings, ownership data, or live provider API is connected.",
            "The official website is a discovery source; legal identity and jurisdiction require verification."]}
def get_sources() -> dict:
    profile = get_profile()
    return {"company_id": COMPANY_ID, "count": len(profile["sources"]), "live_connections": 0, "sources": profile["sources"]}
router = APIRouter(prefix=f"/global/company-directory/company-profiles/{COMPANY_ID}", tags=[f"Company Profile: {DISPLAY_NAME}"])
@router.get("", response_model=CompanyProfile)
def company_profile():
    return get_profile()
@router.get("/sources")
def company_sources():
    return get_sources()
@router.get("/status")
def company_adapter_status():
    return {"company_id": COMPANY_ID, "adapter": "implemented", "profile_data": "unverified", "live_connection": False}
