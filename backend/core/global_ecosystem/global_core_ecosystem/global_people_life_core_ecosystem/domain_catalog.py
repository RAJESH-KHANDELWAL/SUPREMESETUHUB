"""Canonical People Life domain taxonomy and module routing.

Local domains own metadata managers in this ecosystem. Adult-only specialist
domains are references to the canonical Kamasutra ecosystem to avoid duplicate
implementations. This file is metadata-only; it does not execute user workflows.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
from typing import Any

from .policy import redact_sensitive_metadata

_DATA = json.loads(Path(__file__).with_name("catalog.json").read_text(encoding="utf-8"))
PEOPLE_LIFE_MODULES = tuple({**item, "division": "PEOPLE_LIFE", "status": "CORE_CATALOG_ONLY"} for item in _DATA["domains"])
DOMAIN_RECORDS = json.loads(r'''[
    {
        "domain_id": "LIFE_STAGES_AND_HUMAN_DEVELOPMENT",
        "name": "Life Stages and Human Development",
        "purpose": "Human development from prenatal and birth stages through infancy, childhood, adolescence, adulthood, midlife and major life transitions, including age-appropriate development and support.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_life_stages_human_development_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_life_stages_human_development_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "advanced",
            "global_people_work_life",
            "india_people_work_life",
            "student_youth_development"
        ]
    },
    {
        "domain_id": "IDENTITY_CITIZENSHIP_AND_PERSONAL_ADMIN",
        "name": "Identity, Citizenship and Personal Administration",
        "purpose": "Personal identity, civil records, documentation, accessibility of identity services, personal administration and life-event records. Sensitive identifiers remain outside Core metadata.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_identity_citizenship_personal_admin_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_identity_citizenship_personal_admin_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_people_work_life",
            "india_digital_public_services"
        ]
    },
    {
        "domain_id": "EDUCATION_LEARNING_AND_SKILLS",
        "name": "Education, Learning and Skills",
        "purpose": "Early learning, school, higher education, vocational learning, lifelong learning, skills, literacy, language learning, training and credentials.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_education_learning_skills_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_education_learning_skills_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "advanced",
            "student_youth_development",
            "workforce_professional_services"
        ]
    },
    {
        "domain_id": "CAREER_EMPLOYMENT_AND_WORKFORCE",
        "name": "Career, Employment and Workforce",
        "purpose": "Career discovery, jobs, employment, recruitment metadata, workforce development, professional transitions, remote work, freelancing and workplace life.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_career_employment_workforce_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_career_employment_workforce_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "india_people_work_life",
            "workforce_professional_services"
        ]
    },
    {
        "domain_id": "ENTREPRENEURSHIP_LIVELIHOOD_AND_SMALL_BUSINESS",
        "name": "Entrepreneurship, Livelihood and Small Business",
        "purpose": "Self-employment, entrepreneurship, livelihood, micro and small business support, independent work and business capability discovery; detailed commercial execution belongs to Business ecosystems.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_entrepreneurship_livelihood_small_business_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_entrepreneurship_livelihood_small_business_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "small_business_msme_support",
            "workforce_professional_services"
        ]
    },
    {
        "domain_id": "PERSONAL_FINANCE_AND_LIFE_PLANNING",
        "name": "Personal Finance and Life Planning",
        "purpose": "Personal budgeting, household financial planning, savings literacy, insurance and financial-service discovery, benefits and life planning; regulated financial execution remains in Finance ecosystems.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_personal_finance_life_planning_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_personal_finance_life_planning_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_people_work_life",
            "small_business_msme_support"
        ]
    },
    {
        "domain_id": "FAMILY_PARENTING_AND_CAREGIVING",
        "name": "Family, Parenting and Caregiving",
        "purpose": "Family relationships, parenting, child development, caregiving, eldercare, household coordination and family-life transitions.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_family_parenting_caregiving_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_family_parenting_caregiving_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "family_parenting_care"
        ]
    },
    {
        "domain_id": "PERSONAL_SAFETY_CRISIS_AND_SURVIVOR_SUPPORT",
        "name": "Personal Safety, Crisis and Survivor Support",
        "purpose": "Personal and family safety information, safeguarding, abuse prevention, crisis navigation, survivor support and referral metadata; not an emergency-response service.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_personal_safety_crisis_survivor_support_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_personal_safety_crisis_survivor_support_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "family_safety_survivor_support"
        ]
    },
    {
        "domain_id": "DATING_RELATIONSHIPS_MARRIAGE_AND_COMPATIBILITY",
        "name": "Dating, Relationships, Marriage and Compatibility",
        "purpose": "Dating, friendship, partnership, marriage, compatibility, communication, conflict navigation, separation and relationship-life education for age-appropriate audiences.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_dating_relationships_marriage_compatibility_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_dating_relationships_marriage_compatibility_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "dating_matchmaking_relationships",
            "family_parenting_care"
        ]
    },
    {
        "domain_id": "HOME_HOUSEHOLD_AND_DAILY_LIVING",
        "name": "Home, Household and Daily Living",
        "purpose": "Housing and household administration, daily living, food and nutrition literacy, consumer life, routines, personal organization and independent living.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_home_household_daily_living_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_home_household_daily_living_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_people_work_life",
            "india_people_work_life"
        ]
    },
    {
        "domain_id": "PHYSICAL_HEALTH_WELLBEING_AND_ACCESSIBILITY",
        "name": "Physical Health, Wellbeing and Accessibility",
        "purpose": "General health literacy, preventive wellbeing, fitness, nutrition, disability inclusion and accessibility discovery; not diagnosis, treatment or clinical advice.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_physical_health_wellbeing_accessibility_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_physical_health_wellbeing_accessibility_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_people_work_life",
            "sexual_health_reproductive_education"
        ]
    },
    {
        "domain_id": "MENTAL_EMOTIONAL_AND_SOCIAL_WELLBEING",
        "name": "Mental, Emotional and Social Wellbeing",
        "purpose": "Emotional literacy, resilience, social connection, stress-awareness, wellbeing resources and qualified-care referral discovery; not psychotherapy or crisis intervention.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_mental_emotional_social_wellbeing_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_mental_emotional_social_wellbeing_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "family_safety_survivor_support",
            "global_people_work_life"
        ]
    },
    {
        "domain_id": "SEXUAL_REPRODUCTIVE_HEALTH_AND_EDUCATION",
        "name": "Sexual and Reproductive Health Education",
        "purpose": "Age-appropriate sexual and reproductive health education, consent literacy, puberty education and health-resource discovery with safeguarding and privacy boundaries.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_sexual_reproductive_health_education_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_sexual_reproductive_health_education_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "sexual_health_reproductive_education"
        ]
    },
    {
        "domain_id": "DIGITAL_LIFE_AND_GLOBAL_DIGITAL_SERVICES",
        "name": "Digital Life and Global Digital Services",
        "purpose": "Digital identity awareness, online participation, personal technology, digital literacy, online safety and cross-border digital-service discovery.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_digital_life_global_digital_services_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_digital_life_global_digital_services_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_digital_services"
        ]
    },
    {
        "domain_id": "CIVIC_LEGAL_AND_PUBLIC_SERVICES",
        "name": "Civic, Legal and Public Services",
        "purpose": "Citizen services, public-benefit discovery, legal-information navigation, civic participation and government-service metadata; not legal representation or official eligibility decisions.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_civic_legal_public_services_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_civic_legal_public_services_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "india_digital_public_services"
        ]
    },
    {
        "domain_id": "COMMUNITY_CULTURE_SPIRITUALITY_AND_BELONGING",
        "name": "Community, Culture, Spirituality and Belonging",
        "purpose": "Community participation, culture, language, traditions, spirituality, social belonging, volunteering and intergenerational connection.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_community_culture_spirituality_belonging_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_community_culture_spirituality_belonging_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_people_work_life"
        ]
    },
    {
        "domain_id": "TRAVEL_MOBILITY_LEISURE_AND_RECREATION",
        "name": "Travel, Mobility, Leisure and Recreation",
        "purpose": "Mobility, relocation, travel-life planning, recreation, hobbies, sports, arts, entertainment and personal interests.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_travel_mobility_leisure_recreation_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_travel_mobility_leisure_recreation_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_people_work_life"
        ]
    },
    {
        "domain_id": "AGEING_RETIREMENT_AND_LIFE_TRANSITIONS",
        "name": "Ageing, Retirement and Life Transitions",
        "purpose": "Healthy ageing information, later-life independence, retirement transitions, elder support, legacy planning and end-of-life resource discovery.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_ageing_retirement_life_transitions_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_ageing_retirement_life_transitions_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_people_work_life"
        ]
    },
    {
        "domain_id": "GLOBAL_INDIA_AND_CROSS_BORDER_PEOPLE_LIFE",
        "name": "Global, India and Cross-Border People Life",
        "purpose": "Global and India-specific people-life contexts, migration and relocation information, cross-border family/work transitions and localized service discovery.",
        "age_restricted": false,
        "implementation_mode": "LOCAL_DOMAIN_PACKAGE",
        "package_name": "people_global_india_cross_border_life_core_ecosystem",
        "package_path": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/people_global_india_cross_border_life_core_ecosystem",
        "canonical_ecosystem_ref": null,
        "canonical_domain_refs": [],
        "module_folders": [
            "global_people_work_life",
            "india_people_work_life"
        ]
    },
    {
        "domain_id": "ADULT_INTIMACY_KAMASUTRA_AND_SEXUAL_WELLNESS_18_PLUS",
        "name": "Adult Intimacy, Kamasutra and Sexual Wellness 18+",
        "purpose": "Lawful, consenting-adult intimacy education, Kamasutra knowledge, couple intimacy and adult sexual-wellness metadata. Detailed canonical implementation is delegated to the Kamasutra ecosystem.",
        "age_restricted": true,
        "implementation_mode": "CROSS_ECOSYSTEM_REFERENCE",
        "package_name": null,
        "package_path": null,
        "canonical_ecosystem_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/",
        "canonical_domain_refs": [
            {
                "domain_id": "SEXUAL_EDUCATION_AND_TRADITIONAL_KNOWLEDGE",
                "package_name": "global_sexual_education_traditional_knowledge_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_sexual_education_traditional_knowledge_core_ecosystem"
            },
            {
                "domain_id": "RELATIONSHIPS_AND_COMPATIBILITY",
                "package_name": "global_relationships_compatibility_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_relationships_compatibility_core_ecosystem"
            },
            {
                "domain_id": "COACHING_AND_COUNSELLING",
                "package_name": "global_relationship_intimacy_coaching_counselling_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_relationship_intimacy_coaching_counselling_core_ecosystem"
            }
        ],
        "module_folders": [
            "adult_couple_intimacy_education_18_plus"
        ]
    },
    {
        "domain_id": "ADULT_MEDIA_PORNOGRAPHY_AND_CONTENT_GOVERNANCE_18_PLUS",
        "name": "Adult Media, Pornography and Content Governance 18+",
        "purpose": "Metadata for lawful adult-only media, pornography categories, platform distribution, live streaming, licensing, subscriptions, moderation and takedown boundaries.",
        "age_restricted": true,
        "implementation_mode": "CROSS_ECOSYSTEM_REFERENCE",
        "package_name": null,
        "package_path": null,
        "canonical_ecosystem_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/",
        "canonical_domain_refs": [
            {
                "domain_id": "ADULT_MEDIA_AND_CREATOR_ECONOMY",
                "package_name": "global_adult_media_creator_economy_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_media_creator_economy_core_ecosystem"
            },
            {
                "domain_id": "ADVERTISING_AND_DISTRIBUTION",
                "package_name": "global_adult_advertising_distribution_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_advertising_distribution_core_ecosystem"
            }
        ],
        "module_folders": [
            "adult_content_distribution_licensing_18_plus",
            "adult_live_streaming_18_plus",
            "adult_media_pornography_18_plus"
        ]
    },
    {
        "domain_id": "ADULT_CREATOR_ECONOMY_PRODUCTION_AND_WORK_18_PLUS",
        "name": "Adult Creator Economy, Production and Work 18+",
        "purpose": "Lawful adult creator work, studio production, professional operations, platform work and creator-economy metadata, subject to performer autonomy and labor safeguards.",
        "age_restricted": true,
        "implementation_mode": "CROSS_ECOSYSTEM_REFERENCE",
        "package_name": null,
        "package_path": null,
        "canonical_ecosystem_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/",
        "canonical_domain_refs": [
            {
                "domain_id": "BUSINESS_WORK_AND_TRAINING",
                "package_name": "global_adult_business_work_training_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_business_work_training_core_ecosystem"
            },
            {
                "domain_id": "ADULT_MEDIA_AND_CREATOR_ECONOMY",
                "package_name": "global_adult_media_creator_economy_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_media_creator_economy_core_ecosystem"
            },
            {
                "domain_id": "TECHNOLOGY_AND_INFRASTRUCTURE",
                "package_name": "global_adult_technology_infrastructure_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_technology_infrastructure_core_ecosystem"
            }
        ],
        "module_folders": [
            "adult_creator_economy_18_plus",
            "adult_industry_work_business_18_plus",
            "adult_production_studios_18_plus"
        ]
    },
    {
        "domain_id": "ADULT_CONSENT_AGE_SAFETY_PRIVACY_AND_RIGHTS_18_PLUS",
        "name": "Adult Consent, Age, Safety, Privacy and Rights 18+",
        "purpose": "Age assurance, informed consent, performer rights, privacy, safety, lawful licensing, jurisdictional review, moderation and protection against exploitation.",
        "age_restricted": true,
        "implementation_mode": "CROSS_ECOSYSTEM_REFERENCE",
        "package_name": null,
        "package_path": null,
        "canonical_ecosystem_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/",
        "canonical_domain_refs": [
            {
                "domain_id": "LAW_SAFETY_AND_COMPLIANCE",
                "package_name": "global_adult_law_safety_compliance_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_law_safety_compliance_core_ecosystem"
            },
            {
                "domain_id": "GLOBAL_AND_REGIONAL_GOVERNANCE",
                "package_name": "global_adult_wellness_governance_partnerships_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_wellness_governance_partnerships_core_ecosystem"
            },
            {
                "domain_id": "HEALTHCARE_AND_RESEARCH",
                "package_name": "global_sexual_reproductive_healthcare_research_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_sexual_reproductive_healthcare_research_core_ecosystem"
            }
        ],
        "module_folders": [
            "adult_age_verification_safety_18_plus",
            "adult_performer_rights_consent_18_plus",
            "adult_privacy_security_compliance_18_plus"
        ]
    },
    {
        "domain_id": "ADULT_COMMERCE_SUBSCRIPTIONS_AND_BILLING_18_PLUS",
        "name": "Adult Commerce, Subscriptions and Billing 18+",
        "purpose": "Age-gated membership, subscription disclosure, lawful commerce, payment and cancellation metadata; actual payment processing is delegated to Finance and approved payment providers.",
        "age_restricted": true,
        "implementation_mode": "CROSS_ECOSYSTEM_REFERENCE",
        "package_name": null,
        "package_path": null,
        "canonical_ecosystem_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/",
        "canonical_domain_refs": [
            {
                "domain_id": "PAYMENTS_AND_BILLING",
                "package_name": "global_adult_payments_billing_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_payments_billing_core_ecosystem"
            },
            {
                "domain_id": "COMMERCE_AND_MARKETPLACES",
                "package_name": "global_adult_wellness_commerce_marketplace_core_ecosystem",
                "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_core_ecosystem/global_adult_wellness_commerce_marketplace_core_ecosystem"
            }
        ],
        "module_folders": [
            "adult_subscriptions_memberships_18_plus"
        ]
    }
]''')
DOMAIN_DEFINITIONS: dict[str, dict[str, Any]] = {
    item["domain_id"]: item for item in DOMAIN_RECORDS
}
MODULE_DOMAIN_MAP: dict[str, list[str]] = {
    "adult_age_verification_safety_18_plus": [
        "ADULT_CONSENT_AGE_SAFETY_PRIVACY_AND_RIGHTS_18_PLUS"
    ],
    "adult_content_distribution_licensing_18_plus": [
        "ADULT_MEDIA_PORNOGRAPHY_AND_CONTENT_GOVERNANCE_18_PLUS"
    ],
    "adult_couple_intimacy_education_18_plus": [
        "ADULT_INTIMACY_KAMASUTRA_AND_SEXUAL_WELLNESS_18_PLUS"
    ],
    "adult_creator_economy_18_plus": [
        "ADULT_CREATOR_ECONOMY_PRODUCTION_AND_WORK_18_PLUS"
    ],
    "adult_industry_work_business_18_plus": [
        "ADULT_CREATOR_ECONOMY_PRODUCTION_AND_WORK_18_PLUS"
    ],
    "adult_live_streaming_18_plus": [
        "ADULT_MEDIA_PORNOGRAPHY_AND_CONTENT_GOVERNANCE_18_PLUS"
    ],
    "adult_media_pornography_18_plus": [
        "ADULT_MEDIA_PORNOGRAPHY_AND_CONTENT_GOVERNANCE_18_PLUS"
    ],
    "adult_performer_rights_consent_18_plus": [
        "ADULT_CONSENT_AGE_SAFETY_PRIVACY_AND_RIGHTS_18_PLUS"
    ],
    "adult_privacy_security_compliance_18_plus": [
        "ADULT_CONSENT_AGE_SAFETY_PRIVACY_AND_RIGHTS_18_PLUS"
    ],
    "adult_production_studios_18_plus": [
        "ADULT_CREATOR_ECONOMY_PRODUCTION_AND_WORK_18_PLUS"
    ],
    "adult_subscriptions_memberships_18_plus": [
        "ADULT_COMMERCE_SUBSCRIPTIONS_AND_BILLING_18_PLUS"
    ],
    "advanced": [
        "LIFE_STAGES_AND_HUMAN_DEVELOPMENT",
        "EDUCATION_LEARNING_AND_SKILLS"
    ],
    "dating_matchmaking_relationships": [
        "DATING_RELATIONSHIPS_MARRIAGE_AND_COMPATIBILITY"
    ],
    "enterprise": [],
    "family_parenting_care": [
        "FAMILY_PARENTING_AND_CAREGIVING",
        "DATING_RELATIONSHIPS_MARRIAGE_AND_COMPATIBILITY"
    ],
    "family_safety_survivor_support": [
        "PERSONAL_SAFETY_CRISIS_AND_SURVIVOR_SUPPORT",
        "MENTAL_EMOTIONAL_AND_SOCIAL_WELLBEING"
    ],
    "global_digital_services": [
        "DIGITAL_LIFE_AND_GLOBAL_DIGITAL_SERVICES"
    ],
    "global_people_work_life": [
        "LIFE_STAGES_AND_HUMAN_DEVELOPMENT",
        "IDENTITY_CITIZENSHIP_AND_PERSONAL_ADMIN",
        "PERSONAL_FINANCE_AND_LIFE_PLANNING",
        "HOME_HOUSEHOLD_AND_DAILY_LIVING",
        "PHYSICAL_HEALTH_WELLBEING_AND_ACCESSIBILITY",
        "MENTAL_EMOTIONAL_AND_SOCIAL_WELLBEING",
        "COMMUNITY_CULTURE_SPIRITUALITY_AND_BELONGING",
        "TRAVEL_MOBILITY_LEISURE_AND_RECREATION",
        "AGEING_RETIREMENT_AND_LIFE_TRANSITIONS",
        "GLOBAL_INDIA_AND_CROSS_BORDER_PEOPLE_LIFE"
    ],
    "india_digital_public_services": [
        "IDENTITY_CITIZENSHIP_AND_PERSONAL_ADMIN",
        "CIVIC_LEGAL_AND_PUBLIC_SERVICES"
    ],
    "india_people_work_life": [
        "LIFE_STAGES_AND_HUMAN_DEVELOPMENT",
        "CAREER_EMPLOYMENT_AND_WORKFORCE",
        "HOME_HOUSEHOLD_AND_DAILY_LIVING",
        "GLOBAL_INDIA_AND_CROSS_BORDER_PEOPLE_LIFE"
    ],
    "normal": [],
    "premium": [],
    "sexual_health_reproductive_education": [
        "PHYSICAL_HEALTH_WELLBEING_AND_ACCESSIBILITY",
        "SEXUAL_REPRODUCTIVE_HEALTH_AND_EDUCATION"
    ],
    "small_business_msme_support": [
        "ENTREPRENEURSHIP_LIVELIHOOD_AND_SMALL_BUSINESS",
        "PERSONAL_FINANCE_AND_LIFE_PLANNING"
    ],
    "standard": [],
    "student_youth_development": [
        "LIFE_STAGES_AND_HUMAN_DEVELOPMENT",
        "EDUCATION_LEARNING_AND_SKILLS"
    ],
    "supreme": [],
    "workforce_professional_services": [
        "EDUCATION_LEARNING_AND_SKILLS",
        "CAREER_EMPLOYMENT_AND_WORKFORCE",
        "ENTREPRENEURSHIP_LIVELIHOOD_AND_SMALL_BUSINESS"
    ]
}
DOMAIN_PACKAGE_MAP: dict[str, str] = {
    item["domain_id"]: item["package_name"]
    for item in DOMAIN_RECORDS if item["package_name"]
}
SERVICE_TIER_MODULES = {
    item["folder"]: item["service_tier_id"]
    for item in PEOPLE_LIFE_MODULES if item.get("service_tier_id")
}

def list_people_life_modules() -> list[dict[str, Any]]:
    return redact_sensitive_metadata(list(PEOPLE_LIFE_MODULES))

def get_people_life_module(folder_or_id: str) -> dict[str, Any] | None:
    needle = folder_or_id.strip().casefold()
    if not needle:
        return None
    for item in PEOPLE_LIFE_MODULES:
        if item["folder"].casefold() == needle or item["id"].casefold() == needle:
            return redact_sensitive_metadata(item)
    return None

def list_people_life_domains(include_external: bool = True) -> list[dict[str, Any]]:
    items = DOMAIN_RECORDS if include_external else [x for x in DOMAIN_RECORDS if x["implementation_mode"] == "LOCAL_DOMAIN_PACKAGE"]
    return redact_sensitive_metadata(items)

def get_people_life_domain(domain_id: str) -> dict[str, Any] | None:
    needle = domain_id.strip().upper()
    item = DOMAIN_DEFINITIONS.get(needle)
    return redact_sensitive_metadata(item) if item else None

def list_people_life_domain_inventory() -> list[dict[str, Any]]:
    modules = {item["folder"]: item for item in PEOPLE_LIFE_MODULES}
    result = []
    for domain in DOMAIN_RECORDS:
        result.append({
            **redact_sensitive_metadata(domain),
            "modules": [redact_sensitive_metadata(modules[name]) for name in domain.get("module_folders", []) if name in modules],
            "module_count": len([name for name in domain.get("module_folders", []) if name in modules]),
        })
    return result

def people_life_domain_summary() -> dict[str, Any]:
    modes = Counter(item["implementation_mode"] for item in DOMAIN_RECORDS)
    return {
        "domain_count": len(DOMAIN_RECORDS),
        "local_domain_package_count": modes["LOCAL_DOMAIN_PACKAGE"],
        "cross_ecosystem_domain_reference_count": modes["CROSS_ECOSYSTEM_REFERENCE"],
        "age_restricted_domain_count": sum(bool(x["age_restricted"]) for x in DOMAIN_RECORDS),
        "module_count": len(PEOPLE_LIFE_MODULES),
        "mapped_module_count": sum(bool(x.get("domain_ids")) or bool(x.get("service_tier_id")) for x in PEOPLE_LIFE_MODULES),
        "unmapped_module_count": sum(not x.get("domain_ids") and not x.get("service_tier_id") for x in PEOPLE_LIFE_MODULES),
        "service_tier_count": 7,
        "coverage_exhaustive": False,
        "coverage_model": "LIFECYCLE_AND_CROSS_DOMAIN_TAXONOMY",
    }

get_domains = list_people_life_domains
get_domain = get_people_life_domain
