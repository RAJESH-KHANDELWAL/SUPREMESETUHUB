"""Private SUPREME identity/profile helpers used by backend APIs."""

from backend.supreme.config import (
    PERSON_ID,
    INTERNAL_USER_ID,
    USERNAME,
    DISPLAY_NAME,
    BUSINESS_ID,
    COMPANY_ID,
    SUPREME_ID,
    EMAILS,
    ALIAS_NAMES,
)


def normalize(value: object) -> str:
    return str(value).strip().lower()


def get_supreme_profile() -> dict:
    return {
        "supreme_id": SUPREME_ID,
        "owner_person_id": PERSON_ID,
        "owner_internal_user_id": INTERNAL_USER_ID,
        "username": USERNAME,
        "display_name": DISPLAY_NAME,
        "business_id": BUSINESS_ID,
        "company_id": COMPANY_ID,
        "emails": EMAILS,
        "aliases": ALIAS_NAMES,
        "role": "SUPREME_OWNER",
        "status": "active",
    }


def get_person_profile() -> dict:
    return {
        "person_id": PERSON_ID,
        "internal_user_id": INTERNAL_USER_ID,
        "username": USERNAME,
        "display_name": DISPLAY_NAME,
        "business_id": BUSINESS_ID,
        "company_id": COMPANY_ID,
        "supreme_id": SUPREME_ID,
        "emails": EMAILS,
        "aliases": ALIAS_NAMES,
        "role": "SUPREME_OWNER",
        "status": "active",
    }


def search_entities(query: str) -> list[dict]:
    q = normalize(query)
    results = []

    if q and q in normalize(USERNAME):
        results.append({
            "type": "PERSON",
            "person_id": PERSON_ID,
            "username": USERNAME,
            "display_name": DISPLAY_NAME,
        })

    for alias in ALIAS_NAMES:
        if q and q in normalize(alias):
            results.append({
                "type": "ALIAS",
                "label": alias,
                "person_id": PERSON_ID,
                "supreme_id": SUPREME_ID,
            })

    # Email search only sees private values injected at deployment runtime.
    for email in EMAILS:
        if q and q in normalize(email):
            results.append({
                "type": "EMAIL",
                "email": email,
                "person_id": PERSON_ID,
                "supreme_id": SUPREME_ID,
            })

    if not results:
        results.append({
            "type": "EMPTY",
            "query": query,
            "message": "No exact entity match found",
        })

    return results
