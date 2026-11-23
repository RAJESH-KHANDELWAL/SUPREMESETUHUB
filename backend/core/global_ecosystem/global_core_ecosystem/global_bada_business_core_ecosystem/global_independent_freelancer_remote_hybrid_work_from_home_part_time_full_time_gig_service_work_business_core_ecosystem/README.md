# Global Independent Freelancer, Remote, Hybrid and Flexible Work CORE Ecosystem

A vendor-neutral taxonomy and discovery foundation for independent work, freelancing, gig work, remote and hybrid employment, work-from-home opportunities, part-time and full-time roles, contract work, professional services and independent businesses.

## Coverage

- Work relationships: employee, independent contractor, freelancer, sole proprietor, agency/studio, subcontractor, platform worker, temporary, seasonal and project-based engagements.
- Work arrangements: on-site, remote, hybrid, work-from-home, field-based, flexible hours, shift-based, part-time and full-time.
- Service delivery: professional services, local services, digital services, creative work, consulting, technical delivery, logistics and microtasks.
- Career lifecycle: skills, portfolio, discovery, proposals, contracts, delivery, client service, invoicing literacy, reputation and repeat work.
- Geography: Bharat (India) and global country/region overlays; local labour, tax, licensing and worker-classification rules must be checked.

## Architecture

- domain_catalog.py: canonical domain taxonomy.
- region_catalog.py: Bharat and Global overlays.
- catalog.py: ecosystem identity and metadata.
- contracts.py: typed query/result contracts.
- policy.py: permitted discovery and restricted execution actions.
- service.py: read-only domain discovery and search.
- orchestrator.py: dependency and health metadata.
- manager.py: Python entry point (get_manager()).
- manager.php: PHP metadata facade.
- Category subfolders: focused managers mapped to canonical domain IDs.
- tests/: executable standard-library unit tests.

## Implementation boundary

This is a taxonomy/discovery foundation. It does not claim live vacancies, verified employers, guaranteed income, worker classification, payment processing, escrow, identity verification, legal/tax advice or marketplace integrations. Regulated services require applicable licenses and local compliance. The separate backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json is referenced read-only; it is not modified and entries are not fabricated to reach the 2,468 target.
