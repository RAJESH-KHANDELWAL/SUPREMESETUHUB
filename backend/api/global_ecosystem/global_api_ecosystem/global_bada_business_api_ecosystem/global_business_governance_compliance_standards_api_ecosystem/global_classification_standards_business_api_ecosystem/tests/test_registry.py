from .. import registry

def test_registry_ids_are_unique():
    ids = [item["id"] for item in registry.CLASSIFICATIONS]
    assert len(ids) == len(set(ids))

def test_nic_2025_source_metadata_is_explicit():
    item = registry.get_classification("india-nic-2025")
    assert item["counts"]["subclasses"] == 1887
    assert item["status"] == "metadata_verified_dataset_not_yet_ingested"

def test_country_registry_does_not_claim_missing_datasets():
    systems = registry.list_country_systems()
    assert any(item["country_code"] == "GB" and item["status"] == "source_dataset_required" for item in systems)

def test_integrity():
    assert registry.validate_classification_registry()["structurally_valid"]
