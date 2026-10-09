from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from supreme_config import (
    APP_NAME,
    BUSINESS_ID,
    COMPANY_ID,
    PERSON_ID,
    SUPREME_ID,
)

from identity_service import (
    get_supreme_profile,
    get_person_profile,
    search_entities,
)


router = APIRouter(
    prefix="/supreme",
    tags=["SUPREME DASHBOARD"],
)


IDENTITIES = [
    {
        "display_name": "👑 RAJESH KHANDELWAL 👑",
        "username": "RAJESHKHANDELWAL",
        "domain": "https://rajeshkhandelwal.com",
    },
    {
        "display_name": "👑 RAJESH KHANDELWAL OFFICIAL 👑",
        "username": "RAJESHKHANDELWALOFFICIAL",
        "domain": "https://rajeshkhandelwalofficial.com",
    },
    {
        "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
        "username": "DRRAJESHKHANDELWALIBC",
        "domain": "https://drrajeshkhandelwalibc.com",
    },
    {
        "display_name": "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑",
        "username": "DRRAJESHKHANDELWALIBCOFFICIAL",
        "domain": "https://drrajeshkhandelwalibcofficial.com",
    },
]


@router.get("/")
def supreme_dashboard():
    return {
        "success": True,
        "dashboard": "👑 SUPREME DASHBOARD 👑",
        "system": APP_NAME,
        "version": "1.0.0",
        "status": "active",
        "access": "SUPREME",
        "owner": "👑 DR RAJESH KHANDELWAL IBC 👑",
        "identity_count": len(IDENTITIES),
    }


@router.get("/identities")
def supreme_identities():
    return {
        "success": True,
        "dashboard": "👑 SUPREME DASHBOARD 👑",
        "total": len(IDENTITIES),
        "identities": IDENTITIES,
    }


@router.get("/status")
def supreme_status():
    profile = get_supreme_profile()

    return {
        "service": APP_NAME,
        "status": "active",
        "supreme_id": profile["supreme_id"],
        "owner_person_id": profile["owner_person_id"],
        "business_id": BUSINESS_ID,
        "company_id": COMPANY_ID,
        "role": profile["role"],
        "success": True,
        "api": "connected",
        "people_dashboard": "active",
        "supreme_dashboard": "active",
        "backend": "connected",
    }


@router.get("/health")
def supreme_health():
    return {
        "success": True,
        "dashboard": "👑 SUPREME DASHBOARD 👑",
        "service": APP_NAME,
        "supreme_id": SUPREME_ID,
        "status": "healthy",
    }


@router.get("/version")
def supreme_version():
    return {
        "success": True,
        "dashboard": "👑 SUPREME DASHBOARD 👑",
        "version": "1.0.0",
    }


@router.get("/profile")
def supreme_profile():
    return get_supreme_profile()


@router.get("/person")
def supreme_person():
    return get_person_profile()


@router.get("/search")
def supreme_search(
    q: str = Query(default="", max_length=200),
):
    query = q.strip()

    if not query:
        raise HTTPException(
            status_code=400,
            detail="Missing q query parameter",
        )

    results = search_entities(query)

    return {
        "query": query,
        "results": results,
        "count": len(results),
    }


@router.get("/persons")
def persons_list():
    return {
        "service": APP_NAME,
        "people": [get_person_profile()],
    }


@router.get("/businesses")
def businesses_list():
    return {
        "service": APP_NAME,
        "businesses": [
            {
                "business_id": BUSINESS_ID,
                "owner_person_id": PERSON_ID,
                "supreme_id": SUPREME_ID,
                "name": "RAJESH KHANDELWAL OFFICIAL",
                "display_name": "👑 RAJESH KHANDELWAL OFFICIAL 👑",
            }
        ],
    }


@router.get("/companies")
def companies_list():
    return {
        "service": APP_NAME,
        "companies": [
            {
                "company_id": COMPANY_ID,
                "owner_person_id": PERSON_ID,
                "business_id": BUSINESS_ID,
                "supreme_id": SUPREME_ID,
                "name": "DR RAJESH KHANDELWAL IBC",
                "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
            }
        ],
    }
