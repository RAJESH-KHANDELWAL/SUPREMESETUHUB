"""Cohere product/capability domain catalog; not a live API contract."""
from types import MappingProxyType
from .constants import (
    PROVIDER_ID, PROVIDER_NAME, DOMAIN_VERSION, STATUS_CATALOG_ONLY,
    PRODUCT_COMMAND, PRODUCT_EMBED, PRODUCT_RERANK, PRODUCT_CLASSIFY,
    PRODUCT_TOKENIZE, PRODUCT_MODEL_METADATA,
)
from .models import CohereProduct

COHERE_PRODUCTS = MappingProxyType({
    PRODUCT_COMMAND: CohereProduct(PRODUCT_COMMAND, "Command", "Text generation and conversational inference.", "Cohere Command API", ("generation", "chat", "rag")),
    PRODUCT_EMBED: CohereProduct(PRODUCT_EMBED, "Embed", "Text and supported multimodal/document embeddings.", "Cohere Embed API", ("semantic_search", "retrieval", "rag")),
    PRODUCT_RERANK: CohereProduct(PRODUCT_RERANK, "Rerank", "Relevance scoring and ordering of candidate documents.", "Cohere Rerank API", ("search", "retrieval", "rag")),
    PRODUCT_CLASSIFY: CohereProduct(PRODUCT_CLASSIFY, "Classify", "Classification where the selected API/model/account supports it.", "Cohere Classify API", ("classification",)),
    PRODUCT_TOKENIZE: CohereProduct(PRODUCT_TOKENIZE, "Tokenize", "Tokenization and token-count workflows where exposed by supported APIs/SDK.", "Cohere Tokenization API/SDK", ("input_estimation",)),
    PRODUCT_MODEL_METADATA: CohereProduct(PRODUCT_MODEL_METADATA, "Model Metadata", "Discover model metadata only through currently documented supported endpoints.", "Cohere model metadata surface", ("model_discovery",)),
})

COHERE_CAPABILITIES = MappingProxyType({
    "text_generation": (PRODUCT_COMMAND, "Generate text using an available Command model."),
    "chat_completion": (PRODUCT_COMMAND, "Create conversational responses using an available Command model."),
    "text_embeddings": (PRODUCT_EMBED, "Create embeddings for supported text inputs."),
    "multimodal_embeddings": (PRODUCT_EMBED, "Create embeddings for supported multimodal inputs when enabled."),
    "document_reranking": (PRODUCT_RERANK, "Rerank candidate documents by relevance to a query."),
    "text_classification": (PRODUCT_CLASSIFY, "Classify text where officially supported."),
    "token_counting": (PRODUCT_TOKENIZE, "Estimate or inspect tokenization using supported tooling."),
    "model_discovery": (PRODUCT_MODEL_METADATA, "Discover documented model identifiers and metadata."),
})

COHERE_PROVIDER = MappingProxyType({
    "provider_id": PROVIDER_ID,
    "provider_name": PROVIDER_NAME,
    "domain_version": DOMAIN_VERSION,
    "status": STATUS_CATALOG_ONLY,
    "products": tuple(COHERE_PRODUCTS),
    "api_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/cohere_api_ecosystem",
    "ai_provider_path": "backend/global_ecosystem/global_ai_ecosystem/cohere_ecosystem",
    "engine_path": "backend/engine/global_ecosystem/global_engine_ecosystem/cohere_engine_ecosystem",
    "integration_adapter_path": "backend/integration/provider/cohere.py",
    "live_connection_verified": False,
})

def get_product(product_id: str) -> CohereProduct:
    key = str(product_id or "").strip().lower()
    try:
        return COHERE_PRODUCTS[key]
    except KeyError as exc:
        raise KeyError(f"Unknown Cohere product: {product_id}") from exc

def list_products() -> tuple[CohereProduct, ...]:
    return tuple(COHERE_PRODUCTS.values())

def list_capabilities(product_id: str | None = None) -> tuple[dict, ...]:
    rows = tuple(
        {"capability_id": key, "product_id": value[0], "description": value[1]}
        for key, value in COHERE_CAPABILITIES.items()
    )
    if product_id is None:
        return rows
    key = str(product_id).strip().lower()
    return tuple(row for row in rows if row["product_id"] == key)
