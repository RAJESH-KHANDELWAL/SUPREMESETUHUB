"""Owner-curated Bada Business public link registry; no credentials or assumed URLs."""

LINKS = ()

VALID_STATUSES = {"pending_review", "verified_official", "active", "retired"}
VALID_TYPES = {
    "official_website", "course", "product", "service", "referral",
    "affiliate", "partner", "support", "api_documentation",
    "developer_portal", "other",
}

def list_links(*, link_type=None, include_retired=False):
    result = [dict(item) for item in LINKS]
    if link_type:
        result = [item for item in result if item.get("link_type") == link_type]
    if not include_retired:
        result = [item for item in result if item.get("status") != "retired"]
    return result

def get_link(link_id):
    row = next((item for item in LINKS if item.get("id") == link_id), None)
    return dict(row) if row is not None else None

def validate_links():
    ids = [str(item.get("id", "")) for item in LINKS]
    errors = []
    for item in LINKS:
        if item.get("status") not in VALID_STATUSES:
            errors.append(f'{item.get("id")}: invalid status')
        if item.get("link_type") not in VALID_TYPES:
            errors.append(f'{item.get("id")}: invalid link type')
        url = str(item.get("url", ""))
        if not url.startswith("https://"):
            errors.append(f'{item.get("id")}: URL must use HTTPS')
        for field in ("id", "title", "link_type", "url", "source"):
            if not item.get(field):
                errors.append(f'{item.get("id")}: missing {field}')
    duplicates = sorted({value for value in ids if value and ids.count(value) > 1})
    return {
        "valid": not errors and not duplicates,
        "link_count": len(LINKS),
        "duplicate_ids": duplicates,
        "errors": errors,
        "note": "An empty registry is valid until the owner supplies link records.",
    }
