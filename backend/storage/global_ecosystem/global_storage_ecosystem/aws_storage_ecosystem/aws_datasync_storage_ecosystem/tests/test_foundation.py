from aws_datasync_storage_ecosystem.ecosystem_service import get_status

def test_category_is_not_connected_by_default():
    status = get_status()
    assert status["provider"] == "AWS"
    assert status["category"] == "DATASYNC"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["storage_operations_enabled"] is False
