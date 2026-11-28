# IMAGE EDITING INFRA CORE ECOSYSTEM

Parent: NSF Winfra Core. Package `nsfwinfra_image_editing_core_ecosystem/`. ID: `NSFW-INFRA-IMAGE-EDITING-CORE`.

## Scope
Contracts and metadata for editing, masks, in/outpainting, background operations, transforms, enhancement/restoration, color/light, ordering, model compatibility and quality. Processing engine external.

## Capabilities
- `EDIT_OPERATION_METADATA`
- `INPUT_OUTPUT_CONTRACTS`
- `MASK_AND_SELECTION_METADATA`
- `INPAINTING`
- `OUTPAINTING`
- `BACKGROUND_OPERATIONS`
- `TRANSFORMATIONS`
- `ENHANCEMENT_AND_RESTORATION`
- `COLOR_AND_LIGHTING_OPERATIONS`
- `PIPELINE_ORDERING`
- `MODEL_COMPATIBILITY`
- `QUALITY_AND_SAFETY_REFERENCES`

## Files
- `manager.py`: status and capability metadata interface.
- `__init__.py`: public package exports.

Metadata-only: no execution, API calls, persistence, or live-connectivity claim. Authentication, secrets, transport, runtime and storage remain in their designated layers.
