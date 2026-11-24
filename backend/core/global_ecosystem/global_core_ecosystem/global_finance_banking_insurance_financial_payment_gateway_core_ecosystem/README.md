# Global Finance, Banking, Insurance & Financial Payment Gateway Core Ecosystem

Canonical Core catalogue for finance and payment-gateway capabilities across Bharat and international markets.

## Coverage
Banking; insurance and reinsurance; capital markets and investments; consumer and business lending; microfinance; leasing and factoring; accounting, tax, audit and treasury; risk, regulation and compliance; financial data and credit intelligence; fintech and open finance; payment gateways, processors and merchant acquiring; cards, UPI, bank rails, wallets, QR/POS; checkout, billing, refunds, settlement and payouts; FX, remittance, trade, public and social finance.

## Core modules
- `catalog.py`: ecosystem registry
- `domain_catalog.py`: domain definitions and unique package classification
- `product_catalog.py`: child/provider inventory
- `domain_runtime.py`: domain-scoped discovery
- `module_service.py`: package-scoped metadata service
- `orchestrator.py`: read-only orchestration
- `manager.py`: stable public manager
- `service.py`: status and overview
- `contracts.py`: tenant, readiness, secret-reference and result contracts
- `policy.py`: security, compliance and transaction boundaries
- `test_core_domains.py`: catalogue integrity tests

Child directories are registered modules, not live integrations. No redundant PHP files, empty service layers or speculative API clients are created. Add implementation files only when a real domain responsibility is ready.

## Safety
This Core layer does not move money, issue credit, underwrite insurance, execute trades or provide regulated financial advice. Those capabilities require separately authorized API/service layers, jurisdiction-specific review, auditability and external secret management.
