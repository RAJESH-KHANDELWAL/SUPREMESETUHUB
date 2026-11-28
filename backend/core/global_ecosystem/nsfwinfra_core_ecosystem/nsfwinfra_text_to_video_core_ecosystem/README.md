# TEXT TO VIDEO INFRA CORE ECOSYSTEM

Parent: NSF Winfra Core. Package `nsfwinfra_text_to_video_core_ecosystem/`. ID: `NSFW-INFRA-TEXT-TO-VIDEO-CORE`.

## Scope
Metadata/contracts for prompts, storyboard/scenes, sequencing, camera/motion, consistency, transitions, audio compatibility, models, resources and outputs. Generation external.

## Capability metadata
- `PROMPT_CONTRACTS`
- `SCENE_AND_STORYBOARD_METADATA`
- `SCENE_SEQUENCING`
- `PROMPT_TO_SCENE_MAPPING`
- `DURATION_AND_FRAME_RATE`
- `RESOLUTION_AND_ASPECT_RATIO`
- `CAMERA_AND_MOTION_METADATA`
- `CHARACTER_AND_ENVIRONMENT_CONSISTENCY`
- `TRANSITIONS`
- `AUDIO_COMPATIBILITY_REFERENCES`
- `MODEL_COMPATIBILITY`
- `RESOURCE_REQUIREMENTS`
- `OUTPUT_CONTRACTS`
- `QUALITY_AND_SAFETY_REFERENCES`

## Interface
- `manager.py`: status and capability metadata.
- `__init__.py`: public exports.

Metadata-only; no infrastructure execution, API calls, persistence or verified-live claim. Auth, secrets, transport, runtime and storage are separate layers.
