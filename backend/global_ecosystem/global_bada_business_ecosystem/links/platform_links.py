"""Canonical Bada Business official/referral destination registry.

URLs below were supplied by the repository owner. Their presence records
destinations only; it does not assert that every page is currently active,
officially endorsed, or commercially available.
"""

PLATFORM_LINKS = [
    {
        "id": "nice_analysis",
        "name": "Nice Analysis",
        "url": "https://www.badabusiness.com/nice-analysis?pp_code=BIRK076336",
        "type": "PROGRAM_OR_RESOURCE",
        "source": "user_provided_url",
    },
    {
        "id": "business_breakthrough_seminar",
        "name": "Business Breakthrough Seminar",
        "url": "https://www.badabusiness.com/business-breakthrough-seminar?pp_code=BIRK076336",
        "type": "EVENT_OR_SEMINAR",
        "source": "user_provided_url",
    },
    {
        "id": "idea_to_ipo",
        "name": "Idea to IPO",
        "url": "https://www.badabusiness.com/ideatoipo/?pp_code=BIRK076336",
        "type": "WEBINAR_OR_PROGRAM",
        "availability": "recheck current sessions",
        "source": "user_provided_url",
    },
    {
        "id": "lfp_digital",
        "name": "LFP Digital",
        "url": "https://www.badabusiness.com/lfp?pp_code=BIRK076336",
        "type": "PROGRAM",
        "source": "existing_repository_link_and_user_provided_url",
    },
    {
        "id": "bb_coach",
        "name": "Bada Business Coach",
        "url": "https://www.badabusiness.com/bb-coach?pp_code=BIRK076336",
        "type": "COACHING_OR_PROGRAM",
        "source": "user_provided_url",
    },
    {
        "id": "digital_daily_event",
        "name": "Digital Daily Event",
        "url": "https://www.badabusiness.com/workshop/digital/daily_event?pp_code=BIRK076336",
        "type": "WORKSHOP_OR_EVENT",
        "source": "user_provided_url",
    },
    {
        "id": "cash_growth_profit",
        "name": "Cash Growth Profit",
        "url": "https://www.badabusiness.com/cash-growth-profit?pp_code=BIRK076336",
        "type": "PROGRAM",
        "source": "existing_repository_link_and_user_provided_url",
    },
    {
        "id": "business_tales",
        "name": "Business Tales",
        "url": "https://www.badabusiness.com/business-tales?pp_code=BIRK076336",
        "type": "BUSINESS_CONTENT",
        "source": "user_provided_url",
    },
    {
        "id": "digital_dukan",
        "name": "Digital Dukan",
        "url": "https://www.badabusiness.com/digitaldukan/BIRK076336",
        "type": "DIGITAL_STORE",
        "source": "existing_repository_link",
    },
]


def list_platform_links() -> list[dict[str, str]]:
    """Return a copy of the canonical Bada Business destination records."""
    return [dict(link) for link in PLATFORM_LINKS]
