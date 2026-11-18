"""Translation workflow categories, including sensitive-domain review."""
WORKFLOWS = {
    "general": ("websites", "documents", "apps", "customer_support"),
    "business_and_commerce": ("contracts", "product_catalogs", "marketing", "invoices"),
    "public_and_civic": ("government_services", "forms", "public_information"),
    "health_and_wellbeing": ("patient_information", "sexual_health_education", "wellbeing_material"),
    "media_and_entertainment": ("subtitles", "captions", "metadata", "scripts"),
    "adult_restricted": ("adult_content_metadata", "lawful_adult_material_translation"),
}

def get_translation_workflows() -> dict[str, tuple[str, ...]]:
    return dict(WORKFLOWS)
