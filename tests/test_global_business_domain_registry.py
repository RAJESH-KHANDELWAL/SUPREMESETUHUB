from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.domain_registry import (
    DOMAIN_REGISTRY,
    get_domain,
    list_domains,
    search_domains,
    validate_domain_registry,
)


def test_registry_has_twelve_domain_packages():
    assert len(DOMAIN_REGISTRY) == 12
    assert len(list_domains()) == 11


def test_subcategory_ids_are_present_and_unique_within_domains():
    for domain in DOMAIN_REGISTRY:
        values = domain["subcategory_ids"]
        assert values
        assert len(values) == len(set(values))
        assert all(value == value.lower() and " " not in value for value in values)


def test_adult_domain_is_excluded_by_default():
    adult = next(item for item in DOMAIN_REGISTRY if item["adult_only"])
    assert get_domain(adult["id"]) is None
    assert get_domain(adult["id"], include_adult=True) is not None
    assert adult["id"] not in {item["id"] for item in list_domains()}


def test_search_finds_domain_subcategory():
    matches = search_domains("web_development")
    assert any(item["domain_id"] == "freelance_gig_independent_work" for item in matches)


def test_registry_integrity_is_structurally_valid():
    result = validate_domain_registry()
    assert result["structurally_valid"] is True
    assert result["domain_count"] == 12
    assert result["adult_excluded_by_default"] is True
