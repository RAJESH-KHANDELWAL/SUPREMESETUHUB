from ..service import DistributionChannelsService

def test_channel_catalog_has_factory_to_customer_stages():
    service = DistributionChannelsService()
    items = service.list_channels()
    assert len(items) >= 20
    assert service.get_channel("factory_dispatch") is not None
    assert service.get_channel("end_customer_handover") is not None

def test_channel_search():
    service = DistributionChannelsService()
    assert service.list_channels("super stockist")
    assert service.list_channels("retailer")

def test_unknown_channel_returns_none():
    service = DistributionChannelsService()
    assert service.get_channel("not-a-real-channel") is None
