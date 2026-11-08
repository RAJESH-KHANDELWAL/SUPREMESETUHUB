import unittest
import xml.etree.ElementTree as ET
from backend.tech_intelligence.scan_sources import parse_feed, render_report

class TechIntelligenceTests(unittest.TestCase):
    def test_parses_rss_item(self):
        xml = b"<?xml version='1.0'?><rss><channel><item><title>Release 1.2</title><link>https://example.com/release</link><pubDate>Mon, 12 Oct 2026 12:00:00 GMT</pubDate><description>Fixes &amp; improvements</description></item></channel></rss>"
        entries = parse_feed("Example", xml)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].title, "Release 1.2")
        self.assertEqual(entries[0].link, "https://example.com/release")
        self.assertIn("Fixes", entries[0].summary)

    def test_report_is_read_only_and_cautious(self):
        report = render_report([], [("Example", "timeout")])
        self.assertIn("READ-ONLY", report)
        self.assertIn("does not authorize a production update", report)
        self.assertIn("Feed errors", report)

    def test_invalid_xml_raises(self):
        with self.assertRaises(ET.ParseError):
            parse_feed("Broken", b"<rss>")

if __name__ == "__main__":
    unittest.main()
