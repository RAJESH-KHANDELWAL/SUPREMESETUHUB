# DigitalOcean CORE Architecture

The provider root is the single control plane for Cloud, Hosting, Server, Storage and VPS. Each capability package uses the ten-folder Google product-Core layout: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests. Each package also owns README.md, __init__.py, contracts.py, service.py, ecosystem_config.py and ecosystem_manifest.json.

CORE validates payload contracts and caller context only. Existing DigitalOcean API catalogs own provider endpoint metadata and future transport adapters. ENGINE owns runtime execution, retries, timeouts and scheduling. DATABASE/STORAGE own persistence and artifacts. CORE does not resolve secrets or make provider network calls.
