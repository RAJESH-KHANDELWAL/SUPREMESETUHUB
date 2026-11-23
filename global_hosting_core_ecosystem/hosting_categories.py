"""Hosting taxonomy and conservative provider classification.
Categories describe service capabilities; they are not interchangeable provider brands.
Unknown legacy records remain explicitly unclassified until verified.
"""
HOSTING_CATEGORIES = {
 "SHARED_WORDPRESS": {"name":"Shared and WordPress Hosting","description":"Shared Linux hosting and WordPress-focused plans"},
 "MANAGED_WORDPRESS": {"name":"Managed WordPress Hosting","description":"Managed WordPress operations, updates, security and performance"},
 "CLOUD_VPS_DEDICATED": {"name":"Cloud, VPS and Dedicated Compute","description":"Virtual machines, cloud compute and dedicated servers"},
 "MANAGED_HOSTING": {"name":"Managed Hosting","description":"Managed infrastructure and application operations"},
 "APP_PLATFORM": {"name":"Application and Developer Platforms","description":"Application deployment and platform-as-a-service"},
 "EDGE_CDN": {"name":"CDN and Edge Delivery","description":"Content delivery, edge compute and acceleration"},
 "OBJECT_STORAGE": {"name":"Object and File Storage","description":"S3-compatible object and file storage"},
 "MEDIA_STORAGE": {"name":"Media and Asset Hosting","description":"Image, video and media asset delivery"},
 "MANAGED_DATABASE": {"name":"Managed Database Hosting","description":"Managed relational, document, cache and serverless databases"},
 "EMAIL_HOSTING": {"name":"Email Hosting and Delivery","description":"Mailbox hosting and transactional email delivery"},
 "DOMAIN_DNS": {"name":"Domain and DNS Services","description":"Domain registration and DNS services"},
 "COLOCATION_DATACENTRE": {"name":"Colocation and Data Centres","description":"Colocation, interconnection and data-centre services"},
 "CONTROL_PANEL": {"name":"Hosting Control Panels","description":"Hosting administration software; not a hosting provider"},
 "DEVELOPER_STATIC": {"name":"Static and Developer Hosting","description":"Static-site and source-connected hosting"},
 "SPECIALIST_PLATFORM": {"name":"Specialist Hosting Platforms","description":"Specialist platforms and hosting-adjacent infrastructure"},
 "UNCLASSIFIED": {"name":"Needs Verification","description":"Legacy inventory entry awaiting provider identity and service verification"}
}
_CLASS = {
 "SHARED_WORDPRESS": ["ABELOHOST","ALEXHOST","AWARDSPACE","BIGROCK","BLUEANGELHOST","BLUEHOST","CHEMICLOUD","COMBELL","CONTABO","CRAZYDOMAINS","DREAMHOST","FASTCOMET","GANDI","GODADDY","GREENGEEKS","HOSTARMADA","HOSTGATOR","HOSTGATORINDIA","HOSTING_COM","HOSTINGER","HOSTINGRAJA","HOSTITSMART","HOSTPAPA","HOSTSAILOR","HOSTWINDS","INFINITYFREE","INFOMANIAK","INMOTION","INTERSERVER","IONOS","KNOWNHOST","MILESWEB","NAMECHEAP","ONE_COM","SITEGROUND","STRATO","TRANSIP","VENTRAIP","VERPEX","VICETEMPLE","WEBDOCK","WPX","YOTTA","A2_HOSTING","ACCUPWEB","ASPHOSTPORTAL","CHEAPO","HOSTINGUK","HOSTMANTIS","HOSTROCKET","HOSTROUND","KRYSTAL","MDDHOSTING","ROCKHOSTER","STABLEPOINT","ULTAHOST","WEBHOSTINGPAD","WEBHOSTUK","XSERVER","ZUME","GREENHOST","HOSTNET","HOSTING.COM","HOSTING_CONCEPTS","HOSTING.CO.UK","HOSTMAYOR","HOSTPRESTO","HOSTSEO","HOSTUPON","INFINITYHOST","NORDICWAY","WEBHOSTINGPAD_INDIA"],
 "MANAGED_WORDPRESS": ["KINSTA","PAGELY","PRESSABLE","WPENGINE","FLYWHEEL","NEXCESS","DREAMHOST_PRO","GODADDY_PRO","WP_SERVERS","HOSTINGER_PRO","PANTHEON_PLATFORM"],
 "CLOUD_VPS_DEDICATED": ["AWS","ALIBABA_CLOUD","DIGITALOCEAN","E2ENETWORKS","GREENCLOUDVPS","HETZNER","HIVELOCITY","HOSTKEY","HUAWEI_CLOUD","IBM_CLOUD","LEASEWEB","LINODE","M247","MICROSOFT","NETMAGIC","ORACLE_CLOUD","OVHCLOUD","PHOENIXNAP","RACKSPACE","RAMNODE","SCALEWAY","UPCLOUD","VULTR","BUYVM","CTRLS","AKILE","ALWAYSdata","INTERNETVIKINGS","SCALAHOSTING","SERVERS.COM","TEMOK","THE_ONLINE","KAMATERA","LEASEWEB_CLOUD","LINODE_AKAMAI","ORACLE_CLOUD_INFRASTRUCTURE","OVH_CLOUD","VPSDIME","SERVINT","SERVERHUB","SERVERMATRIX","SERVERWALA","VPS_HOSTING"],
 "MANAGED_HOSTING": ["CLOUDWAYS","HOSTINGRAJA","RUNCLOUD","UPTIME"],
 "APP_PLATFORM": ["APPWRITE","FIREBASE","HEROKU","KOYEB","NORTHFLANK","RAILWAY","RENDER","REPLIT","SUPABASE","VERCEL","CLOUDFOUNDRY","DENO_DEPLOY","FLY_DEPLOY","GOOGLE_APP_ENGINE"],
 "EDGE_CDN": ["AKAMAI","BUNNY","CLOUDFLARE","FASTLY","GCORE","CLOUDFRONT","KEYCDN","EDGIO","STACKPATH","VERCEL_EDGE"],
 "OBJECT_STORAGE": ["BACKBLAZE","WASABI","CLOUDFLARE_R2","IDRIVE_E2","LINODE_OBJECT_STORAGE","DIGITALOCEAN_SPACES","STORJ"],
 "MEDIA_STORAGE": ["CLOUDINARY"],
 "MANAGED_DATABASE": ["NEON","PLANETSCALE","TURSO","UPSTASH","AIVEN","MONGODB_ATLAS","REDIS_CLOUD"],
 "EMAIL_HOSTING": ["MAILGUN","POSTMARK","RESEND","ZOHO_MAIL","FASTMAIL","MXROUTE","GMAIL_WORKSPACE","MICROSOFT_365"],
 "DOMAIN_DNS": ["GANDI","NAMECHEAP","NAMESILO","PORKBUN","GODADDY"],
 "COLOCATION_DATACENTRE": ["EQUINIX","PHOENIXNAP","NETMAGIC"],
 "CONTROL_PANEL": ["CPANEL","PLESK"],
 "DEVELOPER_STATIC": ["GITHUB_PAGES","GITLAB_PAGES","NEOCITIES","SURGE","NETLIFY"],
 "SPECIALIST_PLATFORM": ["FLOKINET","FLYIO","HOSTKEY","RESELLERCLUB","RUNCLOUD","SERVERION","SHINJIRU","TENCENT_CLOUD","WORDPRESS_COM","EQUINIX"]
}
_NON_PROVIDER = {"APP_PLATFORM":"SERVICE_CATEGORY","CLOUD":"SERVICE_CATEGORY","DEDICATED_VPS":"SERVICE_CATEGORY","EDGE_STORAGE_CDN":"SERVICE_CATEGORY","WEB":"SERVICE_CATEGORY","INDIA":"REGION_LABEL","PRIVACY_SPECIALTY":"UNVERIFIED_LABEL"}
def classify_provider(provider_id):
 category=next((k for k,ids in _CLASS.items() if provider_id in ids), "UNCLASSIFIED")
 entity_type=_NON_PROVIDER.get(provider_id, "PLATFORM_OR_TECHNOLOGY" if category=="CONTROL_PANEL" else "SERVICE_PROVIDER")
 return {"hosting_category":category,"hosting_category_name":HOSTING_CATEGORIES[category]["name"],"entity_type":entity_type,"is_provider_record":entity_type=="SERVICE_PROVIDER","classification_verified":category!="UNCLASSIFIED" and entity_type=="SERVICE_PROVIDER"}
