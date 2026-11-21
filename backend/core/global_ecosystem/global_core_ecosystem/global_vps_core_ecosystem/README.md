# GLOBAL VPS CORE ECOSYSTEM

Read-only provider control-plane catalogue for virtual private servers. It owns provider identity, capability taxonomy, request contracts, policy boundaries, dependency metadata and readiness. It does not provision or operate VPS instances.

## Providers (20)

1. AWS — `aws_vps_core_ecosystem/`
2. Google Cloud — `google_vps_core_ecosystem/`
3. Microsoft Azure — `microsoft_vps_core_ecosystem/`
4. Oracle Cloud Infrastructure — `oracle_vps_core_ecosystem/`
5. DigitalOcean — `digitalocean_vps_core_ecosystem/`
6. Alibaba Cloud — `alibaba_cloud_vps_core_ecosystem/`
7. Tencent Cloud — `tencent_cloud_vps_core_ecosystem/`
8. Huawei Cloud — `huawei_cloud_vps_core_ecosystem/`
9. Rackspace — `rackspace_vps_core_ecosystem/`
10. Scaleway — `scaleway_vps_core_ecosystem/`
11. OVHcloud — `ovhcloud_vps_core_ecosystem/`
12. Hetzner Cloud — `hetzner_cloud_vps_core_ecosystem/`
13. Vultr — `vultr_vps_core_ecosystem/`
14. IBM Cloud — `ibm_vps_core_ecosystem/`
15. Cloudflare — `cloudflare_vps_core_ecosystem/`
16. NVIDIA — `nvidia_vps_core_ecosystem/`
17. JD Cloud — `jd_cloud_vps_core_ecosystem/`
18. Kingsoft Cloud — `kingsoft_cloud_vps_core_ecosystem/`
19. Baidu AI Cloud — `baidu_cloud_vps_core_ecosystem/`
20. China Telecom Cloud — `china_telecom_cloud_vps_core_ecosystem/`

Each existing provider directory receives one meaningful `provider.py` module that exposes its metadata and delegates validation to shared Core contracts. Shared logic is not copied into every provider folder.

## Domains (16)

1. Provider Governance (`PROVIDER_GOVERNANCE`)
2. Compute and Instance Lifecycle (`COMPUTE_AND_INSTANCE_LIFECYCLE`)
3. Regions and Availability (`REGIONS_AND_AVAILABILITY`)
4. Images and Operating Systems (`IMAGES_AND_OPERATING_SYSTEMS`)
5. Compute Sizing and Capacity (`COMPUTE_SIZING_AND_CAPACITY`)
6. Networking and Virtual Networks (`NETWORKING_AND_VIRTUAL_NETWORKS`)
7. IP Addressing and DNS (`IP_ADDRESSING_AND_DNS`)
8. Firewalls and Network Security (`FIREWALLS_AND_NETWORK_SECURITY`)
9. Identity, Access and SSH (`IDENTITY_ACCESS_AND_SSH`)
10. Block Storage and Volumes (`BLOCK_STORAGE_AND_VOLUMES`)
11. Snapshots, Backups and Recovery (`SNAPSHOTS_BACKUPS_AND_RECOVERY`)
12. Load Balancing and Traffic (`LOAD_BALANCING_AND_TRAFFIC`)
13. Monitoring, Logging and Observability (`MONITORING_LOGGING_AND_OBSERVABILITY`)
14. Billing, Pricing, Quotas and Usage (`BILLING_PRICING_QUOTAS_AND_USAGE`)
15. Compliance, Resilience and Governance (`COMPLIANCE_RESILIENCE_AND_GOVERNANCE`)
16. Automation and Deployment (`AUTOMATION_AND_DEPLOYMENT`)

## Ownership

- CORE: catalogue, identity, taxonomy, contracts, policy and readiness.
- API: provider authentication, HTTP/SDK transport and response normalization.
- ENGINE: provisioning jobs, retries, reconciliation and execution.
- DATABASE/STORAGE: durable state, secret references, audit and backups.
- APP: consent, user workflows and UI.

The 20 provider IDs are sourced from the existing Global VPS API catalogue. Provider API adapter existence and live connectivity are not inferred. Credentials stay in an external secret manager. The verified master taxonomy mapping uses existing `S09_cloud_computing` and `S10_global_server`; no new unique taxonomy entries are added and the 2,468 target is unchanged.
