"""Provider-neutral software domain taxonomy."""

DOMAINS = {
    "CREATIVE": ("design", "video", "audio", "publishing", "digital_assets"),
    "DOCUMENTS": ("authoring", "pdf", "spreadsheets", "presentations"),
    "OPERATING_SYSTEMS": ("desktop", "mobile", "device_platforms"),
    "CLOUD": ("compute", "storage", "networking", "managed_services"),
    "DEVELOPER_TOOLS": ("source_control", "ci_cd", "ide", "package_registry"),
    "WORK_MANAGEMENT": ("projects", "issues", "knowledge_management", "service_management"),
    "PRODUCTIVITY": ("communication", "collaboration", "office_suite"),
    "SECURITY": ("identity", "access_control", "secrets", "compliance"),
    "DATA": ("databases", "analytics", "integration", "governance"),
}

def list_domains() -> dict[str, tuple[str, ...]]:
    return {key: tuple(value) for key, value in DOMAINS.items()}
