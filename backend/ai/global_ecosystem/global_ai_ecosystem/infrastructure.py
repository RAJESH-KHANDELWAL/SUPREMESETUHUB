"""AI infrastructure taxonomy; no cloud resources are provisioned by this module."""
from .schemas import CatalogRecord

INFRASTRUCTURE = tuple(
    CatalogRecord(key, name, "ai_infrastructure", description)
    for key, name, description in (
        ("accelerators", "Compute accelerators", "GPU and other AI accelerator resources."),
        ("model_serving", "Model serving", "Serve models behind managed inference endpoints."),
        ("containers", "Container runtime", "Package and isolate AI workloads."),
        ("batch_jobs", "Batch processing", "Run queued or scheduled inference workloads."),
        ("object_storage", "Object storage", "Store datasets, artifacts and generated media."),
        ("observability", "Observability", "Collect latency, errors, usage and quality telemetry."),
        ("secrets", "Secret management", "Resolve credentials from an approved secret store."),
        ("queues", "Job queues", "Coordinate asynchronous AI tasks."),
    )
)
