"""Cohere provider API ecosystem metadata and family listing."""

PROVIDER_API_ECOSYSTEM = {
    "provider_id": "cohere",
    "name": "COHERE API ECOSYSTEM",
    "vendor": "Cohere",
    "families": ["AI", "DEVELOPER"],
    "api_families": [
        "COMMAND",
        "EMBED",
        "RERANK",
        "TOKENIZE_AND_MODEL_METADATA",
        "CLASSIFICATION_WHERE_SUPPORTED",
    ],
    "api_family_paths": [
        "cohere_command_api_ecosystem",
        "cohere_embed_api_ecosystem",
        "cohere_rerank_api_ecosystem",
        "cohere_tokenize_api_ecosystem",
        "cohere_classify_api_ecosystem",
    ],
    "scope": (
        "Cohere model inference, embeddings, reranking and supported related "
        "language AI APIs. Confirm current endpoint/model availability and account access."
    ),
    "status": "CONFIGURATION_READINESS_SCAFFOLD",
    "live_connection_verified": False,
}


def list_cohere_api_ecosystems():
    """Return declared Cohere API families."""
    return list(PROVIDER_API_ECOSYSTEM["api_families"])


def get_cohere_api_ecosystem():
    """Return a safe shallow copy of Cohere provider metadata."""
    return {
        **PROVIDER_API_ECOSYSTEM,
        "families": list(PROVIDER_API_ECOSYSTEM["families"]),
        "api_families": list(PROVIDER_API_ECOSYSTEM["api_families"]),
        "api_family_paths": list(PROVIDER_API_ECOSYSTEM["api_family_paths"]),
    }
