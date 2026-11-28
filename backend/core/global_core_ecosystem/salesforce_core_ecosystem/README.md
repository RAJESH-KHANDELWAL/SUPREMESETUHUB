# Salesforce Core Ecosystem

Salesforce provider-level Core metadata: identity, product registration, capability-domain classification, policy boundaries, lifecycle/readiness metadata and product-manager discovery.

## 14 product modules
- **Analytics and Reporting** (`salesforce_analytics_core_ecosystem`): Salesforce Analytics APIs and reporting metadata.
- **Apex Development** (`salesforce_apex_core_ecosystem`): Apex developer tooling and code metadata boundaries.
- **Bulk Data Operations** (`salesforce_bulk_core_ecosystem`): Bulk import/export job metadata and async capability discovery.
- **Composite Requests** (`salesforce_composite_core_ecosystem`): Composite REST request composition metadata.
- **Data Cloud** (`salesforce_data_cloud_core_ecosystem`): Data platform ingestion, model and activation metadata.
- **Files and Content** (`salesforce_files_content_core_ecosystem`): Salesforce files, content and document capability metadata.
- **Identity and OAuth** (`salesforce_identity_oauth_core_ecosystem`): Identity and OAuth configuration capability metadata.
- **Marketing Cloud** (`salesforce_marketing_cloud_core_ecosystem`): Campaign, journey and messaging metadata.
- **Metadata and Tooling** (`salesforce_metadata_tooling_core_ecosystem`): Metadata, describe and developer tooling capability metadata.
- **Platform Events and Pub/Sub** (`salesforce_platform_events_pubsub_core_ecosystem`): Event integration and Pub/Sub capability metadata.
- **REST API** (`salesforce_rest_core_ecosystem`): REST resource and capability discovery.
- **Service Cloud** (`salesforce_service_cloud_core_ecosystem`): Customer service, case and support capability metadata.
- **SOAP API** (`salesforce_soap_core_ecosystem`): SOAP operation and compatibility capability metadata.
- **Streaming** (`salesforce_streaming_core_ecosystem`): Streaming, CDC and subscription capability metadata.

## Shared entry points
- `manager.py`: central Python manager for product/domain listing, status, health and routing.
- `manager.php`: thin PHP metadata facade.
- `catalog.py`, `product_catalog.py`, `domain_catalog.py`: product/domain inventories.
- `contracts.py`, `constants.py`, `policy.py`: stable contracts and boundaries.
- `service.py`, `orchestrator.py`, `module_service.py`: shared provider/product discovery.
- `master_catalog.py`: read-only export view.
- `ecosystem_manifest.json`: machine-readable registry.

## Boundary
Core is catalog/control-plane metadata only. It does not make Salesforce API calls, perform OAuth/token exchange, store secrets or verify live tenant connections. Adapters, auth, execution, persistence and user workflows belong to their respective layers. No real Salesforce connection is asserted.
