# ANIME GENERATION INFRA CORE ECOSYSTEM

**Parent:** NSF Winfra Core Ecosystem  
**Package:** `nsfwinfra_anime_generation_core_ecosystem/`  
**Ecosystem ID:** `NSFW-INFRA-ANIME-GENERATION-CORE`

## Scope

Metadata for anime generation styles, prompt presets, model compatibility, scene and character consistency, pipeline configuration, resource requirements and output contracts. Generation engines and provider connections remain outside Core.

## Capability metadata

- `ANIME_STYLE_METADATA`
- `MODEL_COMPATIBILITY`
- `PROMPT_CONFIGURATION`
- `CHARACTER_CONSISTENCY_METADATA`
- `SCENE_CONFIGURATION`
- `GENERATION_PRESETS`
- `RESOURCE_REQUIREMENTS`
- `PIPELINE_METADATA`
- `OUTPUT_CONTRACTS`
- `QUALITY_AND_SAFETY_REFERENCES`

## Package interface

- `manager.py`: canonical package manager, status and capability inventory.
- `__init__.py`: public package exports.

The manager reports `CORE_CATALOG_ONLY`; it does not execute infrastructure operations, persist records, call APIs, or claim verified live connections. Authorization, secrets, transport, execution and persistence remain in their designated layers. Add package files only for concrete additional responsibilities.
