"""Integrity and behavior tests for the finance commercial CORE."""
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_finance_banking_insurance_financial_payment_gateway_service_work_business_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_finance_banking_insurance_financial_payment_gateway_service_work_business_core_ecosystem.domain_catalog import BUSINESS_DOMAINS, PACKAGE_TO_BUSINESS_DOMAIN
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_finance_banking_insurance_financial_payment_gateway_service_work_business_core_ecosystem.product_catalog import FINANCE_BUSINESS_PACKAGES
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_finance_banking_insurance_financial_payment_gateway_service_work_business_core_ecosystem.policy import FinanceBusinessPolicyError, FinanceServiceWorkBusinessPolicy
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_finance_banking_insurance_financial_payment_gateway_service_work_business_core_ecosystem.contracts import TenantContext, ClassificationRequest

def test_all_canonical_domains_and_packages_are_mapped_once():
    manager = get_manager()
    result = manager.validate()
    assert result["valid"], result
    assert result["business_domain_count"] == result["canonical_domain_count"] == 15
    assert result["canonical_package_count"] == result["mapped_package_count"]
    assert len(PACKAGE_TO_BUSINESS_DOMAIN) == len(FINANCE_BUSINESS_PACKAGES)

def test_every_domain_has_meaningful_package_and_business_line_inventory():
    assert len(BUSINESS_DOMAINS) == 15
    assert all(item["package_names"] for item in BUSINESS_DOMAINS)
    assert all(item["business_lines"] for item in BUSINESS_DOMAINS)
    assert all({"SERVICE", "WORK", "BUSINESS"} <= set(item["service_work_business_capabilities"])
               for item in BUSINESS_DOMAINS)

def test_catalog_is_registered_under_bada_business_and_references_master_catalog():
    catalog = get_manager().catalog()
    assert catalog["layer"] == "GLOBAL_BADA_BUSINESS_CORE"
    assert catalog["canonical_ecosystem_id"] == "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-CORE-ECOSYSTEM"
    assert catalog["master_catalog_ref"] == "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    assert catalog["transaction_execution_enabled"] is False

def test_manager_resolves_each_canonical_package():
    manager = get_manager()
    for package in FINANCE_BUSINESS_PACKAGES:
        assert manager.get_package(package["package_name"]) is not None

def test_domain_manager_exposes_only_its_domain_packages():
    manager = get_manager().get_domain_manager("payment_gateway_merchant_services")
    assert manager.status()["package_count"] > 0
    assert all(x["business_domain_id"] == "payment_gateway_merchant_services"
               for x in manager.list_packages()["packages"])

def test_service_work_business_classification_and_business_line_validation():
    manager = get_manager()
    result = manager.classify("payment_gateway_merchant_services", "SERVICE",
                              business_line="payment_integration", jurisdiction="IN")
    assert result["success"]
    assert result["status"] == "CLASSIFICATION_RESOLVED"
    assert result["data"]["execution_enabled"] is False
    rejected = manager.classify("payment_gateway_merchant_services", "SERVICE",
                                business_line="not_registered")
    assert not rejected["success"]

def test_unknown_domain_and_unsupported_type_are_rejected():
    manager = get_manager()
    assert not manager.classify("not_a_finance_domain", "SERVICE")["success"]
    assert not manager.classify("banking_services", "UNSUPPORTED")["success"]

def test_search_returns_domain_and_package_matches():
    result = get_manager().search("merchant")
    assert result["success"]
    assert result["domain_count"] > 0
    assert result["package_count"] > 0

def test_financial_execution_is_blocked_in_classification_core():
    for operation in ("transfer", "refund", "payout", "underwrite", "trade"):
        try:
            FinanceServiceWorkBusinessPolicy.assert_classification_only(operation)
        except FinanceBusinessPolicyError:
            continue
        raise AssertionError(f"Sensitive operation was not blocked: {operation}")

def test_tenant_and_classification_contracts_validate_required_fields():
    TenantContext("tenant-1", "actor-1").validate()
    ClassificationRequest("banking_services", "SERVICE").validate()
