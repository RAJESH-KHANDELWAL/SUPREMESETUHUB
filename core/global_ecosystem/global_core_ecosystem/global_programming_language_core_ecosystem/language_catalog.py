"""Curated language-type registry; deliberately non-exhaustive and metadata-only."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

LANGUAGE_RECORDS: tuple[dict[str, Any], ...] = (
 {"language_id":"PYTHON","canonical_name":"Python","language_type":"GENERAL_PURPOSE","aliases":["py"],"paradigms":["object-oriented","imperative","functional"],"runtime_or_compiler":"CPython; alternative implementations exist","support_status":"METADATA_ONLY"},
 {"language_id":"JAVASCRIPT","canonical_name":"JavaScript","language_type":"GENERAL_PURPOSE","aliases":["JS","ECMAScript"],"paradigms":["event-driven","functional","object-oriented"],"runtime_or_compiler":"Browser engines; Node.js and other runtimes","support_status":"METADATA_ONLY"},
 {"language_id":"TYPESCRIPT","canonical_name":"TypeScript","language_type":"GENERAL_PURPOSE_TYPED_SUPERSET","aliases":["TS"],"paradigms":["object-oriented","functional"],"runtime_or_compiler":"TypeScript compiler; emits JavaScript","support_status":"METADATA_ONLY"},
 {"language_id":"JAVA","canonical_name":"Java","language_type":"GENERAL_PURPOSE","paradigms":["class-based","object-oriented"],"runtime_or_compiler":"JVM","support_status":"METADATA_ONLY"},
 {"language_id":"C","canonical_name":"C","language_type":"SYSTEMS","paradigms":["procedural"],"runtime_or_compiler":"Native C compilers","support_status":"METADATA_ONLY"},
 {"language_id":"CPP","canonical_name":"C++","language_type":"SYSTEMS_GENERAL_PURPOSE","aliases":["C plus plus"],"paradigms":["procedural","object-oriented","generic"],"runtime_or_compiler":"Native C++ compilers","support_status":"METADATA_ONLY"},
 {"language_id":"RUST","canonical_name":"Rust","language_type":"SYSTEMS","paradigms":["imperative","functional"],"runtime_or_compiler":"rustc; LLVM backend","support_status":"METADATA_ONLY"},
 {"language_id":"GO","canonical_name":"Go","language_type":"GENERAL_PURPOSE_SYSTEMS","aliases":["Golang"],"paradigms":["concurrent","imperative"],"runtime_or_compiler":"Go toolchain","support_status":"METADATA_ONLY"},
 {"language_id":"RUBY","canonical_name":"Ruby","language_type":"GENERAL_PURPOSE","paradigms":["object-oriented","imperative","functional"],"runtime_or_compiler":"CRuby and alternative implementations","support_status":"METADATA_ONLY"},
 {"language_id":"PHP","canonical_name":"PHP","language_type":"GENERAL_PURPOSE_WEB","paradigms":["imperative","object-oriented"],"runtime_or_compiler":"PHP runtime","support_status":"METADATA_ONLY"},
 {"language_id":"HTML","canonical_name":"HTML","language_type":"MARKUP","aliases":["HyperText Markup Language"],"specification":"WHATWG HTML Living Standard","support_status":"METADATA_ONLY"},
 {"language_id":"CSS","canonical_name":"CSS","language_type":"STYLESHEET","aliases":["Cascading Style Sheets"],"specification":"W3C CSS specifications","support_status":"METADATA_ONLY"},
 {"language_id":"SQL","canonical_name":"SQL","language_type":"DATABASE_QUERY","aliases":["Structured Query Language"],"specification":"ISO/IEC SQL standards","support_status":"METADATA_ONLY"},
 {"language_id":"JSON","canonical_name":"JSON","language_type":"DATA_SERIALIZATION","specification":"RFC 8259","support_status":"METADATA_ONLY"},
 {"language_id":"YAML","canonical_name":"YAML","language_type":"DATA_SERIALIZATION","specification":"YAML specification","support_status":"METADATA_ONLY"},
)

def list_language_records(language_type: str | None = None) -> list[dict[str, Any]]:
    records = LANGUAGE_RECORDS
    if language_type:
        records = tuple(x for x in records if x["language_type"] == language_type.strip().upper())
    return deepcopy(list(records))

def get_language_record(language_id_or_name: str) -> dict[str, Any] | None:
    needle = language_id_or_name.strip().casefold()
    for item in LANGUAGE_RECORDS:
        names = [item["language_id"], item["canonical_name"], *item.get("aliases", [])]
        if needle in {name.casefold() for name in names}:
            return deepcopy(item)
    return None

def language_catalog_summary() -> dict[str, Any]:
    from collections import Counter
    counts = Counter(item["language_type"] for item in LANGUAGE_RECORDS)
    return {"record_count": len(LANGUAGE_RECORDS), "type_counts": dict(sorted(counts.items())), "coverage_exhaustive": False}
