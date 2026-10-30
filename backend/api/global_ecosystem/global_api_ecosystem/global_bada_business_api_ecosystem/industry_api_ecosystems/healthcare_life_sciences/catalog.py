"""Healthcare & Life Sciences category taxonomy."""
from __future__ import annotations

HEALTHCARE_LIFE_SCIENCES_CATEGORIES = [
    {
        "id": "hospitals_and_health_systems",
        "name": "Hospitals & Health Systems",
        "subcategories": [
            "multi_speciality_hospitals",
            "speciality_hospitals",
            "day_care_centres",
            "hospital_networks"
        ]
    },
    {
        "id": "clinics_and_primary_care",
        "name": "Clinics & Primary Care",
        "subcategories": [
            "general_practice",
            "family_medicine",
            "specialist_clinics",
            "community_health_centres"
        ]
    },
    {
        "id": "diagnostics_and_laboratories",
        "name": "Diagnostics & Laboratories",
        "subcategories": [
            "pathology_labs",
            "medical_imaging",
            "genetic_testing",
            "point_of_care_testing"
        ]
    },
    {
        "id": "pharmacies_and_medicines",
        "name": "Pharmacies & Medicines",
        "subcategories": [
            "retail_pharmacies",
            "hospital_pharmacies",
            "pharmaceutical_distribution",
            "medicine_information"
        ]
    },
    {
        "id": "medical_devices_and_equipment",
        "name": "Medical Devices & Equipment",
        "subcategories": [
            "diagnostic_equipment",
            "patient_monitoring",
            "surgical_instruments",
            "medical_device_services"
        ]
    },
    {
        "id": "digital_health_and_telemedicine",
        "name": "Digital Health & Telemedicine",
        "subcategories": [
            "teleconsultation",
            "electronic_health_records",
            "remote_patient_monitoring",
            "health_apps"
        ]
    },
    {
        "id": "mental_and_behavioural_health",
        "name": "Mental & Behavioural Health",
        "subcategories": [
            "psychology_services",
            "psychiatry_services",
            "counselling_centres",
            "behavioural_health_programmes"
        ]
    },
    {
        "id": "dental_and_oral_health",
        "name": "Dental & Oral Health",
        "subcategories": [
            "general_dentistry",
            "orthodontics",
            "oral_surgery",
            "dental_laboratories"
        ]
    },
    {
        "id": "rehabilitation_and_physiotherapy",
        "name": "Rehabilitation & Physiotherapy",
        "subcategories": [
            "physical_rehabilitation",
            "physiotherapy",
            "occupational_therapy",
            "speech_therapy"
        ]
    },
    {
        "id": "public_and_preventive_health",
        "name": "Public & Preventive Health",
        "subcategories": [
            "vaccination_services",
            "health_screening",
            "epidemiology_services",
            "health_education"
        ]
    },
    {
        "id": "biotechnology_and_research",
        "name": "Biotechnology & Life Sciences Research",
        "subcategories": [
            "biotechnology_research",
            "clinical_research",
            "molecular_biology",
            "biomanufacturing"
        ]
    },
    {
        "id": "clinical_trials_and_cro",
        "name": "Clinical Trials & Contract Research",
        "subcategories": [
            "clinical_trial_sites",
            "contract_research",
            "trial_management",
            "regulatory_documentation"
        ]
    },
    {
        "id": "health_insurance_and_tpa",
        "name": "Health Insurance & TPA Services",
        "subcategories": [
            "health_claims_administration",
            "cashless_networks",
            "medical_underwriting",
            "benefits_administration"
        ]
    },
    {
        "id": "elderly_and_home_care",
        "name": "Elderly, Home & Community Care",
        "subcategories": [
            "home_nursing",
            "elder_care",
            "palliative_support",
            "assisted_living"
        ]
    },
    {
        "id": "veterinary_and_animal_health",
        "name": "Veterinary & Animal Health",
        "subcategories": [
            "veterinary_clinics",
            "animal_diagnostics",
            "animal_pharmaceuticals",
            "livestock_health"
        ]
    }
]

def list_categories() -> list[dict[str, object]]:
    """Return defensive copies of all categories."""
    return [dict(item, subcategories=list(item["subcategories"])) for item in HEALTHCARE_LIFE_SCIENCES_CATEGORIES]

def get_category(category_id: str) -> dict[str, object] | None:
    """Return one category by stable identifier."""
    for item in HEALTHCARE_LIFE_SCIENCES_CATEGORIES:
        if item["id"] == category_id:
            return dict(item, subcategories=list(item["subcategories"]))
    return None
