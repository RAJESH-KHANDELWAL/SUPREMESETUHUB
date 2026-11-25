# IMAGE TO VIDEO INFRA CORE ECOSYSTEM

Parent: NSF Winfra Core. Package `nsfwinfra_image_to_video_core_ecosystem/`. ID: `NSFW-INFRA-IMAGE-TO-VIDEO-CORE`.

## Scope
Metadata for source images, animation, motion/camera, interpolation, duration/frame rate, consistency, compatibility, resources and outputs. Execution external.

## Capabilities
- `SOURCE_IMAGE_REQUIREMENTS`
- `ANIMATION_PIPELINE_METADATA`
- `MOTION_CONFIGURATION`
- `CAMERA_MOVEMENT_METADATA`
- `FRAME_INTERPOLATION`
- `FRAME_RATE_AND_DURATION`
- `TEMPORAL_CONSISTENCY_METADATA`
- `RESOLUTION_AND_ASPECT_RATIO`
- `MODEL_COMPATIBILITY`
- `RESOURCE_REQUIREMENTS`
- `OUTPUT_CONTRACTS`
- `QUALITY_AND_SAFETY_REFERENCES`

## Files
- `manager.py`: status and capability metadata interface.
- `__init__.py`: public package exports.

Metadata-only: no execution, API calls, persistence, or live-connectivity claim. Authentication, secrets, transport, runtime and storage remain in their designated layers.
