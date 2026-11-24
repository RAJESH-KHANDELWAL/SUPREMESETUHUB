"""Supported capability identifiers; does not imply API availability."""
CAPABILITIES = {
    "classify": {"module": "cohere_classify_core_ecosystem", "mode": "contract_only"},
    "command": {"module": "cohere_command_core_ecosystem", "mode": "contract_only"},
    "embed": {"module": "cohere_embed_core_ecosystem", "mode": "contract_only"},
    "rerank": {"module": "cohere_rerank_core_ecosystem", "mode": "contract_only"},
    "tokenize": {"module": "cohere_tokenize_core_ecosystem", "mode": "contract_only"},
}
