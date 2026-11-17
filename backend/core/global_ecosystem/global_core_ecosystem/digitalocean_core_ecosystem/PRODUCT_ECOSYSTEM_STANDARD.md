# DigitalOcean Capability CORE Package Standard

Each capability package must contain exactly ten folders: authentication/, capabilities/, docs/, events/, lifecycle/, models/, schemas/, security/, services/ and tests/. It must also contain README.md, __init__.py, contracts.py, service.py, ecosystem_config.py and ecosystem_manifest.json. PHP caller-context contract is authentication/contract.php; duplicate package php/ folders are prohibited.

Folder ownership: authentication defines tenant/actor context; capabilities and models describe catalog metadata; docs documents the contract; events defines event envelopes; lifecycle defines states; schemas/contracts validate requests; security blocks secret material; services exposes capability validation; tests cover contracts. API/ENGINE/DATABASE/STORAGE work remains in those layers.
