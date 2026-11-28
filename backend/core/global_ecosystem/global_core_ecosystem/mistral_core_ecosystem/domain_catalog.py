"""Mistral capability taxonomy; registration does not imply API readiness."""
from __future__ import annotations
from typing import Any
from .catalog import get_mistral_core_catalog

DOMAIN_DEFINITIONS:dict[str,dict[str,Any]]={
 "PROVIDER_GOVERNANCE":{"name":"Provider Governance","purpose":"Provider identity, product registration, lifecycle and readiness."},
 "MODEL_CATALOG_AND_LIFECYCLE":{"name":"Model Catalog and Lifecycle","purpose":"Model discovery, versions, capability metadata and lifecycle states."},
 "CHAT_AND_TEXT_GENERATION":{"name":"Chat and Text Generation","purpose":"Conversation and text-generation capability metadata and request boundaries."},
 "CODE_AND_FIM_COMPLETION":{"name":"Code and FIM Completion","purpose":"Fill-in-the-middle completion and code-oriented model capability metadata."},
 "EMBEDDINGS_AND_SEMANTIC_SEARCH":{"name":"Embeddings and Semantic Search","purpose":"Embedding model metadata, vector dimensions and retrieval compatibility."},
 "OCR_AND_DOCUMENT_INTELLIGENCE":{"name":"OCR and Document Intelligence","purpose":"Document and image text-extraction capability metadata."},
 "AUDIO_AND_SPEECH":{"name":"Audio and Speech","purpose":"Audio model, speech task and modality capability metadata."},
 "AGENT_ORCHESTRATION":{"name":"Agent Orchestration","purpose":"Agent identity, tool declarations, handoff and orchestration policy metadata."},
 "TOOL_USE_AND_HANDOFF":{"name":"Tool Use and Handoff","purpose":"Tool capability declarations, approval boundaries and handoff metadata."},
 "BATCH_AND_ASYNC_JOBS":{"name":"Batch and Asynchronous Jobs","purpose":"Batch job identity, lifecycle, limits and readiness metadata."},
 "MODEL_ADAPTATION_AND_FINE_TUNING":{"name":"Model Adaptation and Fine-tuning","purpose":"Fine-tuning configuration and job metadata; execution stays outside Core."},
 "STRUCTURED_OUTPUTS":{"name":"Structured Outputs","purpose":"Structured response formats and schema compatibility metadata."},
 "SAFETY_AND_GOVERNANCE":{"name":"Safety and Governance","purpose":"Safety classification, data handling, rights and responsible-use boundaries."},
 "TOKEN_CONTEXT_AND_CAPACITY":{"name":"Token, Context and Capacity","purpose":"Context-window, tokenization and capacity metadata from trusted catalogs."},
 "EVALUATION_AND_QUALITY":{"name":"Evaluation and Quality","purpose":"Evaluation criteria, quality signals and test metadata; execution remains external."},
 "USAGE_QUOTA_AND_BILLING":{"name":"Usage, Quota and Billing","purpose":"Usage and quota metadata; billing transactions remain outside Core."},
 "TENANT_ACCESS_AND_PRIVACY":{"name":"Tenant Access and Privacy","purpose":"Tenant scoping, data minimization, retention and access policy metadata."},
 "API_INTEROPERABILITY":{"name":"API Interoperability","purpose":"References to the separate API layer and provider-neutral integration contracts."},
}

def list_mistral_domain_inventory()->list[dict[str,Any]]:
 mapped={key:[] for key in DOMAIN_DEFINITIONS}
 for product in get_mistral_core_catalog()["children"]:
  for domain_id in product["domains"]: mapped.setdefault(domain_id,[]).append(product["ecosystem_id"])
 return [{"domain_id":key,**value,"product_count":len(mapped.get(key,[])),
  "product_ecosystem_ids":sorted(mapped.get(key,[])),"status":"REGISTERED_METADATA"}
  for key,value in DOMAIN_DEFINITIONS.items()]

def mistral_domain_summary()->dict[str,Any]:
 rows=list_mistral_domain_inventory()
 return {"success":True,"provider":"mistral","domain_count":len(rows),
  "mapped_domain_count":sum(bool(x["product_count"]) for x in rows),
  "unmapped_domain_count":sum(not x["product_count"] for x in rows),"domains":rows}

__all__=["DOMAIN_DEFINITIONS","list_mistral_domain_inventory","mistral_domain_summary"]
