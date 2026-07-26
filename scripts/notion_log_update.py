#!/usr/bin/env python3
"""Post a CEO Update row to Notion (GitHub Actions / CLI).

Usage:
  NOTION_API_KEY=... NOTION_CEO_UPDATES_DATABASE_ID=... \\
    python notion_log_update.py \\
      --slug voice-agent \\
      --title "Deploy personal-server fix" \\
      --summary "Fixed FastAPI redirect type on /" \\
      --source git \\
      --link "https://github.com/josefwebdeveloper/voice-agent/commit/abc"

Optional:
  NOTION_CEO_PROJECTS_DATABASE_ID — also patches Last touch on the project page.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


def _request(method: str, path: str, body: dict | None = None) -> dict:
    api_key = os.environ["NOTION_API_KEY"]
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{NOTION_API}{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()[:500]
        raise SystemExit(f"Notion HTTP {exc.code}: {detail}") from exc


def _db_properties(db_id: str) -> dict:
    return _request("GET", f"/databases/{db_id}").get("properties") or {}


def _title_prop(properties: dict) -> str:
    for name, meta in properties.items():
        if meta.get("type") == "title":
            return name
    raise SystemExit("No title property in database")


def _find_project_page(projects_db: str, slug: str, slug_prop: str = "Slug") -> str | None:
    body = {
        "filter": {"property": slug_prop, "rich_text": {"equals": slug}},
        "page_size": 1,
    }
    results = _request("POST", f"/databases/{projects_db}/query", body).get("results") or []
    if not results:
        return None
    return results[0]["id"]


def _rich_text(content: str) -> dict:
    return {"rich_text": [{"text": {"content": content[:2000]}}]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True, help="CEO Projects slug, e.g. voice-agent")
    parser.add_argument("--title", required=True)
    parser.add_argument("--summary", default="")
    parser.add_argument("--source", default="git")
    parser.add_argument("--link", default="")
    args = parser.parse_args()

    updates_db = os.environ.get("NOTION_CEO_UPDATES_DATABASE_ID", "")
    projects_db = os.environ.get("NOTION_CEO_PROJECTS_DATABASE_ID", "")
    if not updates_db:
        raise SystemExit("NOTION_CEO_UPDATES_DATABASE_ID required")

    up_props = _db_properties(updates_db)
    title_prop = os.environ.get("NOTION_CEO_UPDATES_TITLE_PROPERTY") or _title_prop(up_props)
    summary_prop = os.environ.get("NOTION_CEO_UPDATES_SUMMARY_PROPERTY", "Summary")
    source_prop = os.environ.get("NOTION_CEO_UPDATES_SOURCE_PROPERTY", "Source")
    link_prop = os.environ.get("NOTION_CEO_UPDATES_LINK_PROPERTY", "Link")
    project_prop = os.environ.get("NOTION_CEO_UPDATES_PROJECT_PROPERTY", "Project")

    page_props: dict = {title_prop: {"title": [{"text": {"content": args.title[:2000]}}]}}
    if summary_prop in up_props and args.summary:
        page_props[summary_prop] = _rich_text(args.summary)
    if source_prop in up_props:
        page_props[source_prop] = {"select": {"name": args.source[:100]}}
    if link_prop in up_props and args.link:
        page_props[link_prop] = {"url": args.link[:2000]}

    project_page_id = None
    if projects_db:
        slug_prop = os.environ.get("NOTION_CEO_SLUG_PROPERTY", "Slug")
        project_page_id = _find_project_page(projects_db, args.slug, slug_prop)

    if project_prop in up_props and project_page_id:
        page_props[project_prop] = {"relation": [{"id": project_page_id}]}

    page = _request(
        "POST",
        "/pages",
        {"parent": {"database_id": updates_db}, "properties": page_props},
    )
    print(json.dumps({"ok": True, "page_id": page.get("id"), "url": page.get("url")}))

    if projects_db and project_page_id:
        touch_prop = os.environ.get("NOTION_CEO_LAST_TOUCH_PROPERTY", "Last touch")
        pr_props = _db_properties(projects_db)
        if touch_prop in pr_props and pr_props[touch_prop].get("type") == "date":
            from datetime import date

            _request(
                "PATCH",
                f"/pages/{project_page_id}",
                {"properties": {touch_prop: {"date": {"start": date.today().isoformat()}}}},
            )


if __name__ == "__main__":
    main()
