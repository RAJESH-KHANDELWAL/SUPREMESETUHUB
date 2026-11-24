# IMAGE & VIDEO EFFECTS INFRA CORE ECOSYSTEM

Parent: NSF Winfra Core. Package `nsfwinfra_image_video_effects_core_ecosystem/`. ID: `NSFW-INFRA-IMAGE-VIDEO-EFFECTS-CORE`.

## Scope
Catalog metadata for filters, transitions, animation and motion effects, camera effects, compositing and layer metadata, timeline compatibility, ordering/presets, engine/render constraints, output contracts and quality/version metadata. Execution and rendering remain in dedicated engines.

## Capability metadata
- EFFECTS_CATALOG_METADATA
- FILTERS_AND_TRANSITIONS
- ANIMATION_AND_MOTION_EFFECTS
- CAMERA_EFFECTS
- COMPOSITING_AND_LAYER_METADATA
- TIMELINE_COMPATIBILITY
- ORDERING_AND_PRESETS
- ENGINE_COMPATIBILITY
- RENDERING_CONSTRAINT_METADATA
- OUTPUT_CONTRACTS
- QUALITY_AND_VERSION_METADATA

## Interface
- `manager.py`: metadata status and capability inventory.
- `__init__.py`: public package exports.

Metadata-only: no execution, API calls, persistence or verified-live claim.
