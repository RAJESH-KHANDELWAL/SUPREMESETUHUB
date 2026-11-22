"""NSFWinfra cross-product domain inventory and coverage."""
from __future__ import annotations
from collections import Counter
from typing import Any
from .catalog import get_nsfwinfra_core_catalog
DOMAIN_DEFINITIONS={
  "PROVIDER_GOVERNANCE": [
    "Provider Governance",
    "Provider identity, catalog registration, layer boundaries and readiness."
  ],
  "ACCOUNT_LIMITS_AND_QUOTAS": [
    "Account Limits and Quotas",
    "Rate limits, usage, quotas, account tier and entitlement metadata."
  ],
  "ANIME_AND_STYLE_GENERATION": [
    "Anime and Style Generation",
    "Anime-specific generation capabilities, style catalog and capability boundaries."
  ],
  "IMAGE_GENERATION_AND_EDITING": [
    "Image Generation and Editing",
    "Image generation, editing, input/output formats, task metadata and model capability."
  ],
  "VIDEO_GENERATION_AND_TRANSFORMATION": [
    "Video Generation and Transformation",
    "Text/image to video generation, transformation, duration, formats and task metadata."
  ],
  "MEDIA_TRANSFORMATION_AND_EFFECTS": [
    "Media Transformation and Effects",
    "Image/video effects, transformation options and effect catalog metadata."
  ],
  "ASYNC_JOBS_AND_LIFECYCLE": [
    "Async Jobs and Lifecycle",
    "Task/job registration, state metadata, cancellation boundary and lifecycle discovery."
  ],
  "SIGNED_UPLOADS_AND_ASSET_HANDOFF": [
    "Signed Uploads and Asset Handoff",
    "Signed URL policy metadata, upload capability, asset handoff and expiry metadata."
  ],
  "EVENTS_AND_WEBHOOKS": [
    "Events and Webhooks",
    "Event taxonomy, webhook delivery metadata, signatures, retries and idempotency boundaries."
  ],
  "MEDIA_ASSET_METADATA": [
    "Media Asset Metadata",
    "Asset identifiers, media types, size/duration metadata and ownership boundaries."
  ],
  "MODEL_CATALOG_AND_CAPABILITIES": [
    "Model Catalog and Capabilities",
    "Model inventory, versions, features and capability discovery."
  ],
  "CONTENT_SAFETY_AND_AGE_GATING": [
    "Content Safety and Age Gating",
    "Policy classification, age restrictions, safety and consent boundaries, moderation readiness."
  ],
  "SECURITY_PRIVACY_AND_ACCESS": [
    "Security, Privacy and Access",
    "Tenant isolation, actor identity, secret references, signed access and privacy boundaries."
  ],
  "STORAGE_BOUNDARIES_AND_RETENTION": [
    "Storage Boundaries and Retention",
    "Shared storage ownership, artifact lifecycle and retention metadata."
  ],
  "READINESS_AND_DEPENDENCIES": [
    "Readiness and Dependencies",
    "Required configuration, dependency discovery, readiness checks and health metadata."
  ],
  "CAPABILITY_DISCOVERY": [
    "Capability Discovery",
    "Registered capabilities, product support and capability-to-module mapping."
  ],
  "ERROR_AND_RETRY_METADATA": [
    "Error and Retry Metadata",
    "Provider error taxonomy, retryability and safe failure metadata."
  ],
  "INTEROPERABILITY_AND_INTEGRATION": [
    "Interoperability and Integration",
    "API layer references, AI provider facade references and integration contracts."
  ],
  "USAGE_AND_BILLING_METADATA": [
    "Usage and Billing Metadata",
    "Usage/billing signals and account limit metadata without billing execution."
  ],
  "TENANT_POLICY_AND_AUTHORIZATION": [
    "Tenant Policy and Authorization",
    "Caller context, tenant policy, authorization boundaries and capability classification."
  ],
  "OPERATIONS_AND_OBSERVABILITY": [
    "Operations and Observability",
    "Health/status, diagnostic metadata, metrics boundaries and operational readiness."
  ]
}
def get_domain_catalog()->dict[str,dict[str,Any]]:
 catalog=get_nsfwinfra_core_catalog()
 coverage={domain:[] for domain in DOMAIN_DEFINITIONS}
 for product in catalog["children"]:
  for domain in product["domains"]:
   if domain in coverage: coverage[domain].append(product["ecosystem_id"])
 return {key:{"domain_id":key,"name":definition[0],"purpose":definition[1],"product_ecosystem_ids":sorted(set(coverage[key])),"product_count":len(set(coverage[key]))} for key,definition in DOMAIN_DEFINITIONS.items()}
