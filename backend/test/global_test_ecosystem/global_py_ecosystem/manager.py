"""Inventory Python tests while preserving established CI import paths."""
from pathlib import Path

TEST_ROOT = Path(__file__).resolve().parents[2]


def inventory() -> dict[str, object]:
    """Return the legacy Python test files grouped under the global test ecosystem."""
    files = sorted(
        path.relative_to(TEST_ROOT).as_posix()
        for path in TEST_ROOT.glob("test_*.py")
        if path.is_file()
    )
    return {"language": "python", "test_root": "backend/test", "test_count": len(files), "tests": files}


def get_manager() -> "PythonTestEcosystemManager":
    return PythonTestEcosystemManager()


class PythonTestEcosystemManager:
    def inventory(self) -> dict[str, object]:
        return inventory()


if __name__ == "__main__":
    result = inventory()
    print(f"GLOBAL PYTHON TEST ECOSYSTEM: {result['test_count']} test files inventoried")
