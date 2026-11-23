# Global Finance, Banking, Insurance & Financial Payment Gateway — Service, Work & Business CORE

This is the commercial/service-work-business layer corresponding to the canonical Global CORE package:

`backend/core/global_ecosystem/global_core_ecosystem/global_finance_banking_insurance_financial_payment_gateway_core_ecosystem`

The canonical Global CORE folder remains in its original location and is not moved, renamed, or modified by this module.

## Responsibilities

- Classify finance, banking, insurance, fintech and payment-gateway services, professional work and business models.
- Reuse canonical domain IDs and package names from the Global Finance CORE catalogue.
- Expose a read-only catalogue and mapping validation.
- Keep service classification separate from regulated financial execution, payment processing, underwriting, lending, investment advice and money movement.

## Safety boundary

This module is a taxonomy and discovery layer only. It does not connect to banks or payment providers, execute transactions, hold funds, issue insurance, approve credit, or provide regulated financial advice. Provider integrations and jurisdiction-specific authorization must be implemented and verified separately.

## Main modules

- `domain_catalog.py`: commercial service/work/business mappings to canonical Global CORE domains.
- `catalog.py`: ecosystem identity and canonical dependency.
- `service.py`: classification and validation.
- `orchestrator.py`: read-only discovery and health.
- `manager.py`: stable public manager API.
- `test/`: focused mapping and classification tests.
