#!/usr/bin/env python3
"""Sync business presentation deliverables to Notion CEO + Trello (Company HQ list)."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

META_ROOT = Path(__file__).resolve().parents[1]
COMMIT = os.environ.get("GITHUB_SHA", "main")[:7]
GITHUB_LINK = os.environ.get(
    "PRESENTATION_LINK",
    "https://github.com/josefwebdeveloper/veliform-meta/blob/main/"
    "docs/presentations/VELIFORM_BUSINESS_PRESENTATION_2026-07-28.md",
)
sys.path.insert(0, str(META_ROOT / "scripts"))
from trello_client import create_card  # noqa: E402

TITLE = "Business presentation: goal, profit model, KPIs (2026-07-28)"
SUMMARY = (
    "Added 18-slide Marp deck (EN + RU) with numbers and dates: 11 agents, "
    "Voice Launchpad 5-min promise, WeOffice MVP targets (1 partner or 10 beta orgs), "
    "Railway cost thresholds ($5/$8/$15), Dec 2026 KPI $1K MRR. "
    "Exports: PDF + PPTX in meta/docs/presentations/."
)


def _trello_create_card() -> dict:
    list_id = os.environ.get("TRELLO_COMPANY_HQ_LIST_ID", "").strip()
    if not list_id:
        raise RuntimeError("TRELLO_COMPANY_HQ_LIST_ID is not set")
    return create_card(
        list_id,
        name=TITLE,
        desc=(
            f"{SUMMARY}\n\n"
            f"- EN deck: {GITHUB_LINK}\n"
            f"- RU deck: veliform-meta/docs/presentations/"
            f"VELIFORM_BUSINESS_PRESENTATION_2026-07-28_RU.md\n"
            f"- Commit: {COMMIT}\n"
        ),
    )


def main() -> int:
    results: dict[str, str] = {}

    notion_script = META_ROOT / "scripts" / "notion_log_update.py"
    env = os.environ.copy()
    env.setdefault("CEO_TITLE", TITLE)
    env.setdefault("CEO_SUMMARY", SUMMARY)
    env.setdefault("CEO_LINK", GITHUB_LINK)

    if env.get("NOTION_API_KEY") and env.get("NOTION_CEO_UPDATES_DATABASE_ID"):
        proc = subprocess.run(
            [
                sys.executable,
                str(notion_script),
                "--slug",
                "veliform-landing",
                "--title",
                TITLE,
                "--summary",
                SUMMARY,
                "--source",
                "cursor",
                "--link",
                GITHUB_LINK,
            ],
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        results["notion"] = proc.stdout.strip() or proc.stderr.strip() or f"exit {proc.returncode}"
    else:
        results["notion"] = "skipped — NOTION_API_KEY or NOTION_CEO_UPDATES_DATABASE_ID not set"

    if os.environ.get("TRELLO_API_KEY") and os.environ.get("TRELLO_TOKEN"):
        try:
            card = _trello_create_card()
            results["trello"] = json.dumps({"ok": True, "id": card.get("id"), "url": card.get("url")})
        except Exception as exc:
            results["trello"] = str(exc)[:300]
    else:
        results["trello"] = "skipped — TRELLO_API_KEY / TRELLO_TOKEN not set"

    print(json.dumps(results, indent=2))
    synced = any("ok" in v for v in results.values())
    return 0 if synced else 0  # non-fatal when secrets unavailable locally


if __name__ == "__main__":
    raise SystemExit(main())
