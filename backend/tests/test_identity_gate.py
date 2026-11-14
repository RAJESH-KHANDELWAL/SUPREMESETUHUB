import pytest

from backend.database.gde_connection import IDENTITIES, IDENTITY_GATES, PRIMARY_IDENTITY
from backend.database.identity_context import get_identity, reset_identity, set_identity
from backend.database.identity_gate import IdentityGateError, IdentityGateService


def test_identity_hierarchy_is_one_main_and_four_gates():
    assert PRIMARY_IDENTITY == "SUPREMESETUHUB"
    assert len(IDENTITY_GATES) == 4
    assert len(IDENTITIES) == 5


@pytest.mark.parametrize("code", IDENTITIES)
def test_normalize_accepts_all_five_identities(code):
    assert IdentityGateService.normalize(code.lower()) == code


@pytest.mark.parametrize("code", ["", "UNKNOWN", "SUPREME", "../SUPREMESETUHUB"])
def test_normalize_rejects_unknown_identity(code):
    with pytest.raises(IdentityGateError):
        IdentityGateService.normalize(code)


def test_scope_filter_is_parameterized():
    sql, params = IdentityGateService.scope_filter(
        "DRRAJESHKHANDELWALIBC", column="identity_code"
    )
    assert sql == "identity_code = %s"
    assert params == ("DRRAJESHKHANDELWALIBC",)


def test_scope_filter_rejects_unsafe_column():
    with pytest.raises(ValueError):
        IdentityGateService.scope_filter("SUPREMESETUHUB", column="id; DROP TABLE users")


def test_request_identity_context_is_isolated_and_reset():
    token = set_identity("RAJESHKHANDELWALOFFICIAL", "principal-123")
    try:
        context = get_identity()
        assert context.identity_code == "RAJESHKHANDELWALOFFICIAL"
        assert context.principal_id == "principal-123"
    finally:
        reset_identity(token)
    assert get_identity(required=False) is None
