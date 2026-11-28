"""Fetch public technology feeds and produce a conservative Markdown digest."""
from __future__ import annotations
import argparse
import datetime as dt
import email.utils
import re
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_FEEDS = (
    ("WordPress News", "https://wordpress.org/news/feed/"),
    ("GitHub Changelog", "https://github.blog/changelog/feed/"),
    ("Python Insider", "https://blog.python.org/feeds/posts/default"),
)

@dataclass(frozen=True)
class Entry:
    source: str
    title: str
    link: str
    published: str
    summary: str

def clean(value: str, limit: int = 700) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", value).strip()[:limit]

def normalized_date(value: str) -> str:
    if not value:
        return "Date not supplied by source"
    try:
        parsed = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        try:
            parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        except (TypeError, ValueError, OverflowError):
            return clean(value, 80)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc).isoformat()

def local_text(node: ET.Element, names: tuple[str, ...]) -> str:
    for child in node:
        if child.tag.rsplit("}", 1)[-1] in names:
            text = "".join(child.itertext()).strip()
            if text:
                return text
    return ""

def parse_feed(source: str, xml_bytes: bytes) -> list[Entry]:
    """Parse common RSS and Atom feeds without third-party dependencies."""
    root = ET.fromstring(xml_bytes)
    nodes = root.findall(".//item")
    if not nodes:
        nodes = [n for n in root.iter() if n.tag.rsplit("}", 1)[-1] == "entry"]
    result = []
    for node in nodes:
        title = local_text(node, ("title",))
        link = local_text(node, ("link",))
        if not link:
            for child in node:
                if child.tag.rsplit("}", 1)[-1] == "link":
                    link = child.attrib.get("href", "")
                    if link:
                        break
        published = local_text(node, ("pubDate", "published", "updated"))
        summary = local_text(node, ("description", "summary", "encoded", "content"))
        if title and link and urlparse(link).scheme in ("https", "http"):
            result.append(Entry(source, clean(title, 240), link, normalized_date(published), clean(summary)))
    return result

def fetch_feed(source: str, url: str, timeout: int = 15) -> list[Entry]:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("Feed URL must use HTTPS")
    request = urllib.request.Request(url, headers={"User-Agent": "SUPREMESETUHUB-TechIntelligence/0.1 (read-only public feed monitor)"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        payload = response.read(2_000_000)
    return parse_feed(source, payload)

def render_report(entries: list[Entry], errors: list[tuple[str, str]]) -> str:
    lines = [
        "# SUPREMESETUHUB — Technology Intelligence Digest", "",
        f"- Generated: {dt.datetime.now(dt.timezone.utc).isoformat()}",
        "- Mode: READ-ONLY",
        "- Scope: configured public feeds only; not an exhaustive scan of the internet.", "",
        "## Decision guidance", "",
        "Discovery does not prove an update is safe or necessary. This report does not authorize a production update. Verify official release notes, compatibility, security, costs, licensing, privacy, staging tests, backup and rollback.", "",
        "## Findings", ""
    ]
    if not entries:
        lines.append("No feed entries were retrieved successfully in this run.")
    for entry in entries:
        lines.extend([
            f"### {entry.title}", f"- Source: {entry.source}",
            f"- Published: {entry.published}", f"- Evidence: {entry.link}",
            f"- Summary: {entry.summary or 'No summary supplied; open the source for details.'}",
            "- Benefits: NOT ASSESSED automatically; verify against official release notes and the use case.",
            "- Risks/losses: NOT ASSESSED automatically; check breaking changes, vulnerabilities, costs and compatibility.",
            "- Recommendation: REVIEW; this report does not authorize a production update.", ""
        ])
    if errors:
        lines.extend(["## Feed errors", ""])
        lines.extend([f"- {source}: {message}" for source, message in errors])
        lines.append("")
    lines.extend([
        "## Human approval checklist", "",
        "- [ ] Confirm official source and affected installed version.",
        "- [ ] Check security advisories, breaking changes, support window, license and regional availability.",
        "- [ ] Estimate benefits, implementation effort, recurring costs and risks.",
        "- [ ] Test in staging and run automated tests.",
        "- [ ] Confirm a recent backup and tested rollback/restore path.",
        "- [ ] Approve a reviewed PR before production rollout.", ""
    ])
    return "\n".join(lines)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="artifacts/technology-intelligence.md")
    args = parser.parse_args()
    entries, errors = [], []
    for source, url in DEFAULT_FEEDS:
        try:
            entries.extend(fetch_feed(source, url))
        except (OSError, ValueError, RuntimeError, ET.ParseError) as exc:
            errors.append((source, clean(str(exc), 240)))
    unique = {}
    for entry in entries:
        unique.setdefault(entry.link.rstrip("/"), entry)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(list(unique.values()), errors) + "\n", encoding="utf-8")
    print(f"Wrote {output}: {len(unique)} findings, {len(errors)} feed errors.")
    return 1 if len(errors) == len(DEFAULT_FEEDS) else 0

if __name__ == "__main__":
    raise SystemExit(main())
