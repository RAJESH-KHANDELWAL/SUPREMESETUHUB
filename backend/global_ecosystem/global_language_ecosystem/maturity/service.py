"""Progressive maturity stages; stages are planning labels, not certifications."""
STAGES = {
    "basic": ("single-language content", "manual review", "simple glossary"),
    "standard": ("multi-language workflows", "locale validation", "translation memory planning"),
    "advanced": ("workflow automation", "terminology management", "quality metrics"),
    "enterprise": ("role-based governance", "audit trails", "regional operations", "vendor controls"),
    "supreme": ("global language coverage strategy", "continuous evaluation", "resilience", "accessibility governance", "jurisdiction-aware controls"),
}

def get_maturity_stages() -> dict[str, tuple[str, ...]]:
    return dict(STAGES)
