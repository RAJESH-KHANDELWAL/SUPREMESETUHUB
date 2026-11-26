"""Contract tests for the canonical Backend Global Android Ecosystem native app."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
PROJECT = (
    ROOT
    / "backend"
    / "android"
    / "global_ecosystem"
    / "global_android_ecosystem"
    / "native_android_app"
)


class AndroidFoundationTests(unittest.TestCase):
    def test_native_android_project_files_exist(self):
        self.assertTrue((PROJECT / "settings.gradle").is_file())
        self.assertTrue((PROJECT / "build.gradle").is_file())
        self.assertTrue((PROJECT / "gradle.properties").is_file())
        self.assertTrue((PROJECT / "app" / "build.gradle").is_file())
        self.assertTrue((PROJECT / "app" / "src" / "main" / "AndroidManifest.xml").is_file())

    def test_android_app_configuration(self):
        content = (PROJECT / "app" / "build.gradle").read_text(encoding="utf-8")
        checks = {
            "applicationId": r"""applicationId\s+['"]com\.mainbasefoundation\.android['"]""",
            "namespace": r"""namespace\s+['"]com\.mainbasefoundation\.android['"]""",
            "compileSdk": r"compileSdk\s+36",
            "minSdk": r"minSdk\s+26",
            "targetSdk": r"targetSdk\s+36",
            "Java 17": r"sourceCompatibility\s+JavaVersion\.VERSION_17",
        }
        for label, pattern in checks.items():
            with self.subTest(configuration=label):
                self.assertRegex(content, pattern)

    def test_old_mobile_android_project_is_not_present(self):
        self.assertFalse((ROOT / "backend" / "mobile" / "android").exists())


if __name__ == "__main__":
    unittest.main()
