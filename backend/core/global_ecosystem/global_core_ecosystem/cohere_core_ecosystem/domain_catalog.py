"""Cohere capability domain taxonomy."""
DOMAINS = {
    "language_understanding": ("classify", "rerank"),
    "text_generation": ("command",),
    "vector_representation": ("embed",),
    "text_processing": ("tokenize",),
}
def list_domains():
    return {name: tuple(items) for name, items in DOMAINS.items()}
