"""Run a public-source freelancer research query from GitHub Actions.

Credentials are read only from environment variables. Results are leads, not verified
jobs or payment guarantees. Never commit provider credentials or private personal data.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from backend.freelancer.global_freelancer_ecosystem.research_engine import (
    CATEGORIES,
    MARKETS,
    FreelancerResearchEngine,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search public freelance opportunities.")
    parser.add_argument("--query", required=True, help="Skill, service, or opportunity")
    parser.add_argument("--market", choices=sorted(MARKETS), default="bharat")
    parser.add_argument("--category", choices=sorted(CATEGORIES), default="freelance_work")
    parser.add_argument("--limit", type=int, choices=range(1, 21), default=10)
    parser.add_argument("--output-dir", default="research-output")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    result = FreelancerResearchEngine().search(
        query=args.query,
        market=args.market,
        category=args.category,
        limit=args.limit,
    )
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "requested_by": "GitHub Actions",
        "query": args.query,
        "market": args.market,
        "category": args.category,
        "result": result,
    }
    json_path = output_dir / "freelancer-research.json"
    markdown_path = output_dir / "freelancer-research.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# GLOBAL FREELANCER ECOSYSTEM — Research Results",
        "",
        f"- **Generated (UTC):** {report['generated_at']}",
        f"- **Query:** {args.query}",
        f"- **Market:** {args.market}",
        f"- **Category:** {args.category}",
        f"- **Status:** {result.get('status', 'UNKNOWN')}",
        f"- **Results:** {result.get('count', 0)}",
        "",
        "> Search results are unverified leads. Confirm the original listing, employer/client,",
        "> scope, and payment terms independently. Never pay a fee to unlock a job or share OTPs.",
        "",
    ]
    for index, item in enumerate(result.get("results", []), start=1):
        title = str(item.get("title", "Untitled listing")).replace("\n", " ")
        description = str(item.get("description", "")).replace("\n", " ")
        url = str(item.get("url", ""))
        lines.extend([
            f"## {index}. {title}",
            "",
            f"- **Source:** {url}",
            f"- **Domain:** {item.get('domain', '')}",
            f"- **Relevance (keyword overlap, not trust):** {item.get('relevance_score', 0)}/100",
            f"- **Verification:** {item.get('verification_status', 'UNVERIFIED_PUBLIC_LISTING')}",
            "",
            description,
            "",
        ])
    if not result.get("results"):
        lines.extend([
            "No results were returned. Check provider configuration, API quota, query, and workflow logs.",
            "",
        ])
    markdown_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"JSON report: {json_path}")
    print(f"Markdown report: {markdown_path}")
    print(f"Search status: {result.get('status', 'UNKNOWN')}")
    print(f"Result count: {result.get('count', 0)}")

    if result.get("status") == "SEARCH_PROVIDER_CONFIGURATION_REQUIRED":
        print(
            "Configure BRAVE_SEARCH_API_KEY or both GOOGLE_CSE_API_KEY and GOOGLE_CSE_CX "
            "as GitHub Actions repository secrets.",
            file=sys.stderr,
        )
        return 2
    if result.get("status") == "PROVIDER_ERROR":
        print("Search provider failed. Inspect provider quota and workflow logs.", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
