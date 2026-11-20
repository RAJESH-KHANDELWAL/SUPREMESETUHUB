"""Canonical provider inventory."""
from copy import deepcopy
from .hosting_categories import classify_provider
ROOT_ID="GLOBAL-HOSTING-CORE-ECOSYSTEM"
ROOT={"ecosystem_id":ROOT_ID,"name":"GLOBAL HOSTING CORE ECOSYSTEM","category":"ROOT","parent_id":None,"status":"CORE_CATALOG_ONLY","capabilities":["HOSTING_PROVIDER_REGISTRY","CAPABILITY_METADATA","READINESS_REPORTING"],"live_connection_verified":False}
PROVIDERS=[
  {
    "ecosystem_id": "GLOBAL-ABELOHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ABELOHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "ABELOHOST",
    "provider_name": "ABELOHOST",
    "category": "HOSTING_PROVIDER",
    "sort_order": 1,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ACQUIA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ACQUIA HOSTING CORE ECOSYSTEM",
    "provider_id": "ACQUIA",
    "provider_name": "ACQUIA",
    "category": "HOSTING_PROVIDER",
    "sort_order": 2,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-AKAMAI-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL AKAMAI HOSTING CORE ECOSYSTEM",
    "provider_id": "AKAMAI",
    "provider_name": "AKAMAI",
    "category": "HOSTING_PROVIDER",
    "sort_order": 3,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ALEXHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ALEXHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "ALEXHOST",
    "provider_name": "ALEXHOST",
    "category": "HOSTING_PROVIDER",
    "sort_order": 4,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ALIBABA-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ALIBABA CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "ALIBABA_CLOUD",
    "provider_name": "ALIBABA CLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 5,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-APP-PLATFORM-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL APP PLATFORM HOSTING CORE ECOSYSTEM",
    "provider_id": "APP_PLATFORM",
    "provider_name": "APP PLATFORM",
    "category": "HOSTING_PROVIDER",
    "sort_order": 6,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-APPWRITE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL APPWRITE HOSTING CORE ECOSYSTEM",
    "provider_id": "APPWRITE",
    "provider_name": "APPWRITE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 7,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-AWARDSPACE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL AWARDSPACE HOSTING CORE ECOSYSTEM",
    "provider_id": "AWARDSPACE",
    "provider_name": "AWARDSPACE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 8,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-AWS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL AWS HOSTING CORE ECOSYSTEM",
    "provider_id": "AWS",
    "provider_name": "AWS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 9,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-BACKBLAZE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL BACKBLAZE HOSTING CORE ECOSYSTEM",
    "provider_id": "BACKBLAZE",
    "provider_name": "BACKBLAZE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 10,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-BIGROCK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL BIGROCK HOSTING CORE ECOSYSTEM",
    "provider_id": "BIGROCK",
    "provider_name": "BIGROCK",
    "category": "HOSTING_PROVIDER",
    "sort_order": 11,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-BLUEANGELHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL BLUEANGELHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "BLUEANGELHOST",
    "provider_name": "BLUEANGELHOST",
    "category": "HOSTING_PROVIDER",
    "sort_order": 12,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-BLUEHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL BLUEHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "BLUEHOST",
    "provider_name": "BLUEHOST",
    "category": "HOSTING_PROVIDER",
    "sort_order": 13,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-BUNNY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL BUNNY HOSTING CORE ECOSYSTEM",
    "provider_id": "BUNNY",
    "provider_name": "BUNNY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 14,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-BUYVM-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL BUYVM HOSTING CORE ECOSYSTEM",
    "provider_id": "BUYVM",
    "provider_name": "BUYVM",
    "category": "HOSTING_PROVIDER",
    "sort_order": 15,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CHEMICLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CHEMICLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "CHEMICLOUD",
    "provider_name": "CHEMICLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 16,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "CLOUD",
    "provider_name": "CLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 17,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CLOUDFLARE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CLOUDFLARE HOSTING CORE ECOSYSTEM",
    "provider_id": "CLOUDFLARE",
    "provider_name": "CLOUDFLARE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 18,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CLOUDWAYS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CLOUDWAYS HOSTING CORE ECOSYSTEM",
    "provider_id": "CLOUDWAYS",
    "provider_name": "CLOUDWAYS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 19,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-COMBELL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL COMBELL HOSTING CORE ECOSYSTEM",
    "provider_id": "COMBELL",
    "provider_name": "COMBELL",
    "category": "HOSTING_PROVIDER",
    "sort_order": 20,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CONTABO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CONTABO HOSTING CORE ECOSYSTEM",
    "provider_id": "CONTABO",
    "provider_name": "CONTABO",
    "category": "HOSTING_PROVIDER",
    "sort_order": 21,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CPANEL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CPANEL HOSTING CORE ECOSYSTEM",
    "provider_id": "CPANEL",
    "provider_name": "CPANEL",
    "category": "HOSTING_PROVIDER",
    "sort_order": 22,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CRAZYDOMAINS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CRAZYDOMAINS HOSTING CORE ECOSYSTEM",
    "provider_id": "CRAZYDOMAINS",
    "provider_name": "CRAZYDOMAINS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 23,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CTRLS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CTRLS HOSTING CORE ECOSYSTEM",
    "provider_id": "CTRLS",
    "provider_name": "CTRLS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 24,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-DEDICATED-VPS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL DEDICATED VPS HOSTING CORE ECOSYSTEM",
    "provider_id": "DEDICATED_VPS",
    "provider_name": "DEDICATED VPS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 25,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-DIGITALOCEAN-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL DIGITALOCEAN HOSTING CORE ECOSYSTEM",
    "provider_id": "DIGITALOCEAN",
    "provider_name": "DIGITALOCEAN",
    "category": "HOSTING_PROVIDER",
    "sort_order": 26,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-DREAMHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL DREAMHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "DREAMHOST",
    "provider_name": "DREAMHOST",
    "category": "HOSTING_PROVIDER",
    "sort_order": 27,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-E2ENETWORKS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL E2ENETWORKS HOSTING CORE ECOSYSTEM",
    "provider_id": "E2ENETWORKS",
    "provider_name": "E2ENETWORKS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 28,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-EDGE-STORAGE-CDN-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL EDGE STORAGE CDN HOSTING CORE ECOSYSTEM",
    "provider_id": "EDGE_STORAGE_CDN",
    "provider_name": "EDGE STORAGE CDN",
    "category": "HOSTING_PROVIDER",
    "sort_order": 29,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-EQUINIX-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL EQUINIX HOSTING CORE ECOSYSTEM",
    "provider_id": "EQUINIX",
    "provider_name": "EQUINIX",
    "category": "HOSTING_PROVIDER",
    "sort_order": 30,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-FASTCOMET-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL FASTCOMET HOSTING CORE ECOSYSTEM",
    "provider_id": "FASTCOMET",
    "provider_name": "FASTCOMET",
    "category": "HOSTING_PROVIDER",
    "sort_order": 31,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-FASTLY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL FASTLY HOSTING CORE ECOSYSTEM",
    "provider_id": "FASTLY",
    "provider_name": "FASTLY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 32,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-FIREBASE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL FIREBASE HOSTING CORE ECOSYSTEM",
    "provider_id": "FIREBASE",
    "provider_name": "FIREBASE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 33,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-FLOKINET-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL FLOKINET HOSTING CORE ECOSYSTEM",
    "provider_id": "FLOKINET",
    "provider_name": "FLOKINET",
    "category": "HOSTING_PROVIDER",
    "sort_order": 34,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-FLYIO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL FLYIO HOSTING CORE ECOSYSTEM",
    "provider_id": "FLYIO",
    "provider_name": "FLYIO",
    "category": "HOSTING_PROVIDER",
    "sort_order": 35,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GANDI-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GANDI HOSTING CORE ECOSYSTEM",
    "provider_id": "GANDI",
    "provider_name": "GANDI",
    "category": "HOSTING_PROVIDER",
    "sort_order": 36,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GCORE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GCORE HOSTING CORE ECOSYSTEM",
    "provider_id": "GCORE",
    "provider_name": "GCORE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 37,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GITHUB-PAGES-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GITHUB PAGES HOSTING CORE ECOSYSTEM",
    "provider_id": "GITHUB_PAGES",
    "provider_name": "GITHUB PAGES",
    "category": "HOSTING_PROVIDER",
    "sort_order": 38,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GITLAB-PAGES-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GITLAB PAGES HOSTING CORE ECOSYSTEM",
    "provider_id": "GITLAB_PAGES",
    "provider_name": "GITLAB PAGES",
    "category": "HOSTING_PROVIDER",
    "sort_order": 39,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GODADDY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GODADDY HOSTING CORE ECOSYSTEM",
    "provider_id": "GODADDY",
    "provider_name": "GODADDY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 40,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GOOGLE-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GOOGLE CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "GOOGLE_CLOUD",
    "provider_name": "GOOGLE CLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 41,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GREENCLOUDVPS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GREENCLOUDVPS HOSTING CORE ECOSYSTEM",
    "provider_id": "GREENCLOUDVPS",
    "provider_name": "GREENCLOUDVPS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 42,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GREENGEEKS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GREENGEEKS HOSTING CORE ECOSYSTEM",
    "provider_id": "GREENGEEKS",
    "provider_name": "GREENGEEKS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 43,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HEROKU-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HEROKU HOSTING CORE ECOSYSTEM",
    "provider_id": "HEROKU",
    "provider_name": "HEROKU",
    "category": "HOSTING_PROVIDER",
    "sort_order": 44,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HETZNER-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HETZNER HOSTING CORE ECOSYSTEM",
    "provider_id": "HETZNER",
    "provider_name": "HETZNER",
    "category": "HOSTING_PROVIDER",
    "sort_order": 45,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HIVELOCITY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HIVELOCITY HOSTING CORE ECOSYSTEM",
    "provider_id": "HIVELOCITY",
    "provider_name": "HIVELOCITY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 46,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTARMADA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTARMADA HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTARMADA",
    "provider_name": "HOSTARMADA",
    "category": "HOSTING_PROVIDER",
    "sort_order": 47,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTGATOR-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTGATOR HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTGATOR",
    "provider_name": "HOSTGATOR",
    "category": "HOSTING_PROVIDER",
    "sort_order": 48,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTGATORINDIA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTGATORINDIA HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTGATORINDIA",
    "provider_name": "HOSTGATORINDIA",
    "category": "HOSTING_PROVIDER",
    "sort_order": 49,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTING-COM-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTING COM HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTING_COM",
    "provider_name": "HOSTING COM",
    "category": "HOSTING_PROVIDER",
    "sort_order": 50,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTINGER-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTINGER HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTINGER",
    "provider_name": "HOSTINGER",
    "category": "HOSTING_PROVIDER",
    "sort_order": 51,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTINGRAJA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTINGRAJA HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTINGRAJA",
    "provider_name": "HOSTINGRAJA",
    "category": "HOSTING_PROVIDER",
    "sort_order": 52,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTITSMART-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTITSMART HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTITSMART",
    "provider_name": "HOSTITSMART",
    "category": "HOSTING_PROVIDER",
    "sort_order": 53,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTKEY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTKEY HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTKEY",
    "provider_name": "HOSTKEY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 54,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTPAPA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTPAPA HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTPAPA",
    "provider_name": "HOSTPAPA",
    "category": "HOSTING_PROVIDER",
    "sort_order": 55,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTSAILOR-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTSAILOR HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTSAILOR",
    "provider_name": "HOSTSAILOR",
    "category": "HOSTING_PROVIDER",
    "sort_order": 56,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTWINDS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTWINDS HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTWINDS",
    "provider_name": "HOSTWINDS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 57,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HUAWEI-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HUAWEI CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "HUAWEI_CLOUD",
    "provider_name": "HUAWEI CLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 58,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-IBM-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL IBM CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "IBM_CLOUD",
    "provider_name": "IBM CLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 59,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-INDIA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL INDIA HOSTING CORE ECOSYSTEM",
    "provider_id": "INDIA",
    "provider_name": "INDIA",
    "category": "HOSTING_PROVIDER",
    "sort_order": 60,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-INFINITYFREE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL INFINITYFREE HOSTING CORE ECOSYSTEM",
    "provider_id": "INFINITYFREE",
    "provider_name": "INFINITYFREE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 61,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-INFOMANIAK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL INFOMANIAK HOSTING CORE ECOSYSTEM",
    "provider_id": "INFOMANIAK",
    "provider_name": "INFOMANIAK",
    "category": "HOSTING_PROVIDER",
    "sort_order": 62,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-INMOTION-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL INMOTION HOSTING CORE ECOSYSTEM",
    "provider_id": "INMOTION",
    "provider_name": "INMOTION",
    "category": "HOSTING_PROVIDER",
    "sort_order": 63,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-INTERSERVER-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL INTERSERVER HOSTING CORE ECOSYSTEM",
    "provider_id": "INTERSERVER",
    "provider_name": "INTERSERVER",
    "category": "HOSTING_PROVIDER",
    "sort_order": 64,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-IONOS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL IONOS HOSTING CORE ECOSYSTEM",
    "provider_id": "IONOS",
    "provider_name": "IONOS",
    "category": "HOSTING_PROVIDER",
    "sort_order": 65,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-KINSTA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL KINSTA HOSTING CORE ECOSYSTEM",
    "provider_id": "KINSTA",
    "provider_name": "KINSTA",
    "category": "HOSTING_PROVIDER",
    "sort_order": 66,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-KNOWNHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL KNOWNHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "KNOWNHOST",
    "provider_name": "KNOWNHOST",
    "category": "HOSTING_PROVIDER",
    "sort_order": 67,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-KOYEB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL KOYEB HOSTING CORE ECOSYSTEM",
    "provider_id": "KOYEB",
    "provider_name": "KOYEB",
    "category": "HOSTING_PROVIDER",
    "sort_order": 68,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-LEASEWEB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL LEASEWEB HOSTING CORE ECOSYSTEM",
    "provider_id": "LEASEWEB",
    "provider_name": "LEASEWEB",
    "category": "HOSTING_PROVIDER",
    "sort_order": 69,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-LINODE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL LINODE HOSTING CORE ECOSYSTEM",
    "provider_id": "LINODE",
    "provider_name": "LINODE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 70,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-LIQUIDWEB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL LIQUIDWEB HOSTING CORE ECOSYSTEM",
    "provider_id": "LIQUIDWEB",
    "provider_name": "LIQUIDWEB",
    "category": "HOSTING_PROVIDER",
    "sort_order": 71,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-M247-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL M247 HOSTING CORE ECOSYSTEM",
    "provider_id": "M247",
    "provider_name": "M247",
    "category": "HOSTING_PROVIDER",
    "sort_order": 72,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-MICROSOFT-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL MICROSOFT HOSTING CORE ECOSYSTEM",
    "provider_id": "MICROSOFT",
    "provider_name": "MICROSOFT",
    "category": "HOSTING_PROVIDER",
    "sort_order": 73,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-MILESWEB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL MILESWEB HOSTING CORE ECOSYSTEM",
    "provider_id": "MILESWEB",
    "provider_name": "MILESWEB",
    "category": "HOSTING_PROVIDER",
    "sort_order": 74,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NAMECHEAP-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NAMECHEAP HOSTING CORE ECOSYSTEM",
    "provider_id": "NAMECHEAP",
    "provider_name": "NAMECHEAP",
    "category": "HOSTING_PROVIDER",
    "sort_order": 75,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NEOCITIES-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NEOCITIES HOSTING CORE ECOSYSTEM",
    "provider_id": "NEOCITIES",
    "provider_name": "NEOCITIES",
    "category": "HOSTING_PROVIDER",
    "sort_order": 76,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NETLIFY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NETLIFY HOSTING CORE ECOSYSTEM",
    "provider_id": "NETLIFY",
    "provider_name": "NETLIFY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 77,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NETMAGIC-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NETMAGIC HOSTING CORE ECOSYSTEM",
    "provider_id": "NETMAGIC",
    "provider_name": "NETMAGIC",
    "category": "HOSTING_PROVIDER",
    "sort_order": 78,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NORTHFLANK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NORTHFLANK HOSTING CORE ECOSYSTEM",
    "provider_id": "NORTHFLANK",
    "provider_name": "NORTHFLANK",
    "category": "HOSTING_PROVIDER",
    "sort_order": 79,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ONE-COM-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ONE COM HOSTING CORE ECOSYSTEM",
    "provider_id": "ONE_COM",
    "provider_name": "ONE COM",
    "category": "HOSTING_PROVIDER",
    "sort_order": 80,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ORACLE-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ORACLE CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "ORACLE_CLOUD",
    "provider_name": "ORACLE CLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 81,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-OVHCLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL OVHCLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "OVHCLOUD",
    "provider_name": "OVHCLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 82,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PAGELY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PAGELY HOSTING CORE ECOSYSTEM",
    "provider_id": "PAGELY",
    "provider_name": "PAGELY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 83,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PANTHEON-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PANTHEON HOSTING CORE ECOSYSTEM",
    "provider_id": "PANTHEON",
    "provider_name": "PANTHEON",
    "category": "HOSTING_PROVIDER",
    "sort_order": 84,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PHOENIXNAP-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PHOENIXNAP HOSTING CORE ECOSYSTEM",
    "provider_id": "PHOENIXNAP",
    "provider_name": "PHOENIXNAP",
    "category": "HOSTING_PROVIDER",
    "sort_order": 85,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PLATFORM-SH-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PLATFORM SH HOSTING CORE ECOSYSTEM",
    "provider_id": "PLATFORM_SH",
    "provider_name": "PLATFORM SH",
    "category": "HOSTING_PROVIDER",
    "sort_order": 86,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PLESK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PLESK HOSTING CORE ECOSYSTEM",
    "provider_id": "PLESK",
    "provider_name": "PLESK",
    "category": "HOSTING_PROVIDER",
    "sort_order": 87,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PRESSABLE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PRESSABLE HOSTING CORE ECOSYSTEM",
    "provider_id": "PRESSABLE",
    "provider_name": "PRESSABLE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 88,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PRIVACY-SPECIALTY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PRIVACY SPECIALTY HOSTING CORE ECOSYSTEM",
    "provider_id": "PRIVACY_SPECIALTY",
    "provider_name": "PRIVACY SPECIALTY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 89,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-RACKSPACE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL RACKSPACE HOSTING CORE ECOSYSTEM",
    "provider_id": "RACKSPACE",
    "provider_name": "RACKSPACE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 90,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-RAILWAY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL RAILWAY HOSTING CORE ECOSYSTEM",
    "provider_id": "RAILWAY",
    "provider_name": "RAILWAY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 91,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-RAMNODE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL RAMNODE HOSTING CORE ECOSYSTEM",
    "provider_id": "RAMNODE",
    "provider_name": "RAMNODE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 92,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-RENDER-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL RENDER HOSTING CORE ECOSYSTEM",
    "provider_id": "RENDER",
    "provider_name": "RENDER",
    "category": "HOSTING_PROVIDER",
    "sort_order": 93,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-REPLIT-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL REPLIT HOSTING CORE ECOSYSTEM",
    "provider_id": "REPLIT",
    "provider_name": "REPLIT",
    "category": "HOSTING_PROVIDER",
    "sort_order": 94,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-RESELLERCLUB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL RESELLERCLUB HOSTING CORE ECOSYSTEM",
    "provider_id": "RESELLERCLUB",
    "provider_name": "RESELLERCLUB",
    "category": "HOSTING_PROVIDER",
    "sort_order": 95,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-RUNCLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL RUNCLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "RUNCLOUD",
    "provider_name": "RUNCLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 96,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SCALEWAY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SCALEWAY HOSTING CORE ECOSYSTEM",
    "provider_id": "SCALEWAY",
    "provider_name": "SCALEWAY",
    "category": "HOSTING_PROVIDER",
    "sort_order": 97,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SERVERION-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SERVERION HOSTING CORE ECOSYSTEM",
    "provider_id": "SERVERION",
    "provider_name": "SERVERION",
    "category": "HOSTING_PROVIDER",
    "sort_order": 98,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SHINJIRU-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SHINJIRU HOSTING CORE ECOSYSTEM",
    "provider_id": "SHINJIRU",
    "provider_name": "SHINJIRU",
    "category": "HOSTING_PROVIDER",
    "sort_order": 99,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SITEGROUND-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SITEGROUND HOSTING CORE ECOSYSTEM",
    "provider_id": "SITEGROUND",
    "provider_name": "SITEGROUND",
    "category": "HOSTING_PROVIDER",
    "sort_order": 100,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-STRATO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL STRATO HOSTING CORE ECOSYSTEM",
    "provider_id": "STRATO",
    "provider_name": "STRATO",
    "category": "HOSTING_PROVIDER",
    "sort_order": 101,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SUPABASE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SUPABASE HOSTING CORE ECOSYSTEM",
    "provider_id": "SUPABASE",
    "provider_name": "SUPABASE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 102,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SURGE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SURGE HOSTING CORE ECOSYSTEM",
    "provider_id": "SURGE",
    "provider_name": "SURGE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 103,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-TENCENT-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL TENCENT CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "TENCENT_CLOUD",
    "provider_name": "TENCENT CLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 104,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-TRANSIP-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL TRANSIP HOSTING CORE ECOSYSTEM",
    "provider_id": "TRANSIP",
    "provider_name": "TRANSIP",
    "category": "HOSTING_PROVIDER",
    "sort_order": 105,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-UPCLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL UPCLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "UPCLOUD",
    "provider_name": "UPCLOUD",
    "category": "HOSTING_PROVIDER",
    "sort_order": 106,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-VENTRAIP-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL VENTRAIP HOSTING CORE ECOSYSTEM",
    "provider_id": "VENTRAIP",
    "provider_name": "VENTRAIP",
    "category": "HOSTING_PROVIDER",
    "sort_order": 107,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-VERCEL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL VERCEL HOSTING CORE ECOSYSTEM",
    "provider_id": "VERCEL",
    "provider_name": "VERCEL",
    "category": "HOSTING_PROVIDER",
    "sort_order": 108,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-VERPEX-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL VERPEX HOSTING CORE ECOSYSTEM",
    "provider_id": "VERPEX",
    "provider_name": "VERPEX",
    "category": "HOSTING_PROVIDER",
    "sort_order": 109,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-VICETEMPLE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL VICETEMPLE HOSTING CORE ECOSYSTEM",
    "provider_id": "VICETEMPLE",
    "provider_name": "VICETEMPLE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 110,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-VULTR-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL VULTR HOSTING CORE ECOSYSTEM",
    "provider_id": "VULTR",
    "provider_name": "VULTR",
    "category": "HOSTING_PROVIDER",
    "sort_order": 111,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WASABI-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WASABI HOSTING CORE ECOSYSTEM",
    "provider_id": "WASABI",
    "provider_name": "WASABI",
    "category": "HOSTING_PROVIDER",
    "sort_order": 112,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WEB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WEB HOSTING CORE ECOSYSTEM",
    "provider_id": "WEB",
    "provider_name": "WEB",
    "category": "HOSTING_PROVIDER",
    "sort_order": 113,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WEBDOCK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WEBDOCK HOSTING CORE ECOSYSTEM",
    "provider_id": "WEBDOCK",
    "provider_name": "WEBDOCK",
    "category": "HOSTING_PROVIDER",
    "sort_order": 114,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WORDPRESS-COM-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WORDPRESS COM HOSTING CORE ECOSYSTEM",
    "provider_id": "WORDPRESS_COM",
    "provider_name": "WORDPRESS COM",
    "category": "HOSTING_PROVIDER",
    "sort_order": 115,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WPENGINE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WPENGINE HOSTING CORE ECOSYSTEM",
    "provider_id": "WPENGINE",
    "provider_name": "WPENGINE",
    "category": "HOSTING_PROVIDER",
    "sort_order": 116,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WPX-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WPX HOSTING CORE ECOSYSTEM",
    "provider_id": "WPX",
    "provider_name": "WPX",
    "category": "HOSTING_PROVIDER",
    "sort_order": 117,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-YOTTA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL YOTTA HOSTING CORE ECOSYSTEM",
    "provider_id": "YOTTA",
    "provider_name": "YOTTA",
    "category": "HOSTING_PROVIDER",
    "sort_order": 118,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": [
      "HOSTING_METADATA",
      "PROVIDER_DISCOVERY",
      "CAPABILITY_CLASSIFICATION",
      "READINESS_REPORTING"
    ],
    "live_connection_verified": false,
    "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-AKILE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL AKILE HOSTING CORE ECOSYSTEM",
    "provider_id": "AKILE", "provider_name": "AKILE",
    "category": "HOSTING_PROVIDER", "sort_order": 119,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ALWAYS--HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ALWAYS  HOSTING CORE ECOSYSTEM",
    "provider_id": "ALWAYSdata", "provider_name": "ALWAYS ",
    "category": "HOSTING_PROVIDER", "sort_order": 120,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-A2-HOSTING-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL A2 HOSTING HOSTING CORE ECOSYSTEM",
    "provider_id": "A2_HOSTING", "provider_name": "A2 HOSTING",
    "category": "HOSTING_PROVIDER", "sort_order": 121,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ACCUPWEB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ACCUPWEB HOSTING CORE ECOSYSTEM",
    "provider_id": "ACCUPWEB", "provider_name": "ACCUPWEB",
    "category": "HOSTING_PROVIDER", "sort_order": 122,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ASPHOSTPORTAL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ASPHOSTPORTAL HOSTING CORE ECOSYSTEM",
    "provider_id": "ASPHOSTPORTAL", "provider_name": "ASPHOSTPORTAL",
    "category": "HOSTING_PROVIDER", "sort_order": 123,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CHEAPO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CHEAPO HOSTING CORE ECOSYSTEM",
    "provider_id": "CHEAPO", "provider_name": "CHEAPO",
    "category": "HOSTING_PROVIDER", "sort_order": 124,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-DREAMHOST-PRO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL DREAMHOST PRO HOSTING CORE ECOSYSTEM",
    "provider_id": "DREAMHOST_PRO", "provider_name": "DREAMHOST PRO",
    "category": "HOSTING_PROVIDER", "sort_order": 125,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-FLYWHEEL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL FLYWHEEL HOSTING CORE ECOSYSTEM",
    "provider_id": "FLYWHEEL", "provider_name": "FLYWHEEL",
    "category": "HOSTING_PROVIDER", "sort_order": 126,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GODADDY-PRO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GODADDY PRO HOSTING CORE ECOSYSTEM",
    "provider_id": "GODADDY_PRO", "provider_name": "GODADDY PRO",
    "category": "HOSTING_PROVIDER", "sort_order": 127,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTINGUK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTINGUK HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTINGUK", "provider_name": "HOSTINGUK",
    "category": "HOSTING_PROVIDER", "sort_order": 128,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTMANTIS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTMANTIS HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTMANTIS", "provider_name": "HOSTMANTIS",
    "category": "HOSTING_PROVIDER", "sort_order": 129,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTROCKET-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTROCKET HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTROCKET", "provider_name": "HOSTROCKET",
    "category": "HOSTING_PROVIDER", "sort_order": 130,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTROUND-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTROUND HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTROUND", "provider_name": "HOSTROUND",
    "category": "HOSTING_PROVIDER", "sort_order": 131,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-INTERNETVIKINGS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL INTERNETVIKINGS HOSTING CORE ECOSYSTEM",
    "provider_id": "INTERNETVIKINGS", "provider_name": "INTERNETVIKINGS",
    "category": "HOSTING_PROVIDER", "sort_order": 132,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-KRYSTAL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL KRYSTAL HOSTING CORE ECOSYSTEM",
    "provider_id": "KRYSTAL", "provider_name": "KRYSTAL",
    "category": "HOSTING_PROVIDER", "sort_order": 133,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-LIQUID-WEB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL LIQUID WEB HOSTING CORE ECOSYSTEM",
    "provider_id": "LIQUID_WEB", "provider_name": "LIQUID WEB",
    "category": "HOSTING_PROVIDER", "sort_order": 134,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-MDDHOSTING-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL MDDHOSTING HOSTING CORE ECOSYSTEM",
    "provider_id": "MDDHOSTING", "provider_name": "MDDHOSTING",
    "category": "HOSTING_PROVIDER", "sort_order": 135,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NAMESILO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NAMESILO HOSTING CORE ECOSYSTEM",
    "provider_id": "NAMESILO", "provider_name": "NAMESILO",
    "category": "HOSTING_PROVIDER", "sort_order": 136,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NEXCESS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NEXCESS HOSTING CORE ECOSYSTEM",
    "provider_id": "NEXCESS", "provider_name": "NEXCESS",
    "category": "HOSTING_PROVIDER", "sort_order": 137,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PORKBUN-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PORKBUN HOSTING CORE ECOSYSTEM",
    "provider_id": "PORKBUN", "provider_name": "PORKBUN",
    "category": "HOSTING_PROVIDER", "sort_order": 138,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ROCKHOSTER-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ROCKHOSTER HOSTING CORE ECOSYSTEM",
    "provider_id": "ROCKHOSTER", "provider_name": "ROCKHOSTER",
    "category": "HOSTING_PROVIDER", "sort_order": 139,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SCALAHOSTING-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SCALAHOSTING HOSTING CORE ECOSYSTEM",
    "provider_id": "SCALAHOSTING", "provider_name": "SCALAHOSTING",
    "category": "HOSTING_PROVIDER", "sort_order": 140,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SERVERS-COM-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SERVERS COM HOSTING CORE ECOSYSTEM",
    "provider_id": "SERVERS.COM", "provider_name": "SERVERS COM",
    "category": "HOSTING_PROVIDER", "sort_order": 141,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-STABLEPOINT-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL STABLEPOINT HOSTING CORE ECOSYSTEM",
    "provider_id": "STABLEPOINT", "provider_name": "STABLEPOINT",
    "category": "HOSTING_PROVIDER", "sort_order": 142,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-TEMOK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL TEMOK HOSTING CORE ECOSYSTEM",
    "provider_id": "TEMOK", "provider_name": "TEMOK",
    "category": "HOSTING_PROVIDER", "sort_order": 143,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-THE-ONLINE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL THE ONLINE HOSTING CORE ECOSYSTEM",
    "provider_id": "THE_ONLINE", "provider_name": "THE ONLINE",
    "category": "HOSTING_PROVIDER", "sort_order": 144,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ULTAHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ULTAHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "ULTAHOST", "provider_name": "ULTAHOST",
    "category": "HOSTING_PROVIDER", "sort_order": 145,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WEBHOSTINGPAD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WEBHOSTINGPAD HOSTING CORE ECOSYSTEM",
    "provider_id": "WEBHOSTINGPAD", "provider_name": "WEBHOSTINGPAD",
    "category": "HOSTING_PROVIDER", "sort_order": 146,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WEBHOSTUK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WEBHOSTUK HOSTING CORE ECOSYSTEM",
    "provider_id": "WEBHOSTUK", "provider_name": "WEBHOSTUK",
    "category": "HOSTING_PROVIDER", "sort_order": 147,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WP-SERVERS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WP SERVERS HOSTING CORE ECOSYSTEM",
    "provider_id": "WP_SERVERS", "provider_name": "WP SERVERS",
    "category": "HOSTING_PROVIDER", "sort_order": 148,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-XSERVER-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL XSERVER HOSTING CORE ECOSYSTEM",
    "provider_id": "XSERVER", "provider_name": "XSERVER",
    "category": "HOSTING_PROVIDER", "sort_order": 149,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ZUME-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ZUME HOSTING CORE ECOSYSTEM",
    "provider_id": "ZUME", "provider_name": "ZUME",
    "category": "HOSTING_PROVIDER", "sort_order": 150,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GREENHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GREENHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "GREENHOST", "provider_name": "GREENHOST",
    "category": "HOSTING_PROVIDER", "sort_order": 151,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTNET-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTNET HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTNET", "provider_name": "HOSTNET",
    "category": "HOSTING_PROVIDER", "sort_order": 152,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTING-COM-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTING COM HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTING.COM", "provider_name": "HOSTING COM",
    "category": "HOSTING_PROVIDER", "sort_order": 153,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTINGER-PRO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTINGER PRO HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTINGER_PRO", "provider_name": "HOSTINGER PRO",
    "category": "HOSTING_PROVIDER", "sort_order": 154,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-KAMATERA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL KAMATERA HOSTING CORE ECOSYSTEM",
    "provider_id": "KAMATERA", "provider_name": "KAMATERA",
    "category": "HOSTING_PROVIDER", "sort_order": 155,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-LEASEWEB-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL LEASEWEB CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "LEASEWEB_CLOUD", "provider_name": "LEASEWEB CLOUD",
    "category": "HOSTING_PROVIDER", "sort_order": 156,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-LINODE-AKAMAI-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL LINODE AKAMAI HOSTING CORE ECOSYSTEM",
    "provider_id": "LINODE_AKAMAI", "provider_name": "LINODE AKAMAI",
    "category": "HOSTING_PROVIDER", "sort_order": 157,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ORACLE-CLOUD-INFRASTRUCTURE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ORACLE CLOUD INFRASTRUCTURE HOSTING CORE ECOSYSTEM",
    "provider_id": "ORACLE_CLOUD_INFRASTRUCTURE", "provider_name": "ORACLE CLOUD INFRASTRUCTURE",
    "category": "HOSTING_PROVIDER", "sort_order": 158,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-OVH-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL OVH CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "OVH_CLOUD", "provider_name": "OVH CLOUD",
    "category": "HOSTING_PROVIDER", "sort_order": 159,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-VPSDIME-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL VPSDIME HOSTING CORE ECOSYSTEM",
    "provider_id": "VPSDIME", "provider_name": "VPSDIME",
    "category": "HOSTING_PROVIDER", "sort_order": 160,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-UPTIME-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL UPTIME HOSTING CORE ECOSYSTEM",
    "provider_id": "UPTIME", "provider_name": "UPTIME",
    "category": "HOSTING_PROVIDER", "sort_order": 161,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PANTHEON-PLATFORM-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PANTHEON PLATFORM HOSTING CORE ECOSYSTEM",
    "provider_id": "PANTHEON_PLATFORM", "provider_name": "PANTHEON PLATFORM",
    "category": "HOSTING_PROVIDER", "sort_order": 162,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CLOUDFOUNDRY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CLOUDFOUNDRY HOSTING CORE ECOSYSTEM",
    "provider_id": "CLOUDFOUNDRY", "provider_name": "CLOUDFOUNDRY",
    "category": "HOSTING_PROVIDER", "sort_order": 163,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-DENO-DEPLOY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL DENO DEPLOY HOSTING CORE ECOSYSTEM",
    "provider_id": "DENO_DEPLOY", "provider_name": "DENO DEPLOY",
    "category": "HOSTING_PROVIDER", "sort_order": 164,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-FLY-DEPLOY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL FLY DEPLOY HOSTING CORE ECOSYSTEM",
    "provider_id": "FLY_DEPLOY", "provider_name": "FLY DEPLOY",
    "category": "HOSTING_PROVIDER", "sort_order": 165,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GOOGLE-APP-ENGINE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GOOGLE APP ENGINE HOSTING CORE ECOSYSTEM",
    "provider_id": "GOOGLE_APP_ENGINE", "provider_name": "GOOGLE APP ENGINE",
    "category": "HOSTING_PROVIDER", "sort_order": 166,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-VERCEL-EDGE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL VERCEL EDGE HOSTING CORE ECOSYSTEM",
    "provider_id": "VERCEL_EDGE", "provider_name": "VERCEL EDGE",
    "category": "HOSTING_PROVIDER", "sort_order": 167,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CLOUDFRONT-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CLOUDFRONT HOSTING CORE ECOSYSTEM",
    "provider_id": "CLOUDFRONT", "provider_name": "CLOUDFRONT",
    "category": "HOSTING_PROVIDER", "sort_order": 168,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-KEYCDN-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL KEYCDN HOSTING CORE ECOSYSTEM",
    "provider_id": "KEYCDN", "provider_name": "KEYCDN",
    "category": "HOSTING_PROVIDER", "sort_order": 169,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-EDGIO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL EDGIO HOSTING CORE ECOSYSTEM",
    "provider_id": "EDGIO", "provider_name": "EDGIO",
    "category": "HOSTING_PROVIDER", "sort_order": 170,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-STACKPATH-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL STACKPATH HOSTING CORE ECOSYSTEM",
    "provider_id": "STACKPATH", "provider_name": "STACKPATH",
    "category": "HOSTING_PROVIDER", "sort_order": 171,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CLOUDFLARE-R2-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CLOUDFLARE R2 HOSTING CORE ECOSYSTEM",
    "provider_id": "CLOUDFLARE_R2", "provider_name": "CLOUDFLARE R2",
    "category": "HOSTING_PROVIDER", "sort_order": 172,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-IDRIVE-E2-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL IDRIVE E2 HOSTING CORE ECOSYSTEM",
    "provider_id": "IDRIVE_E2", "provider_name": "IDRIVE E2",
    "category": "HOSTING_PROVIDER", "sort_order": 173,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-LINODE-OBJECT-STORAGE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL LINODE OBJECT STORAGE HOSTING CORE ECOSYSTEM",
    "provider_id": "LINODE_OBJECT_STORAGE", "provider_name": "LINODE OBJECT STORAGE",
    "category": "HOSTING_PROVIDER", "sort_order": 174,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-DIGITALOCEAN-SPACES-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL DIGITALOCEAN SPACES HOSTING CORE ECOSYSTEM",
    "provider_id": "DIGITALOCEAN_SPACES", "provider_name": "DIGITALOCEAN SPACES",
    "category": "HOSTING_PROVIDER", "sort_order": 175,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-STORJ-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL STORJ HOSTING CORE ECOSYSTEM",
    "provider_id": "STORJ", "provider_name": "STORJ",
    "category": "HOSTING_PROVIDER", "sort_order": 176,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-CLOUDINARY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL CLOUDINARY HOSTING CORE ECOSYSTEM",
    "provider_id": "CLOUDINARY", "provider_name": "CLOUDINARY",
    "category": "HOSTING_PROVIDER", "sort_order": 177,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NEON-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NEON HOSTING CORE ECOSYSTEM",
    "provider_id": "NEON", "provider_name": "NEON",
    "category": "HOSTING_PROVIDER", "sort_order": 178,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-PLANETSCALE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL PLANETSCALE HOSTING CORE ECOSYSTEM",
    "provider_id": "PLANETSCALE", "provider_name": "PLANETSCALE",
    "category": "HOSTING_PROVIDER", "sort_order": 179,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-TURSO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL TURSO HOSTING CORE ECOSYSTEM",
    "provider_id": "TURSO", "provider_name": "TURSO",
    "category": "HOSTING_PROVIDER", "sort_order": 180,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-UPSTASH-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL UPSTASH HOSTING CORE ECOSYSTEM",
    "provider_id": "UPSTASH", "provider_name": "UPSTASH",
    "category": "HOSTING_PROVIDER", "sort_order": 181,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-AIVEN-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL AIVEN HOSTING CORE ECOSYSTEM",
    "provider_id": "AIVEN", "provider_name": "AIVEN",
    "category": "HOSTING_PROVIDER", "sort_order": 182,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-MONGODB-ATLAS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL MONGODB ATLAS HOSTING CORE ECOSYSTEM",
    "provider_id": "MONGODB_ATLAS", "provider_name": "MONGODB ATLAS",
    "category": "HOSTING_PROVIDER", "sort_order": 183,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-REDIS-CLOUD-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL REDIS CLOUD HOSTING CORE ECOSYSTEM",
    "provider_id": "REDIS_CLOUD", "provider_name": "REDIS CLOUD",
    "category": "HOSTING_PROVIDER", "sort_order": 184,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-MAILGUN-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL MAILGUN HOSTING CORE ECOSYSTEM",
    "provider_id": "MAILGUN", "provider_name": "MAILGUN",
    "category": "HOSTING_PROVIDER", "sort_order": 185,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-POSTMARK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL POSTMARK HOSTING CORE ECOSYSTEM",
    "provider_id": "POSTMARK", "provider_name": "POSTMARK",
    "category": "HOSTING_PROVIDER", "sort_order": 186,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-RESEND-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL RESEND HOSTING CORE ECOSYSTEM",
    "provider_id": "RESEND", "provider_name": "RESEND",
    "category": "HOSTING_PROVIDER", "sort_order": 187,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-ZOHO-MAIL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL ZOHO MAIL HOSTING CORE ECOSYSTEM",
    "provider_id": "ZOHO_MAIL", "provider_name": "ZOHO MAIL",
    "category": "HOSTING_PROVIDER", "sort_order": 188,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-FASTMAIL-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL FASTMAIL HOSTING CORE ECOSYSTEM",
    "provider_id": "FASTMAIL", "provider_name": "FASTMAIL",
    "category": "HOSTING_PROVIDER", "sort_order": 189,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-MXROUTE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL MXROUTE HOSTING CORE ECOSYSTEM",
    "provider_id": "MXROUTE", "provider_name": "MXROUTE",
    "category": "HOSTING_PROVIDER", "sort_order": 190,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-GMAIL-WORKSPACE-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL GMAIL WORKSPACE HOSTING CORE ECOSYSTEM",
    "provider_id": "GMAIL_WORKSPACE", "provider_name": "GMAIL WORKSPACE",
    "category": "HOSTING_PROVIDER", "sort_order": 191,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-MICROSOFT-365-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL MICROSOFT 365 HOSTING CORE ECOSYSTEM",
    "provider_id": "MICROSOFT_365", "provider_name": "MICROSOFT 365",
    "category": "HOSTING_PROVIDER", "sort_order": 192,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTING-CONCEPTS-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTING CONCEPTS HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTING_CONCEPTS", "provider_name": "HOSTING CONCEPTS",
    "category": "HOSTING_PROVIDER", "sort_order": 193,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTING-CO-UK-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTING CO UK HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTING.CO.UK", "provider_name": "HOSTING CO UK",
    "category": "HOSTING_PROVIDER", "sort_order": 194,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTMAYOR-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTMAYOR HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTMAYOR", "provider_name": "HOSTMAYOR",
    "category": "HOSTING_PROVIDER", "sort_order": 195,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTPRESTO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTPRESTO HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTPRESTO", "provider_name": "HOSTPRESTO",
    "category": "HOSTING_PROVIDER", "sort_order": 196,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTSEO-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTSEO HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTSEO", "provider_name": "HOSTSEO",
    "category": "HOSTING_PROVIDER", "sort_order": 197,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-HOSTUPON-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL HOSTUPON HOSTING CORE ECOSYSTEM",
    "provider_id": "HOSTUPON", "provider_name": "HOSTUPON",
    "category": "HOSTING_PROVIDER", "sort_order": 198,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-INFINITYHOST-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL INFINITYHOST HOSTING CORE ECOSYSTEM",
    "provider_id": "INFINITYHOST", "provider_name": "INFINITYHOST",
    "category": "HOSTING_PROVIDER", "sort_order": 199,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-NORDICWAY-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL NORDICWAY HOSTING CORE ECOSYSTEM",
    "provider_id": "NORDICWAY", "provider_name": "NORDICWAY",
    "category": "HOSTING_PROVIDER", "sort_order": 200,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SERVINT-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SERVINT HOSTING CORE ECOSYSTEM",
    "provider_id": "SERVINT", "provider_name": "SERVINT",
    "category": "HOSTING_PROVIDER", "sort_order": 201,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SERVERHUB-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SERVERHUB HOSTING CORE ECOSYSTEM",
    "provider_id": "SERVERHUB", "provider_name": "SERVERHUB",
    "category": "HOSTING_PROVIDER", "sort_order": 202,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SERVERMATRIX-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SERVERMATRIX HOSTING CORE ECOSYSTEM",
    "provider_id": "SERVERMATRIX", "provider_name": "SERVERMATRIX",
    "category": "HOSTING_PROVIDER", "sort_order": 203,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-SERVERWALA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL SERVERWALA HOSTING CORE ECOSYSTEM",
    "provider_id": "SERVERWALA", "provider_name": "SERVERWALA",
    "category": "HOSTING_PROVIDER", "sort_order": 204,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-VPS-HOSTING-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL VPS HOSTING HOSTING CORE ECOSYSTEM",
    "provider_id": "VPS_HOSTING", "provider_name": "VPS HOSTING",
    "category": "HOSTING_PROVIDER", "sort_order": 205,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  },
  {
    "ecosystem_id": "GLOBAL-WEBHOSTINGPAD-INDIA-HOSTING-CORE-ECOSYSTEM",
    "name": "GLOBAL WEBHOSTINGPAD INDIA HOSTING CORE ECOSYSTEM",
    "provider_id": "WEBHOSTINGPAD_INDIA", "provider_name": "WEBHOSTINGPAD INDIA",
    "category": "HOSTING_PROVIDER", "sort_order": 206,
    "status": "CORE_CATALOG_ONLY",
    "capabilities": ["HOSTING_METADATA","PROVIDER_DISCOVERY","CAPABILITY_CLASSIFICATION","READINESS_REPORTING"],
    "live_connection_verified": false, "api_transport_in_core": false
  }
]
def _enrich(record):
 item=deepcopy(record)
 if item.get("provider_id"):
  item.update(classify_provider(item["provider_id"]))
 return item
def get_catalog():return [deepcopy(ROOT)]+[_enrich(x) for x in PROVIDERS]
def list_providers():return [_enrich(x) for x in PROVIDERS]
def get_provider(key):
 key=key.strip().casefold()
 return next((_enrich(x) for x in PROVIDERS if x["ecosystem_id"].casefold()==key or x["provider_id"].casefold()==key),None)
