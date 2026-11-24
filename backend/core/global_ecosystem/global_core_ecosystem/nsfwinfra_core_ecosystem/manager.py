"""Canonical metadata catalog for the NSF Winfra Core Ecosystem."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
ROOT_ID = "NSFW-INFRA-CORE-ECOSYSTEM"
ROOT_NAME = "NSFW INFRA CORE ECOSYSTEM"
ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {"ecosystem_id": "NSFW-INFRA-ACCOUNT-LIMITS-CORE", "package": "nsfwinfra_account_limits_core_ecosystem", "name": "ACCOUNT LIMITS INFRA CORE ECOSYSTEM", "description": "Metadata and policy definitions for account/tenant resource quotas, usage windows, rate and concurrency limits, warning thresholds, reset schedules, plan/entitlement references and enforcement boundaries. Actual metering, billing, authorization and enforcement belong to their dedicated layers.", "capabilities": ["QUOTAS","USAGE_LIMITS","RATE_LIMITS","PLAN_ENTITLEMENT_REFERENCES","RESOURCE_LIMITS","LIMIT_POLICY_METADATA","WARNING_THRESHOLDS","RESET_WINDOWS","ABUSE_PREVENTION_METADATA","READINESS"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-ANIME-GENERATION-CORE", "package": "nsfwinfra_anime_generation_core_ecosystem", "name": "ANIME GENERATION INFRA CORE ECOSYSTEM", "description": "Metadata for anime generation styles, prompt presets, model compatibility, scene and character consistency, pipeline configuration, resource requirements and output contracts. Generation engines and provider connections remain outside Core.", "capabilities": ["ANIME_STYLE_METADATA","MODEL_COMPATIBILITY","PROMPT_CONFIGURATION","CHARACTER_CONSISTENCY_METADATA","SCENE_CONFIGURATION","GENERATION_PRESETS","RESOURCE_REQUIREMENTS","PIPELINE_METADATA","OUTPUT_CONTRACTS","QUALITY_AND_SAFETY_REFERENCES"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-ASYNC-JOBS-CORE", "package": "nsfwinfra_async_jobs_core_ecosystem", "name": "ASYNC JOBS INFRA CORE ECOSYSTEM", "description": "Contracts and policies for asynchronous job types, states, queues, priorities, worker capability metadata, concurrency, retries, timeouts, cancellation, dead-letter handling, idempotency, dependencies, progress and recovery. Execution, workers, queues and persistence are separate runtime responsibilities.", "capabilities": ["JOB_CONTRACTS","LIFECYCLE_STATES","QUEUE_METADATA","PRIORITY_AND_SCHEDULING","WORKER_CAPABILITY_METADATA","CONCURRENCY_LIMITS","RETRY_AND_BACKOFF_POLICY","TIMEOUTS","CANCELLATION_METADATA","DEAD_LETTER_POLICY","IDEMPOTENCY_REFERENCES","PROGRESS_AND_RESULT_CONTRACTS","RECOVERY_METADATA"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-IMAGE-EDITING-CORE", "package": "nsfwinfra_image_editing_core_ecosystem", "name": "IMAGE EDITING INFRA CORE ECOSYSTEM", "description": "Metadata and contracts for image-editing operations, masks, inpainting, outpainting, background operations, transformations, enhancement, restoration, color/lighting, pipeline ordering, compatibility and output requirements. Actual image-processing engines are out of scope.", "capabilities": ["EDIT_OPERATION_METADATA","INPUT_OUTPUT_CONTRACTS","MASK_AND_SELECTION_METADATA","INPAINTING","OUTPAINTING","BACKGROUND_OPERATIONS","TRANSFORMATIONS","ENHANCEMENT_AND_RESTORATION","COLOR_AND_LIGHTING_OPERATIONS","PIPELINE_ORDERING","MODEL_COMPATIBILITY","QUALITY_AND_SAFETY_REFERENCES"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-IMAGE-GENERATION-CORE", "package": "nsfwinfra_image_generation_core_ecosystem", "name": "IMAGE GENERATION INFRA CORE ECOSYSTEM", "description": "Capability and configuration metadata for image generation prompts, seeds, aspect ratios, resolution, quality, styles, batches, resource requirements, model/provider compatibility, output contracts and safety/rights references. Does not assert live model/provider availability.", "capabilities": ["MODEL_AND_PROVIDER_COMPATIBILITY_METADATA","PROMPT_CONTRACTS","NEGATIVE_PROMPT_METADATA","SEED_CONFIGURATION","ASPECT_RATIOS","RESOLUTION_AND_QUALITY_PRESETS","STYLE_METADATA","BATCH_METADATA","RESOURCE_REQUIREMENTS","PIPELINE_METADATA","OUTPUT_FORMAT_CONTRACTS","QUALITY_AND_SAFETY_REFERENCES"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-IMAGE-TO-VIDEO-CORE", "package": "nsfwinfra_image_to_video_core_ecosystem", "name": "IMAGE TO VIDEO INFRA CORE ECOSYSTEM", "description": "Metadata for image-to-video source requirements, animation pipelines, motion and camera configuration, interpolation, duration/frame rate, temporal consistency, compatibility, resources and output contracts. Video execution is external.", "capabilities": ["SOURCE_IMAGE_REQUIREMENTS","ANIMATION_PIPELINE_METADATA","MOTION_CONFIGURATION","CAMERA_MOVEMENT_METADATA","FRAME_INTERPOLATION","FRAME_RATE_AND_DURATION","TEMPORAL_CONSISTENCY_METADATA","RESOLUTION_AND_ASPECT_RATIO","MODEL_COMPATIBILITY","RESOURCE_REQUIREMENTS","OUTPUT_CONTRACTS","QUALITY_AND_SAFETY_REFERENCES"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-IMAGE-VIDEO-EFFECTS-CORE", "package": "nsfwinfra_image_video_effects_core_ecosystem", "name": "IMAGE & VIDEO EFFECTS INFRA CORE ECOSYSTEM", "description": "Catalog and compatibility metadata for filters, transitions, animation/motion/camera effects, compositing, layers, timeline ordering, presets, rendering constraints, output contracts and versions. Effect execution/rendering remains in the engine layer.", "capabilities": ["EFFECTS_CATALOG_METADATA","FILTERS_AND_TRANSITIONS","ANIMATION_AND_MOTION_EFFECTS","CAMERA_EFFECTS","COMPOSITING_AND_LAYER_METADATA","TIMELINE_COMPATIBILITY","ORDERING_AND_PRESETS","ENGINE_COMPATIBILITY","RENDERING_CONSTRAINT_METADATA","OUTPUT_CONTRACTS","QUALITY_AND_VERSION_METADATA"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-SIGNED-UPLOADS-CORE", "package": "nsfwinfra_signed_uploads_core_ecosystem", "name": "SIGNED UPLOADS INFRA CORE ECOSYSTEM", "description": "Policy and contract metadata for authorized signed uploads, signature expiry, file size/type restrictions, MIME/content validation, purpose classification, storage references, multipart/chunking, integrity, retries, abuse prevention and cleanup. Signing secrets, upload transport and storage writes remain external.", "capabilities": ["UPLOAD_CONTRACTS","AUTHORIZATION_REQUIREMENTS","SIGNATURE_METADATA","EXPIRATION_POLICY","SIZE_AND_TYPE_LIMITS","MIME_AND_CONTENT_VALIDATION_POLICY","UPLOAD_PURPOSE_METADATA","STORAGE_DESTINATION_REFERENCES","MULTIPART_AND_CHUNK_METADATA","INTEGRITY_METADATA","RETRY_POLICY","ABUSE_PREVENTION","CLEANUP_AND_RETENTION","READINESS"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-TEXT-TO-VIDEO-CORE", "package": "nsfwinfra_text_to_video_core_ecosystem", "name": "TEXT TO VIDEO INFRA CORE ECOSYSTEM", "description": "Metadata and contracts for text-to-video prompts, scene/storyboard structure, sequencing, scene mapping, motion/camera, temporal and character/environment consistency, transitions, audio compatibility, model compatibility, resources and outputs. Video/audio execution is external.", "capabilities": ["PROMPT_CONTRACTS","SCENE_AND_STORYBOARD_METADATA","SCENE_SEQUENCING","PROMPT_TO_SCENE_MAPPING","DURATION_AND_FRAME_RATE","RESOLUTION_AND_ASPECT_RATIO","CAMERA_AND_MOTION_METADATA","CHARACTER_AND_ENVIRONMENT_CONSISTENCY","TRANSITIONS","AUDIO_COMPATIBILITY_REFERENCES","MODEL_COMPATIBILITY","RESOURCE_REQUIREMENTS","OUTPUT_CONTRACTS","QUALITY_AND_SAFETY_REFERENCES"], "status": "REGISTERED", "enabled": True},
    {"ecosystem_id": "NSFW-INFRA-WEBHOOKS-CORE", "package": "nsfwinfra_webhooks_core_ecosystem", "name": "WEBHOOKS INFRA CORE ECOSYSTEM", "description": "Contracts and policy metadata for webhook subscriptions, events and schemas, endpoints, delivery config, signing/secret references, retries, timeouts, limits, attempts, dead-letter references, idempotency, ordering, endpoint validation, SSRF safeguards and readiness. Delivery and persistence remain external.", "capabilities": ["SUBSCRIPTION_METADATA","EVENT_REGISTRY_AND_SCHEMAS","ENDPOINT_METADATA","DELIVERY_CONFIGURATION","SIGNING_AND_SECRET_REFERENCES","RETRY_AND_BACKOFF_POLICY","TIMEOUTS_AND_RATE_LIMITS","DELIVERY_ATTEMPT_METADATA","FAILED_DELIVERY_AND_DEAD_LETTER_REFERENCES","IDEMPOTENCY","ORDERING_GUARANTEE_METADATA","ENDPOINT_HEALTH_METADATA","SSRF_AND_ENDPOINT_VALIDATION_POLICY","AUDIT_REFERENCES","READINESS"], "status": "REGISTERED", "enabled": True},
)
def list_ecosystems(*, enabled_only: bool = False) -> list[dict[str, Any]]:
    records = [deepcopy(item) for item in ECOSYSTEMS]
    return [item for item in records if item["enabled"]] if enabled_only else records
def get_ecosystem(ecosystem_id: str) -> dict[str, Any] | None:
    key = str(ecosystem_id).strip().casefold()
    for item in ECOSYSTEMS:
        if item["ecosystem_id"].casefold() == key or item["package"].casefold() == key:
            return deepcopy(item)
    return None


class NSFWinfraCoreManager:
    """Stable public manager for NSF Winfra provider metadata."""

    NAME = ROOT_NAME
    ECOSYSTEM_ID = ROOT_ID

    def __init__(self) -> None:
        # Lazy imports avoid cycles: orchestration reads the catalog above.
        from .orchestrator import NSFWinfraCoreOrchestrator
        from .service import NSFWinfraCoreService
        self._orchestrator = NSFWinfraCoreOrchestrator()
        self._service = NSFWinfraCoreService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_ecosystems(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_ecosystems(enabled_only=enabled_only)

    def get_ecosystem(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_ecosystem(ecosystem_id)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def master_catalog_reference(self, *, load_summary: bool = False) -> dict[str, Any]:
        return self._orchestrator.master_catalog_reference(load_summary=load_summary)


def get_manager() -> NSFWinfraCoreManager:
    """Return the canonical NSF Winfra manager."""
    return NSFWinfraCoreManager()


__all__ = [
    "ROOT_ID", "ROOT_NAME", "ECOSYSTEMS",
    "list_ecosystems", "get_ecosystem",
    "NSFWinfraCoreManager", "get_manager",
]
