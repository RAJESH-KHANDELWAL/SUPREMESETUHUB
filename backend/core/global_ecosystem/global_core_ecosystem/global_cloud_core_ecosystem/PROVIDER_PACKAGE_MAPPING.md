# Cloud provider package reconciliation

**Canonical inventory source:** `backend/global_ecosystem/global_cloud_ecosystem/catalog.py`

This mapping is intentionally conservative. A provider folder is not automatically a registered provider, and a runtime catalog entry is not automatically a completed Core implementation.

## Existing Core folders mapped to canonical runtime IDs

| Runtime provider ID | Existing Core package |
|---|---|
| `aws` | `aws_cloud_core_ecosystem` |
| `google_cloud` | `google_cloud_core_ecosystem` |
| `microsoft_azure` | `microsoft_cloud_core_ecosystem` |
| `oracle_cloud` | `oracle_cloud_core_ecosystem` |
| `ibm_cloud` | `ibm_cloud_core_ecosystem` |
| `alibaba_cloud` | `alibaba_cloud_core_ecosystem` |
| `tencent_cloud` | `tencent_cloud_core_ecosystem` |
| `huawei_cloud` | `huawei_cloud_core_ecosystem` |
| `digitalocean` | `digitalocean_cloud_core_ecosystem` |
| `cloudflare` | `cloudflare_cloud_core_ecosystem` |
| `hetzner` | `hetzner_cloud_core_ecosystem` |
| `vultr` | `vultr_cloud_core_ecosystem` |
| `ovhcloud` | `ovhcloud_cloud_core_ecosystem` |
| `scaleway` | `scaleway_cloud_core_ecosystem` |
| `backblaze` | `backblaze_cloud_core_ecosystem` |
| `wasabi` | `wasabi_cloud_core_ecosystem` |

These mappings are name-based associations only. They do not establish package completeness, provider authentication, API connectivity or production readiness.

## Newly scaffolded canonical provider packages

The following 25 catalog IDs now have provider-specific Core package directories using the ten-folder Google reference layout:

`vercel`, `netlify`, `render`, `linode`, `proton_drive`, `dropbox`, `box`, `onedrive`, `google_drive`, `mega`, `icloud`, `idrive`, `pcloud`, `jio_cloud`, `digiboxx`, `tata_communications_cloud`, `nxtgen`, `esds`, `ctrls`, `yotta`, `e2e_networks`, `oracle_cloud_india`, `aws_india`, `azure_india`, `gcp_india`.

**Important:** these are structural scaffolds only. They do not imply provider implementation or live verification.

## Existing Core provider folders not represented by a canonical runtime ID

`abelohost_cloud_core_ecosystem`, `alexhost_cloud_core_ecosystem`, `alibaba_cloud_cloud_core_ecosystem`, `baidu_cloud_cloud_core_ecosystem`, `baidu_cloud_core_ecosystem`, `blueangelhost_cloud_core_ecosystem`, `china_telecom_cloud_cloud_core_ecosystem`, `china_telecom_cloud_core_ecosystem`, `flokinet_cloud_core_ecosystem`, `hetzner_cloud_cloud_core_ecosystem`, `hostkey_cloud_core_ecosystem`, `hostsailor_cloud_core_ecosystem`, `huawei_cloud_cloud_core_ecosystem`, `jd_cloud_cloud_core_ecosystem`, `jd_cloud_core_ecosystem`, `kingsoft_cloud_cloud_core_ecosystem`, `kingsoft_cloud_core_ecosystem`, `nvidia_cloud_core_ecosystem`, `rackspace_cloud_core_ecosystem`, `shinjiru_cloud_core_ecosystem`, `tencent_cloud_cloud_core_ecosystem`, `vicetemple_cloud_core_ecosystem`.

These folders are preserved as existing repository content. They must be classified as planned, legacy, alias, or candidate provider entries through a reviewed change before registration, rename or removal.

## Required reconciliation policy

1. Keep runtime provider IDs stable unless a migration explicitly approves a change.
2. Do not infer canonical provider identity from folder naming alone.
3. Use the Google ten-folder package layout for every canonical provider package.
4. Preserve unmatched folders until ownership and references are audited.
5. Add automated parity tests before treating package inventory as complete.
