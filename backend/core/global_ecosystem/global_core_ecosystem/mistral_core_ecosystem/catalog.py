"""Canonical Mistral provider and product-family registry; metadata only."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ROOT_ID = "MISTRAL-CORE-ECOSYSTEM"
ROOT_PATH = "backend/core/global_ecosystem/global_core_ecosystem/mistral_core_ecosystem"
API_ROOT = "backend/api/global_ecosystem/global_api_ecosystem/mistral_api_ecosystem"
ENGINE_ROOT = "backend/engine/global_ecosystem/global_engine_ecosystem/global_ai_engine_ecosystem/mistral_ai_engine_ecosystem"
RUNTIME_ROOT = "backend/global_ecosystem/global_ai_ecosystem/mistral_ecosystem"

_PRODUCTS: tuple[dict[str, Any], ...] = (
 {"key":"agents","ecosystem_id":"MISTRAL-AGENTS-CORE-ECOSYSTEM","name":"Mistral Agents","directory":"mistral_agents_core_ecosystem","api_directory":"mistral_agents_api_ecosystem","domains":["AGENT_ORCHESTRATION","TOOL_USE_AND_HANDOFF"],"capabilities":["AGENT_DEFINITION_METADATA","TOOL_REGISTRY_METADATA","HANDOFF_POLICY_METADATA","AGENT_READINESS_DISCOVERY"]},
 {"key":"audio","ecosystem_id":"MISTRAL-AUDIO-CORE-ECOSYSTEM","name":"Mistral Audio","directory":"mistral_audio_core_ecosystem","api_directory":"mistral_audio_api_ecosystem","domains":["AUDIO_AND_SPEECH"],"capabilities":["AUDIO_CAPABILITY_DISCOVERY","SPEECH_TASK_METADATA","AUDIO_READINESS_DISCOVERY"]},
 {"key":"batch","ecosystem_id":"MISTRAL-BATCH-CORE-ECOSYSTEM","name":"Mistral Batch","directory":"mistral_batch_core_ecosystem","api_directory":"mistral_batch_api_ecosystem","domains":["BATCH_AND_ASYNC_JOBS"],"capabilities":["BATCH_JOB_METADATA","BATCH_LIFECYCLE_METADATA","BATCH_READINESS_DISCOVERY"]},
 {"key":"chat","ecosystem_id":"MISTRAL-CHAT-CORE-ECOSYSTEM","name":"Mistral Chat","directory":"mistral_chat_core_ecosystem","api_directory":"mistral_chat_api_ecosystem","domains":["CHAT_AND_TEXT_GENERATION","STRUCTURED_OUTPUTS","SAFETY_AND_GOVERNANCE"],"capabilities":["CHAT_COMPLETION_METADATA","CONVERSATION_CAPABILITY_DISCOVERY","STRUCTURED_OUTPUT_METADATA","CONTENT_SAFETY_POLICY_METADATA"]},
 {"key":"embeddings","ecosystem_id":"MISTRAL-EMBEDDINGS-CORE-ECOSYSTEM","name":"Mistral Embeddings","directory":"mistral_embeddings_core_ecosystem","api_directory":"mistral_embeddings_api_ecosystem","domains":["EMBEDDINGS_AND_SEMANTIC_SEARCH"],"capabilities":["EMBEDDING_MODEL_METADATA","VECTOR_DIMENSION_METADATA","SEMANTIC_SEARCH_CAPABILITY_DISCOVERY"]},
 {"key":"fim_completions","ecosystem_id":"MISTRAL-FIM-COMPLETIONS-CORE-ECOSYSTEM","name":"Mistral FIM Completions","directory":"mistral_fim_completions_core_ecosystem","api_directory":"mistral_fim_completions_api_ecosystem","domains":["CODE_AND_FIM_COMPLETION"],"capabilities":["FIM_COMPLETION_METADATA","CODE_MODEL_DISCOVERY","CODE_COMPLETION_POLICY_METADATA"]},
 {"key":"fine_tuning","ecosystem_id":"MISTRAL-FINE-TUNING-CORE-ECOSYSTEM","name":"Mistral Fine-tuning","directory":"mistral_fine_tuning_core_ecosystem","api_directory":"mistral_fine_tuning_api_ecosystem","domains":["MODEL_ADAPTATION_AND_FINE_TUNING"],"capabilities":["FINE_TUNING_JOB_METADATA","TRAINING_CONFIGURATION_METADATA","MODEL_ADAPTATION_READINESS_DISCOVERY"]},
 {"key":"models","ecosystem_id":"MISTRAL-MODELS-CORE-ECOSYSTEM","name":"Mistral Models","directory":"mistral_models_core_ecosystem","api_directory":"mistral_models_api_ecosystem","domains":["MODEL_CATALOG_AND_LIFECYCLE","TOKEN_CONTEXT_AND_CAPACITY"],"capabilities":["MODEL_CATALOG_DISCOVERY","MODEL_VERSION_METADATA","MODEL_CAPABILITY_METADATA","MODEL_LIFECYCLE_METADATA"]},
 {"key":"ocr","ecosystem_id":"MISTRAL-OCR-CORE-ECOSYSTEM","name":"Mistral OCR","directory":"mistral_ocr_core_ecosystem","api_directory":"mistral_ocr_api_ecosystem","domains":["OCR_AND_DOCUMENT_INTELLIGENCE"],"capabilities":["OCR_MODEL_METADATA","DOCUMENT_EXTRACTION_CAPABILITY_DISCOVERY","DOCUMENT_PROCESSING_POLICY_METADATA"]},
)

def get_mistral_core_catalog() -> dict[str, Any]:
 """Return a defensive copy of the provider and its nine existing packages."""
 children=[]
 for item in _PRODUCTS:
  row=deepcopy(item)
  row.update({"ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":ROOT_ID,
   "core_module":f"{ROOT_PATH}/{item['directory']}",
   "api_catalog_ref":f"{API_ROOT}/{item['api_directory']}",
   "status":"CORE_CATALOG_ONLY","enabled":True,"connected":False,"live_connection_verified":False})
  children.append(row)
 return {"ecosystem_id":ROOT_ID,"name":"MISTRAL CORE ECOSYSTEM","provider":"mistral","vendor":"Mistral AI",
  "ecosystem_type":"PROVIDER_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","status":"CORE_CATALOG_ONLY","enabled":True,
  "core_path":ROOT_PATH,"api_catalog_ref":API_ROOT,"engine_ref":ENGINE_ROOT,"runtime_ref":RUNTIME_ROOT,
  "capabilities":["MISTRAL_PROVIDER_REGISTRY","MODEL_AND_PRODUCT_DISCOVERY","AI_CAPABILITY_TAXONOMY",
   "TENANT_SCOPED_POLICY_METADATA","READINESS_AND_DEPENDENCY_DISCOVERY","READ_ONLY_MASTER_CATALOG_MAPPING"],
  "children":children}

__all__=["ROOT_ID","ROOT_PATH","API_ROOT","ENGINE_ROOT","RUNTIME_ROOT","get_mistral_core_catalog"]
