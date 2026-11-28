from ..service import DistributionChannelsService
from ..business_profiles import CHANNEL_BUSINESS_PROFILES

def test_channel_catalog_has_factory_to_customer_stages():
    service = DistributionChannelsService()
    items = service.list_channels()
    assert len(items) == 25
    assert service.get_channel("factory_dispatch") is not None
    assert service.get_channel("end_customer_handover") is not None

def test_every_channel_has_a_business_profile():
    service = DistributionChannelsService()
    items = service.list_channels()
    assert len(CHANNEL_BUSINESS_PROFILES) == 25
    assert all(item["business_profile"] for item in items)
    for item in items:
        profile = item["business_profile"]
        assert profile["business_types"]
        assert profile["operating_modes"]
        assert profile["core_activities"]
        assert profile["onboarding_data"]

def test_factory_dispatch_profile_handoffs_to_warehouse_or_customer():
    profile = DistributionChannelsService().get_channel("factory_dispatch")["business_profile"]
    assert "finished_goods_warehouse" in profile["handoff_to"]
    assert "end_customer_handover" in profile["handoff_to"]

def test_wholesaler_profile_serves_retail_and_institutional_buyers():
    profile = DistributionChannelsService().get_channel("wholesalers")["business_profile"]
    assert "retailers_shopkeepers" in profile["handoff_to"]
    assert "institutional_bulk_buyers" in profile["handoff_to"]

def test_search_and_unknown_channel():
    service = DistributionChannelsService()
    assert service.list_channels("super stockist")
    assert service.get_channel("not-a-real-channel") is None
