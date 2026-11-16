"""Read-only hosting provider inventory derived from the supplied folder snapshot."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

HOSTING_PROVIDER_CATALOG: tuple[dict[str, Any], ...] = tuple([
  {
    "provider_id": "abelohost",
    "package_name": "abelohost_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-ABELOHOST-CORE-ECOSYSTEM",
    "name": "ABELOHOST",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "acquia",
    "package_name": "acquia_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-ACQUIA-CORE-ECOSYSTEM",
    "name": "ACQUIA",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "akamai",
    "package_name": "akamai_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-AKAMAI-CORE-ECOSYSTEM",
    "name": "AKAMAI",
    "category": "EDGE_CDN_AND_OBJECT_STORAGE",
    "capabilities": [
      "EDGE_DISTRIBUTION_METADATA",
      "CACHE_CONFIGURATION_METADATA",
      "OBJECT_STORAGE_REFERENCE",
      "ORIGIN_CONFIGURATION_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "alexhost",
    "package_name": "alexhost_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-ALEXHOST-CORE-ECOSYSTEM",
    "name": "ALEXHOST",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "alibaba_cloud",
    "package_name": "alibaba_cloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-ALIBABA_CLOUD-CORE-ECOSYSTEM",
    "name": "ALIBABA CLOUD",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "appwrite",
    "package_name": "appwrite_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-APPWRITE-CORE-ECOSYSTEM",
    "name": "APPWRITE",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "awardspace",
    "package_name": "awardspace_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-AWARDSPACE-CORE-ECOSYSTEM",
    "name": "AWARDSPACE",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "aws",
    "package_name": "aws_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-AWS-CORE-ECOSYSTEM",
    "name": "AWS",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "backblaze",
    "package_name": "backblaze_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-BACKBLAZE-CORE-ECOSYSTEM",
    "name": "BACKBLAZE",
    "category": "EDGE_CDN_AND_OBJECT_STORAGE",
    "capabilities": [
      "EDGE_DISTRIBUTION_METADATA",
      "CACHE_CONFIGURATION_METADATA",
      "OBJECT_STORAGE_REFERENCE",
      "ORIGIN_CONFIGURATION_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "bigrock",
    "package_name": "bigrock_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-BIGROCK-CORE-ECOSYSTEM",
    "name": "BIGROCK",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "blueangelhost",
    "package_name": "blueangelhost_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-BLUEANGELHOST-CORE-ECOSYSTEM",
    "name": "BLUEANGELHOST",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "bluehost",
    "package_name": "bluehost_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-BLUEHOST-CORE-ECOSYSTEM",
    "name": "BLUEHOST",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "bunny",
    "package_name": "bunny_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-BUNNY-CORE-ECOSYSTEM",
    "name": "BUNNY",
    "category": "EDGE_CDN_AND_OBJECT_STORAGE",
    "capabilities": [
      "EDGE_DISTRIBUTION_METADATA",
      "CACHE_CONFIGURATION_METADATA",
      "OBJECT_STORAGE_REFERENCE",
      "ORIGIN_CONFIGURATION_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "buyvm",
    "package_name": "buyvm_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-BUYVM-CORE-ECOSYSTEM",
    "name": "BUYVM",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "chemicloud",
    "package_name": "chemicloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-CHEMICLOUD-CORE-ECOSYSTEM",
    "name": "CHEMICLOUD",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "cloudflare",
    "package_name": "cloudflare_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-CLOUDFLARE-CORE-ECOSYSTEM",
    "name": "CLOUDFLARE",
    "category": "EDGE_CDN_AND_OBJECT_STORAGE",
    "capabilities": [
      "EDGE_DISTRIBUTION_METADATA",
      "CACHE_CONFIGURATION_METADATA",
      "OBJECT_STORAGE_REFERENCE",
      "ORIGIN_CONFIGURATION_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "cloudways",
    "package_name": "cloudways_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-CLOUDWAYS-CORE-ECOSYSTEM",
    "name": "CLOUDWAYS",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "combell",
    "package_name": "combell_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-COMBELL-CORE-ECOSYSTEM",
    "name": "COMBELL",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "contabo",
    "package_name": "contabo_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-CONTABO-CORE-ECOSYSTEM",
    "name": "CONTABO",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "cpanel",
    "package_name": "cpanel_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-CPANEL-CORE-ECOSYSTEM",
    "name": "CPANEL",
    "category": "HOSTING_CONTROL_AND_MANAGEMENT",
    "capabilities": [
      "HOSTING_ACCOUNT_METADATA",
      "CONTROL_PLANE_CONFIGURATION_METADATA",
      "SERVER_AND_SITE_MANAGEMENT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "crazydomains",
    "package_name": "crazydomains_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-CRAZYDOMAINS-CORE-ECOSYSTEM",
    "name": "CRAZYDOMAINS",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "ctrls",
    "package_name": "ctrls_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-CTRLS-CORE-ECOSYSTEM",
    "name": "CTRLS",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "digitalocean",
    "package_name": "digitalocean_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-DIGITALOCEAN-CORE-ECOSYSTEM",
    "name": "DIGITALOCEAN",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "dreamhost",
    "package_name": "dreamhost_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-DREAMHOST-CORE-ECOSYSTEM",
    "name": "DREAMHOST",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "e2enetworks",
    "package_name": "e2enetworks_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-E2ENETWORKS-CORE-ECOSYSTEM",
    "name": "E2ENETWORKS",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "equinix",
    "package_name": "equinix_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-EQUINIX-CORE-ECOSYSTEM",
    "name": "EQUINIX",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "fastcomet",
    "package_name": "fastcomet_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-FASTCOMET-CORE-ECOSYSTEM",
    "name": "FASTCOMET",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "fastly",
    "package_name": "fastly_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-FASTLY-CORE-ECOSYSTEM",
    "name": "FASTLY",
    "category": "EDGE_CDN_AND_OBJECT_STORAGE",
    "capabilities": [
      "EDGE_DISTRIBUTION_METADATA",
      "CACHE_CONFIGURATION_METADATA",
      "OBJECT_STORAGE_REFERENCE",
      "ORIGIN_CONFIGURATION_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "firebase",
    "package_name": "firebase_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-FIREBASE-CORE-ECOSYSTEM",
    "name": "FIREBASE",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "flokinet",
    "package_name": "flokinet_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-FLOKINET-CORE-ECOSYSTEM",
    "name": "FLOKINET",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "flyio",
    "package_name": "flyio_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-FLYIO-CORE-ECOSYSTEM",
    "name": "FLYIO",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "gandi",
    "package_name": "gandi_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-GANDI-CORE-ECOSYSTEM",
    "name": "GANDI",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "gcore",
    "package_name": "gcore_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-GCORE-CORE-ECOSYSTEM",
    "name": "GCORE",
    "category": "EDGE_CDN_AND_OBJECT_STORAGE",
    "capabilities": [
      "EDGE_DISTRIBUTION_METADATA",
      "CACHE_CONFIGURATION_METADATA",
      "OBJECT_STORAGE_REFERENCE",
      "ORIGIN_CONFIGURATION_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "github_pages",
    "package_name": "github_pages_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-GITHUB_PAGES-CORE-ECOSYSTEM",
    "name": "GITHUB PAGES",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "gitlab_pages",
    "package_name": "gitlab_pages_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-GITLAB_PAGES-CORE-ECOSYSTEM",
    "name": "GITLAB PAGES",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "godaddy",
    "package_name": "godaddy_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-GODADDY-CORE-ECOSYSTEM",
    "name": "GODADDY",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "google_cloud",
    "package_name": "google_cloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-GOOGLE_CLOUD-CORE-ECOSYSTEM",
    "name": "GOOGLE CLOUD",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "greencloudvps",
    "package_name": "greencloudvps_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-GREENCLOUDVPS-CORE-ECOSYSTEM",
    "name": "GREENCLOUDVPS",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "greengeeks",
    "package_name": "greengeeks_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-GREENGEEKS-CORE-ECOSYSTEM",
    "name": "GREENGEEKS",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "heroku",
    "package_name": "heroku_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HEROKU-CORE-ECOSYSTEM",
    "name": "HEROKU",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hetzner",
    "package_name": "hetzner_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HETZNER-CORE-ECOSYSTEM",
    "name": "HETZNER",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hivelocity",
    "package_name": "hivelocity_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HIVELOCITY-CORE-ECOSYSTEM",
    "name": "HIVELOCITY",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostarmada",
    "package_name": "hostarmada_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTARMADA-CORE-ECOSYSTEM",
    "name": "HOSTARMADA",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostgator",
    "package_name": "hostgator_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTGATOR-CORE-ECOSYSTEM",
    "name": "HOSTGATOR",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostgatorindia",
    "package_name": "hostgatorindia_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTGATORINDIA-CORE-ECOSYSTEM",
    "name": "HOSTGATORINDIA",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hosting_com",
    "package_name": "hosting_com_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTING_COM-CORE-ECOSYSTEM",
    "name": "HOSTING COM",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostinger",
    "package_name": "hostinger_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTINGER-CORE-ECOSYSTEM",
    "name": "HOSTINGER",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostingraja",
    "package_name": "hostingraja_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTINGRAJA-CORE-ECOSYSTEM",
    "name": "HOSTINGRAJA",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostitsmart",
    "package_name": "hostitsmart_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTITSMART-CORE-ECOSYSTEM",
    "name": "HOSTITSMART",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostkey",
    "package_name": "hostkey_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTKEY-CORE-ECOSYSTEM",
    "name": "HOSTKEY",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostpapa",
    "package_name": "hostpapa_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTPAPA-CORE-ECOSYSTEM",
    "name": "HOSTPAPA",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostsailor",
    "package_name": "hostsailor_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTSAILOR-CORE-ECOSYSTEM",
    "name": "HOSTSAILOR",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "hostwinds",
    "package_name": "hostwinds_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HOSTWINDS-CORE-ECOSYSTEM",
    "name": "HOSTWINDS",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "huawei_cloud",
    "package_name": "huawei_cloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-HUAWEI_CLOUD-CORE-ECOSYSTEM",
    "name": "HUAWEI CLOUD",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "ibm_cloud",
    "package_name": "ibm_cloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-IBM_CLOUD-CORE-ECOSYSTEM",
    "name": "IBM CLOUD",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "infinityfree",
    "package_name": "infinityfree_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-INFINITYFREE-CORE-ECOSYSTEM",
    "name": "INFINITYFREE",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "infomaniak",
    "package_name": "infomaniak_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-INFOMANIAK-CORE-ECOSYSTEM",
    "name": "INFOMANIAK",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "inmotion",
    "package_name": "inmotion_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-INMOTION-CORE-ECOSYSTEM",
    "name": "INMOTION",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "interserver",
    "package_name": "interserver_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-INTERSERVER-CORE-ECOSYSTEM",
    "name": "INTERSERVER",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "ionos",
    "package_name": "ionos_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-IONOS-CORE-ECOSYSTEM",
    "name": "IONOS",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "kinsta",
    "package_name": "kinsta_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-KINSTA-CORE-ECOSYSTEM",
    "name": "KINSTA",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "knownhost",
    "package_name": "knownhost_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-KNOWNHOST-CORE-ECOSYSTEM",
    "name": "KNOWNHOST",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "koyeb",
    "package_name": "koyeb_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-KOYEB-CORE-ECOSYSTEM",
    "name": "KOYEB",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "leaseweb",
    "package_name": "leaseweb_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-LEASEWEB-CORE-ECOSYSTEM",
    "name": "LEASEWEB",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "linode",
    "package_name": "linode_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-LINODE-CORE-ECOSYSTEM",
    "name": "LINODE",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "liquidweb",
    "package_name": "liquidweb_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-LIQUIDWEB-CORE-ECOSYSTEM",
    "name": "LIQUIDWEB",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "m247",
    "package_name": "m247_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-M247-CORE-ECOSYSTEM",
    "name": "M247",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "microsoft",
    "package_name": "microsoft_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-MICROSOFT-CORE-ECOSYSTEM",
    "name": "MICROSOFT",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "milesweb",
    "package_name": "milesweb_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-MILESWEB-CORE-ECOSYSTEM",
    "name": "MILESWEB",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "namecheap",
    "package_name": "namecheap_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-NAMECHEAP-CORE-ECOSYSTEM",
    "name": "NAMECHEAP",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "neocities",
    "package_name": "neocities_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-NEOCITIES-CORE-ECOSYSTEM",
    "name": "NEOCITIES",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "netlify",
    "package_name": "netlify_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-NETLIFY-CORE-ECOSYSTEM",
    "name": "NETLIFY",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "netmagic",
    "package_name": "netmagic_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-NETMAGIC-CORE-ECOSYSTEM",
    "name": "NETMAGIC",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "northflank",
    "package_name": "northflank_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-NORTHFLANK-CORE-ECOSYSTEM",
    "name": "NORTHFLANK",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "one_com",
    "package_name": "one_com_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-ONE_COM-CORE-ECOSYSTEM",
    "name": "ONE COM",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "oracle_cloud",
    "package_name": "oracle_cloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-ORACLE_CLOUD-CORE-ECOSYSTEM",
    "name": "ORACLE CLOUD",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "ovhcloud",
    "package_name": "ovhcloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-OVHCLOUD-CORE-ECOSYSTEM",
    "name": "OVHCLOUD",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "pagely",
    "package_name": "pagely_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-PAGELY-CORE-ECOSYSTEM",
    "name": "PAGELY",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "pantheon",
    "package_name": "pantheon_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-PANTHEON-CORE-ECOSYSTEM",
    "name": "PANTHEON",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "phoenixnap",
    "package_name": "phoenixnap_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-PHOENIXNAP-CORE-ECOSYSTEM",
    "name": "PHOENIXNAP",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "platform_sh",
    "package_name": "platform_sh_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-PLATFORM_SH-CORE-ECOSYSTEM",
    "name": "PLATFORM SH",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "plesk",
    "package_name": "plesk_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-PLESK-CORE-ECOSYSTEM",
    "name": "PLESK",
    "category": "HOSTING_CONTROL_AND_MANAGEMENT",
    "capabilities": [
      "HOSTING_ACCOUNT_METADATA",
      "CONTROL_PLANE_CONFIGURATION_METADATA",
      "SERVER_AND_SITE_MANAGEMENT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "pressable",
    "package_name": "pressable_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-PRESSABLE-CORE-ECOSYSTEM",
    "name": "PRESSABLE",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "rackspace",
    "package_name": "rackspace_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-RACKSPACE-CORE-ECOSYSTEM",
    "name": "RACKSPACE",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "railway",
    "package_name": "railway_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-RAILWAY-CORE-ECOSYSTEM",
    "name": "RAILWAY",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "ramnode",
    "package_name": "ramnode_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-RAMNODE-CORE-ECOSYSTEM",
    "name": "RAMNODE",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "render",
    "package_name": "render_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-RENDER-CORE-ECOSYSTEM",
    "name": "RENDER",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "replit",
    "package_name": "replit_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-REPLIT-CORE-ECOSYSTEM",
    "name": "REPLIT",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "resellerclub",
    "package_name": "resellerclub_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-RESELLERCLUB-CORE-ECOSYSTEM",
    "name": "RESELLERCLUB",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "runcloud",
    "package_name": "runcloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-RUNCLOUD-CORE-ECOSYSTEM",
    "name": "RUNCLOUD",
    "category": "HOSTING_CONTROL_AND_MANAGEMENT",
    "capabilities": [
      "HOSTING_ACCOUNT_METADATA",
      "CONTROL_PLANE_CONFIGURATION_METADATA",
      "SERVER_AND_SITE_MANAGEMENT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "scaleway",
    "package_name": "scaleway_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-SCALEWAY-CORE-ECOSYSTEM",
    "name": "SCALEWAY",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "serverion",
    "package_name": "serverion_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-SERVERION-CORE-ECOSYSTEM",
    "name": "SERVERION",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "shinjiru",
    "package_name": "shinjiru_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-SHINJIRU-CORE-ECOSYSTEM",
    "name": "SHINJIRU",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "siteground",
    "package_name": "siteground_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-SITEGROUND-CORE-ECOSYSTEM",
    "name": "SITEGROUND",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "strato",
    "package_name": "strato_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-STRATO-CORE-ECOSYSTEM",
    "name": "STRATO",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "supabase",
    "package_name": "supabase_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-SUPABASE-CORE-ECOSYSTEM",
    "name": "SUPABASE",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "surge",
    "package_name": "surge_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-SURGE-CORE-ECOSYSTEM",
    "name": "SURGE",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "tencent_cloud",
    "package_name": "tencent_cloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-TENCENT_CLOUD-CORE-ECOSYSTEM",
    "name": "TENCENT CLOUD",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "transip",
    "package_name": "transip_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-TRANSIP-CORE-ECOSYSTEM",
    "name": "TRANSIP",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "upcloud",
    "package_name": "upcloud_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-UPCLOUD-CORE-ECOSYSTEM",
    "name": "UPCLOUD",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "ventraip",
    "package_name": "ventraip_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-VENTRAIP-CORE-ECOSYSTEM",
    "name": "VENTRAIP",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "vercel",
    "package_name": "vercel_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-VERCEL-CORE-ECOSYSTEM",
    "name": "VERCEL",
    "category": "PLATFORM_AS_A_SERVICE",
    "capabilities": [
      "APPLICATION_DEPLOYMENT_METADATA",
      "BUILD_AND_RUNTIME_CONFIGURATION_METADATA",
      "DOMAIN_AND_ENVIRONMENT_REFERENCE",
      "DEPLOYMENT_STATUS_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "verpex",
    "package_name": "verpex_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-VERPEX-CORE-ECOSYSTEM",
    "name": "VERPEX",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "vicetemple",
    "package_name": "vicetemple_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-VICETEMPLE-CORE-ECOSYSTEM",
    "name": "VICETEMPLE",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "vultr",
    "package_name": "vultr_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-VULTR-CORE-ECOSYSTEM",
    "name": "VULTR",
    "category": "CLOUD_INFRASTRUCTURE",
    "capabilities": [
      "COMPUTE_RESOURCE_METADATA",
      "NETWORK_AND_REGION_METADATA",
      "INSTANCE_LIFECYCLE_BOUNDARY",
      "INFRASTRUCTURE_ACCOUNT_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "wasabi",
    "package_name": "wasabi_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-WASABI-CORE-ECOSYSTEM",
    "name": "WASABI",
    "category": "EDGE_CDN_AND_OBJECT_STORAGE",
    "capabilities": [
      "EDGE_DISTRIBUTION_METADATA",
      "CACHE_CONFIGURATION_METADATA",
      "OBJECT_STORAGE_REFERENCE",
      "ORIGIN_CONFIGURATION_BOUNDARY"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "webdock",
    "package_name": "webdock_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-WEBDOCK-CORE-ECOSYSTEM",
    "name": "WEBDOCK",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "wordpress_com",
    "package_name": "wordpress_com_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-WORDPRESS_COM-CORE-ECOSYSTEM",
    "name": "WORDPRESS COM",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "wpengine",
    "package_name": "wpengine_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-WPENGINE-CORE-ECOSYSTEM",
    "name": "WP ENGINE",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "wpx",
    "package_name": "wpx_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-WPX-CORE-ECOSYSTEM",
    "name": "WPX",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  },
  {
    "provider_id": "yotta",
    "package_name": "yotta_hosting_core_ecosystem",
    "ecosystem_id": "GLOBAL-HOSTING-YOTTA-CORE-ECOSYSTEM",
    "name": "YOTTA",
    "category": "WEB_AND_MANAGED_HOSTING",
    "capabilities": [
      "HOSTING_PLAN_METADATA",
      "DOMAIN_AND_SITE_ASSOCIATION",
      "SERVER_RESOURCE_METADATA",
      "BACKUP_AND_RESTORE_POLICY_REFERENCE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "enabled": true,
    "api_available": null,
    "connected": false,
    "live_connection_verified": false,
    "api_calls_performed": 0
  }
])

HOSTING_CAPABILITY_PACKAGES: tuple[dict[str, Any], ...] = tuple([
  {
    "package_name": "app_platform_hosting_core_ecosystem",
    "capability_id": "APP_PLATFORM",
    "name": "APP PLATFORM",
    "status": "CAPABILITY_PACKAGE"
  },
  {
    "package_name": "cloud_hosting_hosting_core_ecosystem",
    "capability_id": "CLOUD_HOSTING",
    "name": "CLOUD HOSTING",
    "status": "CAPABILITY_PACKAGE"
  },
  {
    "package_name": "dedicated_vps_hosting_core_ecosystem",
    "capability_id": "DEDICATED_VPS",
    "name": "DEDICATED VPS",
    "status": "CAPABILITY_PACKAGE"
  },
  {
    "package_name": "edge_storage_cdn_hosting_core_ecosystem",
    "capability_id": "EDGE_STORAGE_CDN",
    "name": "EDGE STORAGE CDN",
    "status": "CAPABILITY_PACKAGE"
  },
  {
    "package_name": "india_hosting_hosting_core_ecosystem",
    "capability_id": "INDIA_HOSTING",
    "name": "INDIA HOSTING",
    "status": "CAPABILITY_PACKAGE"
  },
  {
    "package_name": "privacy_specialty_hosting_core_ecosystem",
    "capability_id": "PRIVACY_SPECIALTY",
    "name": "PRIVACY SPECIALTY",
    "status": "CAPABILITY_PACKAGE"
  },
  {
    "package_name": "web_hosting_hosting_core_ecosystem",
    "capability_id": "WEB_HOSTING",
    "name": "WEB HOSTING",
    "status": "CAPABILITY_PACKAGE"
  }
])

def list_hosting_providers(*, category: str | None = None) -> list[dict[str, Any]]:
    records = HOSTING_PROVIDER_CATALOG
    if category:
        records = tuple(item for item in records if item["category"] == category)
    return [deepcopy({**item, "status": "CORE_CATALOG_ONLY", "api_available": None,
                      "connected": False, "live_connection_verified": False,
                      "api_calls_performed": 0}) for item in records]

def get_hosting_provider(provider_id: str) -> dict[str, Any] | None:
    key = str(provider_id).strip().casefold()
    for item in HOSTING_PROVIDER_CATALOG:
        if item["provider_id"].casefold() == key:
            return list_hosting_providers()[HOSTING_PROVIDER_CATALOG.index(item)]
    return None

def list_hosting_capability_packages() -> list[dict[str, Any]]:
    return [deepcopy(item) for item in HOSTING_CAPABILITY_PACKAGES]

def hosting_provider_summary() -> dict[str, Any]:
    records = list_hosting_providers()
    return {
        "provider_count": len(records),
        "capability_package_count": len(HOSTING_CAPABILITY_PACKAGES),
        "hosting_related_child_folder_count": len(records) + len(HOSTING_CAPABILITY_PACKAGES),
        "catalog_only_count": sum(item["status"] == "CORE_CATALOG_ONLY" for item in records),
        "live_connection_verified_count": sum(item["live_connection_verified"] for item in records),
        "api_calls_performed": sum(item["api_calls_performed"] for item in records),
        "categories": {category: sum(item["category"] == category for item in records)
                       for category in sorted({item["category"] for item in records})},
    }
