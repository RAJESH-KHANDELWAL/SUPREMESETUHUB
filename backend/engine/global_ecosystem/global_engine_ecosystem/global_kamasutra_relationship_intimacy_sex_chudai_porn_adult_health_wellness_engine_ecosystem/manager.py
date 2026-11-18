"""Central manager and catalog for the global Kamasutra ENGINE ecosystem."""
from __future__ import annotations

from importlib import import_module
from typing import Callable

from .engine import ProviderEngine
from .models import EngineDescriptor
from .registry import EngineRegistry


PROVIDER = "GLOBAL KAMASUTRA RELATIONSHIP INTIMACY SEX CHUDAI PORN ADULT HEALTH WELLNESS"

# Existing catalog labels retained from catalog.py.
CHILD_ECOSYSTEMS = [
    "ABELOHOST ADULT INDUSTRY",
    "ADULT B2B B2C MARKETPLACE TRADE",
    "ADULT BODY FITNESS WELLNESS",
    "ADULT BUSINESS MANAGEMENT DEVELOPMENT",
    "ADULT ENTERTAINMENT PORN MEDIA",
    "ADULT LAW SAFETY COMPLIANCE",
    "ADULT MEDIA CREATORS",
    "ADULT RELATIONSHIPS COMPATIBILITY",
    "ADULT SEXUAL EDUCATION",
    "ADULT STARTUPS MSMES COMPANIES",
    "ADULT TECHNOLOGY SOFTWARE APIS",
    "ADULT TRAINING CERTIFICATION DEVELOPMENT",
    "ADULT WELLNESS PRODUCTS COMMERCE",
    "ADULT WORK JOBS CAREERS",
    "BANGBROS ADULT INDUSTRY",
    "BHARAT ADULT WELLNESS ECOSYSTEM",
    "BRAZZERS ADULT INDUSTRY",
    "CCBILL ADULT INDUSTRY",
    "CLIPS4SALE ADULT INDUSTRY",
    "CLOUDFLARE ADULT INDUSTRY",
    "CONSULTANTS ADVISORS PROFESSIONAL SERVICES",
    "COUPLE INTIMACY ROMANCE",
    "CRAKREVENUE ADULT INDUSTRY",
    "DATING GF BF RELATIONSHIPS",
    "EPOCH ADULT INDUSTRY",
    "EVILANGEL ADULT INDUSTRY",
    "EXOCLICK ADULT INDUSTRY",
    "FAMILY PARENTING REPRODUCTIVE WELLNESS",
    "FAMILY RELATIONSHIPS COMMUNITY BUSINESS",
    "FAMILY RELATIONSHIPS PARENTING",
    "FANSLY ADULT INDUSTRY",
    "FAPHOUSE ADULT INDUSTRY",
    "GLOBAL ADULT WELLNESS ECOSYSTEM",
    "GLOBAL PARTNERSHIPS NETWORKING",
    "INTIMACY COACHING",
    "KAMASUTRA ANCIENT KNOWLEDGE",
    "LGBTQ ADULT WELLNESS",
    "LOYALFANS ADULT INDUSTRY",
    "MANYVIDS ADULT INDUSTRY",
    "MARRIAGE MARRIED LIFE",
    "MATURE ADULT RELATIONSHIPS",
    "MEDICAL HEALTHCARE PROFESSIONALS",
    "MENS SEXUAL HEALTH",
    "NAUGHTYAMERICA ADULT INDUSTRY",
    "ONLYFANS ADULT INDUSTRY",
    "PAXUM ADULT INDUSTRY",
    "PORNHUB ADULT INDUSTRY",
    "REALITYKINGS ADULT INDUSTRY",
    "RELATIONSHIP COACHING",
    "SEGPAY ADULT INDUSTRY",
    "SEXOLOGY PROFESSIONAL COUNSELLING",
    "SEXUAL HEALTH RESEARCH INNOVATION",
    "SEXUAL PRACTICES INTIMACY",
    "SEXUAL PSYCHOLOGY THERAPY",
    "SEXUAL REPRODUCTIVE HEALTHCARE",
    "SEXUAL WELLNESS COACHING",
    "TRAFFICJUNKY ADULT INDUSTRY",
    "VEROTEL ADULT INDUSTRY",
    "VICETEMPLE ADULT INDUSTRY",
    "WOMENS SEXUAL HEALTH",
    "XHAMSTER ADULT INDUSTRY",
    "XVIDEOS ADULT INDUSTRY",
]

