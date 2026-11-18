"""Integration guardrails for cloud infrastructure providers."""
CLOUD_INTEGRATION_GUARDRAILS=(
"Use official documented APIs and provider-approved SDKs only.",
"Never embed credentials in source code or commit secrets.",
"Never infer account ownership, permissions, regional availability, price or compliance.",
"Require explicit account configuration and least-privilege credentials.",
"Destructive storage, compute, IAM and network operations require explicit authorization.",
"Catalog presence and adapter scaffolds never imply a live provider connection.",
"Keep API, CORE, ENGINE and DATABASE implementations in their separately owned layers.",
)
__all__=["CLOUD_INTEGRATION_GUARDRAILS"]
