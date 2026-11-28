from professional_fields.catalog import list_professional_fields, get_professional_field, get_professional_subcategory, validate_professional_fields

def test_professional_field_catalog_is_structurally_valid():
    assert validate_professional_fields()["structurally_valid"] is True

def test_professional_fields_have_unique_ids():
    fields = list_professional_fields()
    assert len({item.id for item in fields}) == len(fields)

def test_subcategory_lookup_is_scoped_to_parent_field():
    assert get_professional_subcategory("it_technology", "software_development") is not None
    assert get_professional_subcategory("banking_finance", "software_development") is None

def test_unknown_field_returns_none():
    assert get_professional_field("not_a_real_field") is None
