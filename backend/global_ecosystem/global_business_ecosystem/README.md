# GLOBAL BUSINESS ECOSYSTEM

Canonical path: `backend/global_ecosystem/global_business_ecosystem/`

The Global Business Ecosystem is the Bharat-to-global umbrella for business domains, business models, companies, organizations, business education, trade, commerce and enterprise operations. It spans Basic / Normal through Standard, Professional, Advanced, Expert, Enterprise / Industrial, Research, Frontier and Supreme / Long-horizon maturity scopes.

## Connected canonical business vertical

`global_bada_business_ecosystem/` is connected as a child business vertical through the Python adapter:

`adapters/bada_business.py`

The adapter imports the existing canonical package and reads its catalog, programs, courses, events and network-marketing/direct-selling child registry. It does not copy Bada Business provider records into this umbrella.

## Registered business namespaces

- `global_bada_business_ecosystem` — provider resources, programs, courses, events, referrals and direct-selling/affiliate child domains. Code-connected resource catalog.
- `global_company_companies_ecosystem` — company and corporate namespace.
- `global_organizations_ecosystem` — organizations and institutions namespace.
- `global_finance_ecosystem` — finance and fintech namespace.
- `global_payment_ecosystem` — payment and commerce namespace.

Other business categories are represented as taxonomy categories until their dedicated package implementation is ready. A catalog entry does not claim a production integration.

## Functional coverage

Business strategy, entrepreneurship, startups, companies, organizations, education and training, network marketing, direct selling, affiliate marketing, sales, customer relationships, marketing, branding, finance, accounting, tax, payments, marketplaces, e-commerce, human resources, legal compliance, governance, supply chains, operations, franchising, licensing, consulting, social enterprise, international trade, cross-border business and digital platform business.

## Architecture boundaries

- GLOBAL_ECOSYSTEM owns business taxonomy, namespace registry and descriptive catalog relationships.
- API owns HTTP interfaces and transport contracts.
- CORE owns stable business contracts and business rules.
- ENGINE owns orchestration and runtime execution.
- DATABASE owns persistence schemas, migrations and data access.
- SECURITY / IDENTITY owns authentication, authorization, secret storage and audit.
- Provider-specific source records remain in their canonical provider/domain packages.

## Tests

Run from repository root:

```bash
python -m unittest backend.global_ecosystem.global_business_ecosystem.tests.test_business_ecosystem -v
```

The Bada Business adapter is a code-level package connection. It does not establish official API access, provider partnership, current offer availability, payment processing, registration submission or production readiness.
