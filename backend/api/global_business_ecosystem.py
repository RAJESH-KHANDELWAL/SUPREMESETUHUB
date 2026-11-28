from datetime import datetime, timezone
from typing import Any

from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/global-business-ecosystem",
    tags=["GLOBAL BUSINESS ECOSYSTEM"],
)


# =========================================================
# OFFICIAL IDENTITY
# =========================================================

GLOBAL_BUSINESS_ECOSYSTEM = "GLOBAL BUSINESS ECOSYSTEM"
SHORT_SEARCH_TERM = "GBE"


# =========================================================
# TWO COMPLETELY SEPARATE CONNECTIONS
# =========================================================

CONNECTIONS = {

    "SUPREMESETUHUB": {
        "connection_id": "GLOBAL-BUSINESS-ECOSYSTEM-SUPREMESETUHUB",

        "name": GLOBAL_BUSINESS_ECOSYSTEM,

        "scope": "SUPREMESETUHUB",

        "search_terms": [
            "GBE",
            "GLOBAL",
            "BUSINESS",
            "ECOSYSTEM",
            "GLOBAL BUSINESS",
            "BUSINESS ECOSYSTEM",
            "GLOBAL BUSINESS ECOSYSTEM",
        ],

        "domains": [
            "SUPREMESETUHUB",
        ],
    },


    "FOUR_OFFICIAL_DOMAINS": {
        "connection_id": "GLOBAL-BUSINESS-ECOSYSTEM-FOUR-OFFICIAL-DOMAINS",

        "name": GLOBAL_BUSINESS_ECOSYSTEM,

        "scope": "FOUR_OFFICIAL_DOMAINS",

        "search_terms": [
            "GBE",
            "GLOBAL",
            "BUSINESS",
            "ECOSYSTEM",
            "GLOBAL BUSINESS",
            "BUSINESS ECOSYSTEM",
            "GLOBAL BUSINESS ECOSYSTEM",
        ],

        "domains": [
            "DOMAIN_1",
            "DOMAIN_2",
            "DOMAIN_3",
            "DOMAIN_4",
        ],
    },
}


# =========================================================
# SEPARATE DATA STORAGE
# =========================================================

CONNECTION_DATA = {
    "SUPREMESETUHUB": {
        "content": {},
        "visitor_events": [],
        "ai_context": [],
    },

    "FOUR_OFFICIAL_DOMAINS": {
        "content": {},
        "visitor_events": [],
        "ai_context": [],
    },
}


# =========================================================
# GET ONE CONNECTION
# =========================================================

@router.get("/{connection}")
def get_connection(connection: str):

    connection = connection.upper()

    if connection not in CONNECTIONS:

        return {
            "success": False,
            "error": "CONNECTION_NOT_FOUND",
        }

    config = CONNECTIONS[connection]

    return {
        "success": True,

        "api": "GLOBAL BUSINESS ECOSYSTEM",

        "name": GLOBAL_BUSINESS_ECOSYSTEM,

        "connection": config,

        "data": CONNECTION_DATA[connection],
    }


# =========================================================
# SEARCH
# =========================================================

@router.get("/{connection}/search")
def search_connection(
    connection: str,
    q: str,
):

    connection = connection.upper()

    if connection not in CONNECTIONS:

        return {
            "success": False,
            "error": "CONNECTION_NOT_FOUND",
        }

    query = " ".join(
        q.strip().upper().split()
    )

    config = CONNECTIONS[connection]

    matches = []

    for term in config["search_terms"]:

        if (
            query == term
            or query in term
            or term in query
        ):
            matches.append(term)

    return {

        "success": True,

        "api": "GLOBAL BUSINESS ECOSYSTEM",

        "name": GLOBAL_BUSINESS_ECOSYSTEM,

        "connection": connection,

        "query": q,

        "matches": matches,

        "page": {
            "name": GLOBAL_BUSINESS_ECOSYSTEM,
            "connection_id": config["connection_id"],
        },
    }


# =========================================================
# RECORD VISITOR EVENT
# =========================================================

@router.post("/{connection}/visitor-event")
def record_visitor_event(
    connection: str,
    event_type: str,
    device: str = "unknown",
    browser: str = "unknown",
    section: str = "unknown",
    action: str = "unknown",
    metadata: dict[str, Any] | None = None,
):

    connection = connection.upper()

    if connection not in CONNECTIONS:

        return {
            "success": False,
            "error": "CONNECTION_NOT_FOUND",
        }

    event = {

        "timestamp": datetime.now(
            timezone.utc
        ).isoformat(),

        "connection": connection,

        "connection_id": CONNECTIONS[
            connection
        ]["connection_id"],

        "page_name": GLOBAL_BUSINESS_ECOSYSTEM,

        "event_type": event_type,

        "device": device,

        "browser": browser,

        "section": section,

        "action": action,

        "metadata": metadata or {},
    }

    CONNECTION_DATA[
        connection
    ]["visitor_events"].append(event)

    return {

        "success": True,

        "page_name": GLOBAL_BUSINESS_ECOSYSTEM,

        "connection": connection,

        "event": event,
    }


# =========================================================
# GET VISITOR EVENTS
# =========================================================

@router.get("/{connection}/visitor-events")
def get_visitor_events(
    connection: str,
):

    connection = connection.upper()

    if connection not in CONNECTIONS:

        return {
            "success": False,
            "error": "CONNECTION_NOT_FOUND",
        }

    events = CONNECTION_DATA[
        connection
    ]["visitor_events"]

    return {

        "success": True,

        "page_name": GLOBAL_BUSINESS_ECOSYSTEM,

        "connection": connection,

        "count": len(events),

        "events": events,
    }