# These module paths match the existing child folders exactly, in catalog order.
CHILD_ENGINE_MODULES = (
    "abelohost_adult_industry_engine_ecosystem",
    "adult_b2b_b2c_marketplace_trade",
    "adult_body_fitness_wellness",
    "adult_business_management_development",
    "adult_entertainment_porn_media",
    "adult_law_safety_compliance",
    "adult_media_creators",
    "adult_relationships_compatibility",
    "adult_sexual_education",
    "adult_startups_msmes_companies",
    "adult_technology_software_apis",
    "adult_training_certification_development",
    "adult_wellness_products_commerce",
    "adult_work_jobs_careers",
    "bangbros_adult_industry_engine_ecosystem",
    "bharat_adult_wellness_ecosystem",
    "brazzers_adult_industry_engine_ecosystem",
    "ccbill_adult_industry_engine_ecosystem",
    "clips4sale_adult_industry_engine_ecosystem",
    "cloudflare_adult_industry_engine_ecosystem",
    "consultants_advisors_professional_services",
    "couple_intimacy_romance",
    "crakrevenue_adult_industry_engine_ecosystem",
    "dating_gf_bf_relationships",
    "epoch_adult_industry_engine_ecosystem",
    "evilangel_adult_industry_engine_ecosystem",
    "exoclick_adult_industry_engine_ecosystem",
    "family_parenting_reproductive_wellness",
    "family_relationships_community_business_engine_ecosystem",
    "family_relationships_parenting",
    "fansly_adult_industry_engine_ecosystem",
    "faphouse_adult_industry_engine_ecosystem",
    "global_adult_wellness_ecosystem",
    "global_partnerships_networking",
    "intimacy_coaching",
    "kamasutra_ancient_knowledge",
    "lgbtq_adult_wellness",
    "loyalfans_adult_industry_engine_ecosystem",
    "manyvids_adult_industry_engine_ecosystem",
    "marriage_married_life",
    "mature_adult_relationships",
    "medical_healthcare_professionals",
    "mens_sexual_health",
    "naughtyamerica_adult_industry_engine_ecosystem",
    "onlyfans_adult_industry_engine_ecosystem",
    "paxum_adult_industry_engine_ecosystem",
    "pornhub_adult_industry_engine_ecosystem",
    "realitykings_adult_industry_engine_ecosystem",
    "relationship_coaching",
    "segpay_adult_industry_engine_ecosystem",
    "sexology_professional_counselling",
    "sexual_health_research_innovation",
    "sexual_practices_intimacy",
    "sexual_psychology_therapy",
    "sexual_reproductive_healthcare",
    "sexual_wellness_coaching",
    "trafficjunky_adult_industry_engine_ecosystem",
    "verotel_adult_industry_engine_ecosystem",
    "vicetemple_adult_industry_engine_ecosystem",
    "womens_sexual_health",
    "xhamster_adult_industry_engine_ecosystem",
    "xvideos_adult_industry_engine_ecosystem",
)

if len(CHILD_ECOSYSTEMS) != len(CHILD_ENGINE_MODULES):
    raise RuntimeError("Child ecosystem catalog and module map are out of sync")

CATALOG = (
    EngineDescriptor(
        "ENGINE-GLOBAL_KAMASUTRA_RELATIONSHIP_INTIMACY_SEX_CHUDAI_PORN_ADULT_HEALTH_WELLNESS",
        PROVIDER,
        PROVIDER,
        ("LIFECYCLE", "EXECUTION_BOUNDARY", "CHILD_ENGINE_REGISTRY"),
    ),
)


def list_engines():
    """Return the ecosystem's root ENGINE descriptor."""
    return [
        {
            "engine_id": item.engine_id,
            "name": item.name,
            "provider": item.provider,
            "capabilities": list(item.capabilities),
            "metadata": dict(item.metadata),
        }
        for item in CATALOG
    ]


class EcosystemEngineManager:
    """Load, register, configure, and execute the existing child ENGINE modules."""

    def __init__(self, handler: Callable | None = None, auto_load_children: bool = True):
        self.registry = EngineRegistry()
        self.root_engine = ProviderEngine(handler=handler)
        self.child_engines = {}
        self.load_errors = {}
        if auto_load_children:
            self.load_children()

    def load_children(self):
        """Import each existing child engine module and register its engine."""
        for module_name in CHILD_ENGINE_MODULES:
            if self.registry.get(module_name) is not None:
                continue
            try:
                module = import_module(
                    f".{module_name}.engine",
                    package=__package__,
                )
                engine_class = getattr(module, "ProviderEngine")
                engine = engine_class()
                self.registry.register(module_name, engine)
                self.child_engines[module_name] = engine
                self.load_errors.pop(module_name, None)
            except Exception as exc:
                self.load_errors[module_name] = f"{type(exc).__name__}: {exc}"
        return self.status()

    def register(self, key, value):
        registered = self.registry.register(key, value)
        self.child_engines[key] = registered
        return registered

    def get(self, key):
        return self.registry.get(key)

    def configure_root(self, handler: Callable):
        self.root_engine.configure(handler)
        return self.root_engine

    def configure_child(self, key: str, handler: Callable):
        if not callable(handler):
            raise TypeError("handler must be callable")
        current = self.registry.get(key)
        if current is None:
            raise KeyError("child engine is not registered: " + str(key))
        configured = type(current)(handler=handler)
        self.registry.replace(key, configured)
        self.child_engines[key] = configured
        return configured

    def execute(self, key: str, operation: str, payload: dict | None = None):
        engine = self.registry.get(key)
        if engine is None:
            raise KeyError("engine is not registered: " + str(key))
        return engine.execute(operation, payload)

    def status(self):
        configured_count = sum(
            1
            for engine in self.child_engines.values()
            if callable(getattr(engine, "_handler", None))
        )
        loaded_count = len(self.child_engines)
        expected_count = len(CHILD_ENGINE_MODULES)
        if loaded_count == expected_count and not self.load_errors and configured_count == expected_count:
            runtime_status = "READY"
        elif configured_count:
            runtime_status = "PARTIALLY_CONFIGURED"
        else:
            runtime_status = "NOT_CONFIGURED"
        return {
            "layer": "ENGINE",
            "ecosystem": PROVIDER,
            "catalog_status": "READY",
            "catalog_count": len(CATALOG),
            "child_ecosystem_count": len(CHILD_ECOSYSTEMS),
            "expected_child_engine_count": expected_count,
            "loaded_child_engine_count": loaded_count,
            "registered_count": self.registry.count(),
            "configured_child_engine_count": configured_count,
            "not_configured_child_engine_count": loaded_count - configured_count,
            "load_error_count": len(self.load_errors),
            "load_errors": dict(self.load_errors),
            "root_engine": self.root_engine.health(),
            "status": runtime_status,
        }


__all__ = [
    "PROVIDER",
    "CHILD_ECOSYSTEMS",
    "CHILD_ENGINE_MODULES",
    "CATALOG",
    "list_engines",
    "EcosystemEngineManager",
]
