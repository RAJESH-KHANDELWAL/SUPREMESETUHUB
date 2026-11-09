"""Short, reusable keyword foundation for Bharat and global business discovery.

Search volume is not asserted here. Validate priority with Search Console, Trends,
and keyword tools before making volume or ranking claims.
"""

KEYWORD_GROUPS = {
    "CORE_BRAND": [
        "business coach",
        "business consultant",
        "business advisor",
        "independent consultant",
        "global business",
    ],
    "SERVICES": [
        "WordPress developer",
        "website development",
        "SEO services",
        "digital marketing",
        "social media marketing",
        "affiliate marketing",
        "startup mentor",
        "business networking",
        "lead generation",
    ],
    "WORK_AND_GROWTH": [
        "freelance jobs",
        "remote jobs",
        "freelance work",
        "online business",
        "business growth",
        "startup guidance",
        "business collaboration",
    ],
    "BHARAT_INTENT": [
        "business coach India",
        "freelance work India",
        "website developer India",
        "digital marketing India",
        "online business ideas",
        "startup India",
    ],
    "GLOBAL_INTENT": [
        "business coach online",
        "global consulting",
        "remote freelance jobs",
        "website design services",
        "SEO consultant",
        "business partnership",
    ],
}


def keyword_foundation() -> dict:
    """Return concise keyword groups without claiming search-volume rankings."""
    groups = {name: list(values) for name, values in KEYWORD_GROUPS.items()}
    return {
        "success": True,
        "foundation": "SUPREMESETUHUB_MAIN_BASE_FOUNDATION",
        "audience": ["BHARAT", "GLOBAL WORLD"],
        "style": "SHORT_SEARCH_INTENT_KEYWORDS",
        "search_volume_verified": False,
        "groups": groups,
        "keyword_count": sum(len(values) for values in groups.values()),
        "usage": [
            "Use naturally in page titles, service pages, bios, and content topics",
            "Avoid keyword stuffing and repetitive tags",
            "Validate demand and prioritize using Search Console and trend data",
        ],
    }
