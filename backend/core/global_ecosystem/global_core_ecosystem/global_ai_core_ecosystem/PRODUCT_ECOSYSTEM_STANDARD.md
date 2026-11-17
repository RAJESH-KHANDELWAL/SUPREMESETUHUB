# Global AI Product CORE Ecosystem Standard

Every runtime provider/model/framework registry entry receives a `<provider_id>_core_ecosystem` package with exactly ten folders: authentication/contract.php; capabilities/catalog.py; docs/README.md; events/contracts.py; lifecycle/state.py; models/product_model.py; schemas/product_schema.py; security/policy.py; services/core_service.py; tests/__init__.py and tests/test_manifest.py.

Package root: README.md, __init__.py, ecosystem_config.py, ecosystem_manifest.json and service.py. Shared product behavior lives in module_service.py. Runtime registry metadata is not copied. API owns authentication and transport; ENGINE owns inference and tool execution. Legacy aliases are not canonical packages.
