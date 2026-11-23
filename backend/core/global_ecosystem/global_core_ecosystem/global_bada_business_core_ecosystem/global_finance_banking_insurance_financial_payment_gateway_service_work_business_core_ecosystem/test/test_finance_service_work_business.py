"""Contract tests for finance service/work/business taxonomy."""
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_finance_banking_insurance_financial_payment_gateway_service_work_business_core_ecosystem.manager import get_manager

def test_canonical_mappings_are_complete_and_unique():
    manager = get_manager()
    result = manager.validate()
    assert result["valid"], result
    assert result["business_domain_count"] == 15
    assert result["unique_domain_ids"]

def test_catalog_keeps_canonical_core_as_read_only_dependency():
    catalog = get_manager().catalog()
    assert catalog["layer"] == "GLOBAL_BADA_BUSINESS_CORE"
    assert catalog["canonical_ecosystem_id"] == "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-CORE-ECOSYSTEM"
    assert catalog["mode"] == "CLASSIFICATION_ONLY"

def test_service_work_business_classification():
    result = get_manager().classify("payment_gateway_merchant_services", "SERVICE")
    assert result["valid"]
    assert result["service_type"] == "SERVICE"
    assert result["execution_enabled"] is False

def test_unknown_domain_and_unsupported_type_are_rejected():
    manager = get_manager()
    assert not manager.classify("not_a_finance_domain", "SERVICE")["valid"]
    assert not manager.classify("banking_services", "UNSUPPORTED")["valid"]

def test_search_finds_payment_business_lines():
    results = get_manager().search("merchant")
    assert results
    assert any(item["domain_id"] == "payment_gateway_merchant_services" for item in results)
