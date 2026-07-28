#!/usr/bin/env python3
"""Sync business presentation deliverables to Notion CEO + ClickUp (Company HQ list)."""

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
CLICKUP_LIST_ID = "901819936119"  # Company HQ
CLICKUP_API = "https://api.clickup.com/api/v2"

TITLE = "Business presentation: goal, profit model, KPIs (2026-07-28)"
SUMMARY = (
    "Added 18-slide Marp deck (EN + RU) with numbers and dates: 11 agents, "
    "Voice Launchpad 5-min promise, WeOffice MVP targets (1 partner or 10 beta orgs), "
    "Railway cost thresholds ($5/$8/$15), Dec 2026 KPI $1K MRR. "
    "Exports: PDF + PPTX in meta/docs/presentations/."
)


def _clickup_create_task(token: str) -> dict:
    body = {
        "name": TITLE,
        "description": (
            f"{SUMMARY}\n\n"
            f"- EN deck: {GITHUB_LINK}\n"
            f"- RU deck: veliform-meta/docs/presentations/"
            f"VELIFORM_BUSINESS_PRESENTATION_2026-07-28_RU.md\n"
            f"- Commit: {COMMIT}\n"
        ),
        "status": "complete",
        "tags": ["ceo-steward", "presentation"],
    }
    req = urllib.request.Request(
        f"{CLICKUP_API}/list/{CLICKUP_LIST_ID}/task",
        data=json.dumps(body).encode(),
        headers={
            "Authorization": token,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


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

    token = env.get("CLICKUP_API_TOKEN", "").strip()
    if token:
        try:
            task = _clickup_create_task(token)
            results["clickup"] = json.dumps({"ok": True, "id": task.get("id"), "url": task.get("url")})
        except urllib.error.HTTPError as exc:
            results["clickup"] = f"HTTP {exc.code}: {exc.read().decode()[:300]}"
    else:
        results["clickup"] = "skipped — CLICKUP_API_TOKEN not set"

    print(json.dumps(results, indent=2))
    synced = any("ok" in v for v in results.values())
    return 0 if synced else 0  # non-fatal when secrets unavailable locally


if __name__ == "__main__":
    raise SystemExit(main())
