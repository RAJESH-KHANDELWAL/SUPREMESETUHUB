"""Canonical NSFWinfra Core provider catalog; inventory and metadata only."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
ROOT_ID="NSFWINFRA-CORE-ECOSYSTEM"
ROOT_PATH="backend/core/global_ecosystem/global_core_ecosystem/nsfwinfra_core_ecosystem"
API_ROOT="backend/api/global_ecosystem/global_api_ecosystem/nsfwinfra_api_ecosystem"
AI_API_REF="backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/nsfwinfra_ai_api_ecosystem"
AI_CORE_REF="backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/nsfwinfra_ai_core_ecosystem"
AI_PROVIDER_REF=None
_PRODUCTS=[
  {
    "key": "account_limits",
    "ecosystem_id": "NSFW-ACCOUNT-LIMITS-CORE-ECOSYSTEM",
    "name": "Account Limits",
    "directory": "nsfwinfra_account_limits_core_ecosystem",
    "api_directory": "nsfwinfra_account_limits_api_ecosystem",
    "domains": [
      "ACCOUNT_LIMITS_AND_QUOTAS",
      "PROVIDER_GOVERNANCE"
    ],
    "capabilities": [
      "ACCOUNT_LIMIT_DISCOVERY",
      "QUOTA_POLICY_METADATA",
      "LIMIT_READINESS"
    ]
  },
  {
    "key": "anime_generation",
    "ecosystem_id": "NSFW-ANIME-GENERATION-CORE-ECOSYSTEM",
    "name": "Anime Generation",
    "directory": "nsfwinfra_anime_generation_core_ecosystem",
    "api_directory": "nsfwinfra_anime_generation_api_ecosystem",
    "domains": [
      "ANIME_AND_STYLE_GENERATION",
      "IMAGE_GENERATION_AND_EDITING",
      "CONTENT_SAFETY_AND_AGE_GATING"
    ],
    "capabilities": [
      "ANIME_GENERATION_CAPABILITY_DISCOVERY",
      "STYLE_METADATA",
      "CONTENT_POLICY_METADATA"
    ]
  },
  {
    "key": "async_jobs",
    "ecosystem_id": "NSFW-ASYNC-JOBS-CORE-ECOSYSTEM",
    "name": "Async Jobs",
    "directory": "nsfwinfra_async_jobs_core_ecosystem",
    "api_directory": "nsfwinfra_async_jobs_api_ecosystem",
    "domains": [
      "ASYNC_JOBS_AND_LIFECYCLE",
      "ACCOUNT_LIMITS_AND_QUOTAS",
      "EVENTS_AND_WEBHOOKS"
    ],
    "capabilities": [
      "JOB_METADATA",
      "JOB_LIFECYCLE_DISCOVERY",
      "ASYNC_READINESS"
    ]
  },
  {
    "key": "image_editing",
    "ecosystem_id": "NSFW-IMAGE-EDITING-CORE-ECOSYSTEM",
    "name": "Image Editing",
    "directory": "nsfwinfra_image_editing_core_ecosystem",
    "api_directory": "nsfwinfra_image_editing_api_ecosystem",
    "domains": [
      "IMAGE_GENERATION_AND_EDITING",
      "MEDIA_ASSET_METADATA",
      "CONTENT_SAFETY_AND_AGE_GATING"
    ],
    "capabilities": [
      "IMAGE_EDITING_CAPABILITY_DISCOVERY",
      "EDIT_TASK_METADATA",
      "SAFETY_POLICY_METADATA"
    ]
  },
  {
    "key": "image_generation",
    "ecosystem_id": "NSFW-IMAGE-GENERATION-CORE-ECOSYSTEM",
    "name": "Image Generation",
    "directory": "nsfwinfra_image_generation_core_ecosystem",
    "api_directory": "nsfwinfra_image_generation_api_ecosystem",
    "domains": [
      "IMAGE_GENERATION_AND_EDITING",
      "ANIME_AND_STYLE_GENERATION",
      "CONTENT_SAFETY_AND_AGE_GATING"
    ],
    "capabilities": [
      "IMAGE_GENERATION_CAPABILITY_DISCOVERY",
      "MODEL_AND_STYLE_METADATA",
      "SAFETY_POLICY_METADATA"
    ]
  },
  {
    "key": "image_to_video",
    "ecosystem_id": "NSFW-IMAGE-TO-VIDEO-CORE-ECOSYSTEM",
    "name": "Image to Video",
    "directory": "nsfwinfra_image_to_video_core_ecosystem",
    "api_directory": "nsfwinfra_image_to_video_api_ecosystem",
    "domains": [
      "VIDEO_GENERATION_AND_TRANSFORMATION",
      "MEDIA_ASSET_METADATA",
      "CONTENT_SAFETY_AND_AGE_GATING"
    ],
    "capabilities": [
      "IMAGE_TO_VIDEO_CAPABILITY_DISCOVERY",
      "VIDEO_TASK_METADATA",
      "SAFETY_POLICY_METADATA"
    ]
  },
  {
    "key": "image_video_effects",
    "ecosystem_id": "NSFW-IMAGE-VIDEO-EFFECTS-CORE-ECOSYSTEM",
    "name": "Image/Video Effects",
    "directory": "nsfwinfra_image_video_effects_core_ecosystem",
    "api_directory": "nsfwinfra_image_video_effects_api_ecosystem",
    "domains": [
      "MEDIA_TRANSFORMATION_AND_EFFECTS",
      "MEDIA_ASSET_METADATA",
      "CONTENT_SAFETY_AND_AGE_GATING"
    ],
    "capabilities": [
      "EFFECTS_CATALOG_METADATA",
      "TRANSFORMATION_TASK_METADATA",
      "SAFETY_POLICY_METADATA"
    ]
  },
  {
    "key": "signed_uploads",
    "ecosystem_id": "NSFW-SIGNED-UPLOADS-CORE-ECOSYSTEM",
    "name": "Signed Uploads",
    "directory": "nsfwinfra_signed_uploads_core_ecosystem",
    "api_directory": "nsfwinfra_signed_uploads_api_ecosystem",
    "domains": [
      "SIGNED_UPLOADS_AND_ASSET_HANDOFF",
      "STORAGE_BOUNDARIES_AND_RETENTION",
      "SECURITY_PRIVACY_AND_ACCESS"
    ],
    "capabilities": [
      "SIGNED_UPLOAD_POLICY_METADATA",
      "UPLOAD_READINESS_DISCOVERY",
      "ASSET_HANDOFF_METADATA"
    ]
  },
  {
    "key": "text_to_video",
    "ecosystem_id": "NSFW-TEXT-TO-VIDEO-CORE-ECOSYSTEM",
    "name": "Text to Video",
    "directory": "nsfwinfra_text_to_video_core_ecosystem",
    "api_directory": "nsfwinfra_text_to_video_api_ecosystem",
    "domains": [
      "VIDEO_GENERATION_AND_TRANSFORMATION",
      "CONTENT_SAFETY_AND_AGE_GATING",
      "ACCOUNT_LIMITS_AND_QUOTAS"
    ],
    "capabilities": [
      "TEXT_TO_VIDEO_CAPABILITY_DISCOVERY",
      "VIDEO_MODEL_METADATA",
      "SAFETY_POLICY_METADATA"
    ]
  },
  {
    "key": "webhooks",
    "ecosystem_id": "NSFW-WEBHOOKS-CORE-ECOSYSTEM",
    "name": "Webhooks",
    "directory": "nsfwinfra_webhooks_core_ecosystem",
    "api_directory": "nsfwinfra_webhooks_api_ecosystem",
    "domains": [
      "EVENTS_AND_WEBHOOKS",
      "ASYNC_JOBS_AND_LIFECYCLE",
      "SECURITY_PRIVACY_AND_ACCESS"
    ],
    "capabilities": [
      "WEBHOOK_EVENT_METADATA",
      "DELIVERY_POLICY_METADATA",
      "WEBHOOK_READINESS_DISCOVERY"
    ]
  }
]
_COMMON=["PROVIDER_GOVERNANCE","SECURITY_PRIVACY_AND_ACCESS","TENANT_POLICY_AND_AUTHORIZATION","READINESS_AND_DEPENDENCIES","CAPABILITY_DISCOVERY","MODEL_CATALOG_AND_CAPABILITIES","STORAGE_BOUNDARIES_AND_RETENTION","ERROR_AND_RETRY_METADATA","INTEROPERABILITY_AND_INTEGRATION","USAGE_AND_BILLING_METADATA","OPERATIONS_AND_OBSERVABILITY"]
def get_nsfwinfra_core_catalog()->dict[str,Any]:
 children=[]
 for item in _PRODUCTS:
  row=deepcopy(item)
  row["domains"]=list(dict.fromkeys([*_COMMON,*item["domains"]]))
  row.update({"ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":ROOT_ID,"core_module":f"{ROOT_PATH}/{item['directory']}","api_catalog_ref":f"{API_ROOT}/{item['api_directory']}","status":"CORE_CATALOG_ONLY","enabled":True,"connected":False,"live_connection_verified":False})
  children.append(row)
 return {"ecosystem_id":ROOT_ID,"name":"NSFW INFRA CORE ECOSYSTEM","provider":"nsfwinfra","ecosystem_type":"PROVIDER_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","status":"CORE_CATALOG_ONLY","enabled":True,"core_path":ROOT_PATH,"api_catalog_ref":API_ROOT,"ai_api_ref":AI_API_REF,"ai_core_ref":AI_CORE_REF,"ai_provider_ref":AI_PROVIDER_REF,"capabilities":["NSFWINFRA_PROVIDER_REGISTRY","IMAGE_AND_VIDEO_GENERATION_CAPABILITY_DISCOVERY","ANIME_AND_STYLE_METADATA","ASYNC_JOB_AND_WEBHOOK_METADATA","SIGNED_UPLOAD_POLICY_METADATA","TENANT_SCOPED_POLICY","AGE_AND_CONTENT_SAFETY_BOUNDARIES","READ_ONLY_MASTER_CATALOG_MAPPING"],"children":children}
__all__=["ROOT_ID","ROOT_PATH","API_ROOT","AI_API_REF","AI_CORE_REF","AI_PROVIDER_REF","get_nsfwinfra_core_catalog"]
