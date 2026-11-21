"""Hugging Face provider-neutral capability domains."""
from __future__ import annotations
DOMAIN_DEFINITIONS = (
("PROVIDER_GOVERNANCE","Provider Governance","Provider identity, lifecycle, catalog and capability ownership."),
("HUB_REPOSITORY_GOVERNANCE","Hub and Repository Governance","Repository identity, visibility, revisions, access and metadata."),
("MODEL_DISCOVERY","Model Discovery and Metadata","Model cards, tasks, libraries, tags, licences and revisions."),
("DATASET_DISCOVERY","Dataset Discovery and Metadata","Dataset cards, splits, formats, licences and revisions."),
("SPACES_APPLICATIONS","Spaces and Applications","Space metadata, runtime profile and application lifecycle."),
("INFERENCE_CAPABILITIES","Inference Capabilities","Task compatibility, provider routing and model capability metadata."),
("INFERENCE_ENDPOINTS","Inference Endpoints","Endpoint configuration, deployment readiness and scaling metadata."),
("TASKS_PIPELINES","Tasks and Pipelines","Task taxonomy and pipeline input/output contracts."),
("AUTHENTICATION_ACCESS","Authentication and Access","Token references, authorization scopes and access boundaries."),
("ORGANIZATIONS_TEAMS","Organizations and Teams","Organization, team, membership and role metadata."),
("DISCUSSIONS_COMMUNITY","Discussions and Community","Repository discussions and community metadata."),
("WEBHOOKS_EVENTS","Webhooks and Events","Event schemas, webhook registration and delivery policy metadata."),
("EVALUATION_BENCHMARKS","Evaluation and Benchmarks","Evaluation jobs, benchmark metadata and result lineage."),
("BILLING_PRICING","Billing and Pricing","Plans, pricing, usage and billing references; no payment execution."),
("DOWNLOADS_CACHE","Downloads and Cache","Download artifacts, cache references and lifecycle metadata."),
("STORAGE_ARTIFACTS","Storage and Artifacts","Storage quotas, artifact references, retention and lifecycle metadata."),
("SECURITY_PRIVACY_COMPLIANCE","Security, Privacy and Compliance","Secrets boundary, licence, privacy, safety and audit metadata."),
("TENANCY_QUOTAS_USAGE","Tenancy, Quotas and Usage","Tenant isolation, rate/quota metadata and usage boundaries."),
("MODEL_DATA_LINEAGE","Model and Dataset Lineage","Revision provenance, source references and reproducibility metadata."),
("INTEGRATION_DEPENDENCIES","Integration Dependencies","API/ENGINE/runtime dependency references without duplicating their implementations."),
)
def list_domains() -> list[dict]:
    return [{"domain_id": key, "name": name, "description": description, "layer": "CORE", "implementation_mode": "SHARED_METADATA_TAXONOMY"} for key,name,description in DOMAIN_DEFINITIONS]
def get_domain(domain_id: str) -> dict | None:
    key = str(domain_id).strip().upper()
    return next((item for item in list_domains() if item["domain_id"] == key), None)
def domain_summary() -> dict:
    items = list_domains()
    return {"domain_count": len(items), "domain_ids": [item["domain_id"] for item in items]}
