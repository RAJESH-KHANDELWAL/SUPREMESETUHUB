from backend.crm.people_crm_ecosystem import PeopleCRMEcosystem
from backend.crm.people_crm_ecosystem.models import PeopleContact


def test_status_does_not_claim_google_providers_are_connected():
    status = PeopleCRMEcosystem().status()
    assert status["ecosystem"] == "PEOPLE_CRM_ECOSYSTEM"
    assert status["private_owner_crm"] == "SEPARATE_MODULE_AND_DATA_BOUNDARY"
    assert status["providers"]["GOOGLE_CONTACTS"]["status"] == "NOT_CONNECTED"
    assert status["providers"]["GOOGLE_SHEETS"]["live_api_implemented"] is False


def test_normalize_google_contact_resource():
    contact = PeopleCRMEcosystem().normalize_google_contact(
        {
            "names": [{"displayName": "Raj Kumar"}],
            "emailAddresses": [{"value": "raj@example.com"}],
            "phoneNumbers": [{"value": "+911234567890"}],
            "organizations": [{"name": "Example Co"}],
            "metadata": {"sources": [{"id": "google-resource-1"}]},
        },
        contact_id="PER-1",
    )
    assert contact.full_name == "Raj Kumar"
    assert contact.email == "raj@example.com"
    assert contact.phone == "+911234567890"
    assert contact.organization == "Example Co"
    assert contact.external_id == "google-resource-1"
    assert contact.source == "GOOGLE_CONTACTS"


def test_normalize_sheet_row_uses_explicit_column_mapping():
    contact = PeopleCRMEcosystem().normalize_sheet_row(
        {"Full Name": "Asha", "Email Address": "asha@example.com", "Mobile": "123"},
        contact_id="PER-2",
        column_map={"full_name": "Full Name", "email": "Email Address", "phone": "Mobile"},
    )
    assert contact.full_name == "Asha"
    assert contact.email == "asha@example.com"
    assert contact.phone == "123"
    assert contact.source == "GOOGLE_SHEETS"


def test_do_not_contact_cannot_have_contact_consent():
    contact = PeopleContact(
        contact_id="PER-3", full_name="Do Not Contact", contact_status="DO_NOT_CONTACT",
        consent_to_contact=True,
    )
    try:
        contact.validate()
    except ValueError as exc:
        assert "contact consent" in str(exc)
    else:
        raise AssertionError("DO_NOT_CONTACT must override contact consent")
