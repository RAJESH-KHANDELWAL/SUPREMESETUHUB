"""Offline tests for the Bada Business program execution engine."""
import pytest

from .engine import (
    BadaBusinessProgramEngine,
    ProgramEngineNotConfigured,
    ProgramEngineValidationError,
)


def test_health_exposes_engine_layer_and_unverified_connection():
    result = BadaBusinessProgramEngine().health()
    assert result["layer"] == "ENGINE"
    assert result["status"] == "READY"
    assert result["live_provider_connection_verified"] is False


def test_list_programs_reads_canonical_catalog_without_side_effects():
    result = BadaBusinessProgramEngine().execute("LIST_PROGRAMS")
    assert result["success"] is True
    assert result["count"] >= 1
    assert result["executed"] is False


def test_get_program_requires_program_id():
    with pytest.raises(ProgramEngineValidationError):
        BadaBusinessProgramEngine().execute("GET_PROGRAM", {})


def test_get_program_rejects_unknown_id():
    with pytest.raises(ProgramEngineValidationError):
        BadaBusinessProgramEngine().execute(
            "GET_PROGRAM", {"program_id": "unknown-program"}
        )


def test_get_program_reads_canonical_record():
    engine = BadaBusinessProgramEngine()
    first = engine.execute("LIST_PROGRAMS")["data"][0]
    result = engine.execute("GET_PROGRAM", {"program_id": first["program_id"]})
    assert result["success"] is True
    assert result["source"] == "canonical_catalog"
    assert result["data"]["program_id"] == first["program_id"]


def test_prepare_program_is_dry_run_only():
    engine = BadaBusinessProgramEngine()
    program = engine.execute("LIST_PROGRAMS")["data"][0]
    result = engine.execute(
        "PREPARE_PROGRAM", {"program_id": program["program_id"]}
    )
    assert result["dry_run"] is True
    assert result["executed"] is False
    assert result["requires_core_approval"] is True


def test_execute_program_is_not_enabled_without_handler():
    engine = BadaBusinessProgramEngine()
    program = engine.execute("LIST_PROGRAMS")["data"][0]
    with pytest.raises(ProgramEngineNotConfigured):
        engine.execute(
            "EXECUTE_PROGRAM", {"program_id": program["program_id"]}
        )


def test_execute_program_dry_run_never_calls_handler():
    called = []
    engine = BadaBusinessProgramEngine(
        {"EXECUTE_PROGRAM": lambda payload: called.append(payload)}
    )
    program = engine.execute("LIST_PROGRAMS")["data"][0]
    result = engine.execute(
        "EXECUTE_PROGRAM",
        {"program_id": program["program_id"]},
        dry_run=True,
    )
    assert result["executed"] is False
    assert called == []


def test_injected_handler_executes_explicitly():
    received = []
    engine = BadaBusinessProgramEngine(
        {"EXECUTE_PROGRAM": lambda payload: received.append(payload) or {"queued": True}}
    )
    program = engine.execute("LIST_PROGRAMS")["data"][0]
    result = engine.execute(
        "EXECUTE_PROGRAM", {"program_id": program["program_id"]}
    )
    assert result["executed"] is True
    assert result["provider_connection_verified"] is False
    assert received[0]["program_id"] == program["program_id"]


def test_unknown_operation_is_rejected():
    with pytest.raises(ProgramEngineValidationError):
        BadaBusinessProgramEngine().execute("DELETE_EVERYTHING", {})
