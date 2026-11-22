# IMAGE GENERATION INFRA CORE ECOSYSTEM

Parent: NSF Winfra Core. Package `nsfwinfra_image_generation_core_ecosystem/`. ID: `NSFW-INFRA-IMAGE-GENERATION-CORE`.

## Scope
Metadata for prompts, seeds, aspect ratios, resolution, quality, styles, batches, resources, model/provider compatibility, output formats and safety/rights. No live provider claim.

## Capabilities
- `MODEL_AND_PROVIDER_COMPATIBILITY_METADATA`
- `PROMPT_CONTRACTS`
- `NEGATIVE_PROMPT_METADATA`
- `SEED_CONFIGURATION`
- `ASPECT_RATIOS`
- `RESOLUTION_AND_QUALITY_PRESETS`
- `STYLE_METADATA`
- `BATCH_METADATA`
- `RESOURCE_REQUIREMENTS`
- `PIPELINE_METADATA`
- `OUTPUT_FORMAT_CONTRACTS`
- `QUALITY_AND_SAFETY_REFERENCES`

## Files
- `manager.py`: status and capability metadata interface.
- `__init__.py`: public package exports.

Metadata-only: no execution, API calls, persistence, or live-connectivity claim. Authentication, secrets, transport, runtime and storage remain in their designated layers.
