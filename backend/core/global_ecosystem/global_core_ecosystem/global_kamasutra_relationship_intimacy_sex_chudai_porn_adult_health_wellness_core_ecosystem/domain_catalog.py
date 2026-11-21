"""Canonical responsibility domains and package classification."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
DOMAINS: dict[str, dict[str, Any]] = {
    "RELATIONSHIPS_AND_COMPATIBILITY": {
        "domain_id": "RELATIONSHIPS_AND_COMPATIBILITY",
        "name": "Relationships and Compatibility",
        "purpose": "Dating, couples, marriage, family systems and adult relationship wellbeing.",
        "product_ids": [
            "ADULT-RELATIONSHIPS-COMPATIBILITY",
            "COUPLE-INTIMACY-ROMANCE",
            "DATING-GF-BF-RELATIONSHIPS",
            "FAMILY-PARENTING-REPRODUCTIVE-WELLNESS",
            "FAMILY-RELATIONSHIPS-COMMUNITY-BUSINESS-CORE-ECOSYSTEM",
            "FAMILY-RELATIONSHIPS-PARENTING",
            "MARRIAGE-MARRIED-LIFE",
            "MATURE-ADULT-RELATIONSHIPS"
        ]
    },
    "SEXUAL_EDUCATION_AND_TRADITIONAL_KNOWLEDGE": {
        "domain_id": "SEXUAL_EDUCATION_AND_TRADITIONAL_KNOWLEDGE",
        "name": "Sexual Education and Traditional Knowledge",
        "purpose": "Evidence-informed adult sexual education, consent literacy and historical Kamasutra studies.",
        "product_ids": [
            "ADULT-SEXUAL-EDUCATION",
            "KAMASUTRA-ANCIENT-KNOWLEDGE",
            "SEXUAL-PRACTICES-INTIMACY"
        ]
    },
    "HEALTHCARE_AND_RESEARCH": {
        "domain_id": "HEALTHCARE_AND_RESEARCH",
        "name": "Healthcare and Research",
        "purpose": "Sexual and reproductive health domains, wellness research and licensed clinical boundaries.",
        "product_ids": [
            "ADULT-BODY-FITNESS-WELLNESS",
            "LGBTQ-ADULT-WELLNESS",
            "MEDICAL-HEALTHCARE-PROFESSIONALS",
            "MENS-SEXUAL-HEALTH",
            "SEXUAL-HEALTH-RESEARCH-INNOVATION",
            "SEXUAL-REPRODUCTIVE-HEALTHCARE",
            "WOMENS-SEXUAL-HEALTH"
        ]
    },
    "COACHING_AND_COUNSELLING": {
        "domain_id": "COACHING_AND_COUNSELLING",
        "name": "Coaching and Counselling",
        "purpose": "Non-clinical coaching and professional counselling directories; clinical care remains with licensed providers.",
        "product_ids": [
            "CONSULTANTS-ADVISORS-PROFESSIONAL-SERVICES",
            "INTIMACY-COACHING",
            "RELATIONSHIP-COACHING",
            "SEXOLOGY-PROFESSIONAL-COUNSELLING",
            "SEXUAL-PSYCHOLOGY-THERAPY",
            "SEXUAL-WELLNESS-COACHING"
        ]
    },
    "ADULT_MEDIA_AND_CREATOR_ECONOMY": {
        "domain_id": "ADULT_MEDIA_AND_CREATOR_ECONOMY",
        "name": "Adult Media and Creator Economy",
        "purpose": "Lawful adult media platforms, creator services, distribution and moderation for consenting adults.",
        "product_ids": [
            "ADULT-ENTERTAINMENT-PORN-MEDIA",
            "ADULT-MEDIA-CREATORS",
            "BANGBROS-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "BRAZZERS-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "CLIPS4SALE-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "EVILANGEL-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "FANSLY-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "FAPHOUSE-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "LOYALFANS-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "MANYVIDS-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "NAUGHTYAMERICA-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "ONLYFANS-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "PORNHUB-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "REALITYKINGS-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "VICETEMPLE-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "XHAMSTER-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "XVIDEOS-ADULT-INDUSTRY-CORE-ECOSYSTEM"
        ]
    },
    "BUSINESS_WORK_AND_TRAINING": {
        "domain_id": "BUSINESS_WORK_AND_TRAINING",
        "name": "Business, Work and Training",
        "purpose": "Industry operations, employment, professional training and enterprise development.",
        "product_ids": [
            "ADULT-BUSINESS-MANAGEMENT-DEVELOPMENT",
            "ADULT-STARTUPS-MSMES-COMPANIES",
            "ADULT-TRAINING-CERTIFICATION-DEVELOPMENT",
            "ADULT-WORK-JOBS-CAREERS"
        ]
    },
    "COMMERCE_AND_MARKETPLACES": {
        "domain_id": "COMMERCE_AND_MARKETPLACES",
        "name": "Commerce and Marketplaces",
        "purpose": "B2B/B2C marketplaces and lawful adult-wellness product commerce.",
        "product_ids": [
            "ADULT-B2B-B2C-MARKETPLACE-TRADE",
            "ADULT-WELLNESS-PRODUCTS-COMMERCE"
        ]
    },
    "TECHNOLOGY_AND_INFRASTRUCTURE": {
        "domain_id": "TECHNOLOGY_AND_INFRASTRUCTURE",
        "name": "Technology and Infrastructure",
        "purpose": "Software, APIs, hosting, infrastructure and technical enablement.",
        "product_ids": [
            "ADULT-TECHNOLOGY-SOFTWARE-APIS",
            "CLOUDFLARE-ADULT-INDUSTRY-CORE-ECOSYSTEM"
        ]
    },
    "LAW_SAFETY_AND_COMPLIANCE": {
        "domain_id": "LAW_SAFETY_AND_COMPLIANCE",
        "name": "Law, Safety and Compliance",
        "purpose": "Age assurance, consent, rights, privacy, moderation, reporting and legal controls.",
        "product_ids": [
            "ADULT-LAW-SAFETY-COMPLIANCE"
        ]
    },
    "PAYMENTS_AND_BILLING": {
        "domain_id": "PAYMENTS_AND_BILLING",
        "name": "Payments and Billing",
        "purpose": "Payment processors, billing, payouts and provider metadata.",
        "product_ids": [
            "CCBILL-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "EPOCH-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "PAXUM-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "SEGPAY-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "VEROTEL-ADULT-INDUSTRY-CORE-ECOSYSTEM"
        ]
    },
    "ADVERTISING_AND_DISTRIBUTION": {
        "domain_id": "ADVERTISING_AND_DISTRIBUTION",
        "name": "Advertising and Distribution",
        "purpose": "Advertising networks, affiliate/referral infrastructure and distribution controls.",
        "product_ids": [
            "CRAKREVENUE-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "EXOCLICK-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "TRAFFICJUNKY-ADULT-INDUSTRY-CORE-ECOSYSTEM"
        ]
    },
    "GLOBAL_AND_REGIONAL_GOVERNANCE": {
        "domain_id": "GLOBAL_AND_REGIONAL_GOVERNANCE",
        "name": "Global and Regional Governance",
        "purpose": "Bharat/global coverage, partnerships and ecosystem-level coordination.",
        "product_ids": [
            "ABELOHOST-ADULT-INDUSTRY-CORE-ECOSYSTEM",
            "BHARAT-ADULT-WELLNESS-CORE-ECOSYSTEM",
            "GLOBAL-ADULT-WELLNESS-CORE-ECOSYSTEM",
            "GLOBAL-PARTNERSHIPS-NETWORKING"
        ]
    }
}
def list_domains() -> list[dict[str, Any]]:
    return deepcopy(list(DOMAINS.values()))
def get_domain(domain_id: str) -> dict[str, Any] | None:
    item = DOMAINS.get(str(domain_id).strip().upper())
    return deepcopy(item) if item else None
__all__ = ["DOMAINS", "list_domains", "get_domain"]
