# Healthcare, Medical, Life Sciences & Total Wellness API Ecosystem

Standalone ecosystem **#03** under `global_api_ecosystem/`, outside the Bada Business tree.

## Scope
Bharat + global human healthcare, whole-body anatomy and physiology, clinical specialties, hospitals, clinics, doctors, nursing, diagnostics, medicines, surgery, donors, reproductive and sexual medicine, health and wellness, public health, digital health, biotechnology, and veterinary/animal healthcare.

## Domain structure
See `subcategories.py` for the canonical 34-domain registry. Each domain has its own folder with a README and catalog metadata.

## Whole-body coverage
The anatomy domain covers cells, tissues, organs, organ systems, body regions and specialist anatomy. Clinical domains cover normal health, prevention, screening, diagnosis, treatment, surgery, rehabilitation and long-term care. Human and animal care are separately classified.

## Sexual health and adult-content boundary
Clinical sexual and reproductive healthcare, fertility, consent-based donor services, sexual medicine and medically relevant intimacy care are included. The separate Kamasutra/adult-wellness ecosystem remains the canonical home for adult lifestyle, relationship and lawful adult-media business taxonomy. Pornography or nudity is not classified as medical treatment or healthcare service.

## Safety and governance
- Clinical diagnosis, prescribing, procedures and treatment must be performed by appropriately licensed professionals.
- Donor, fertility, transplant and clinical-trial workflows require informed consent, privacy safeguards, eligibility screening and jurisdiction-specific compliance.
- Health data requires strict privacy, security, access control, auditability and data minimisation.
- Animal services must respect veterinary licensing and species-specific welfare.
- No provider, doctor, hospital, licence, medicine, donor or certification is verified merely by appearing in this taxonomy.

## API scaffold
Router prefix: `/healthcare-medical-life-sciences`
Endpoints: `GET /status`, `GET /domains`, `GET /domains/{domain_id}`

## Status
Initial taxonomy and API scaffolding. Parent application router registration, test execution, persistence, clinical governance review, provider verification and live integrations remain follow-up work. Not a medical device or clinical decision system.
