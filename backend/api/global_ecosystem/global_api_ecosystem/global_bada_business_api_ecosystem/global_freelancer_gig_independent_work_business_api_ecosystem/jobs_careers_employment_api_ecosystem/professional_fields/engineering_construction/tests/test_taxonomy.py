from ..categories import FIELD_ID, SUBCATEGORY_DEFINITIONS
from ..validators import validate_field_taxonomy
from ..services import get_subcategory, list_subcategories

def test_field_taxonomy_is_structurally_valid():
    assert validate_field_taxonomy()["structurally_valid"] is True

def test_subcategory_ids_are_unique():
    ids = [item["id"] for item in SUBCATEGORY_DEFINITIONS]
    assert len(ids) == len(set(ids))

def test_subcategory_lookup_is_scoped_to_field():
    first = SUBCATEGORY_DEFINITIONS[0]["id"]
    assert get_subcategory(first)["id"] == first
    assert get_subcategory("not_a_real_subcategory") is None

def test_field_identity_and_count():
    assert FIELD_ID
    assert len(list_subcategories()) == len(SUBCATEGORY_DEFINITIONS)
