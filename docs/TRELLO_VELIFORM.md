# Trello — Veliform Company (landing, SEO, HQ)

> **Primary task tracker** (migrated from ClickUp 2026-07-29). Voice board — [`voice/docs/TRELLO_PROJECT.md`](../../voice/docs/TRELLO_PROJECT.md).

## Setup (one time)

1. **Credentials:** https://trello.com/power-ups/admin → API Key + Token (`read,write`).
2. **Local env** (do not commit):
   ```bash
   export TRELLO_API_KEY=...
   export TRELLO_TOKEN=...
   ```
3. **Bootstrap boards + lists + seed cards:**
   ```bash
   cd meta
   pip install pyyaml requests
   python scripts/trello_bootstrap.py
   ```
   Writes IDs to `ceo/trello.yaml` and patches `veliform-landing/config/*-agent.json`.
4. **GitHub secrets** (`veliform-landing` repo):
   ```bash
   gh secret set TRELLO_API_KEY --repo josefwebdeveloper/veliform-landing
   gh secret set TRELLO_TOKEN --repo josefwebdeveloper/veliform-landing
   gh secret set TRELLO_MARKETING_LIST_ID --repo josefwebdeveloper/veliform-landing
   gh secret set TRELLO_COMPANY_HQ_LIST_ID --repo josefwebdeveloper/veliform-landing
   ```
5. **Cursor MCP:** fill `TRELLO_API_KEY` / `TRELLO_TOKEN` in `meta/.cursor/mcp.json` and `voice/.cursor/mcp.json` → Reload Window.

## Boards (after bootstrap)

| Board | Lists |
|-------|--------|
| **Veliform Company** | 🌐 SEO & Marketing · 🏗 Company HQ · 📋 Backlog |
| **Veliform Voice** | ✅ Done · 🚧 In Progress · 📋 Backlog · 🔧 Ops · 🏢 Business · 👤 Personal |

Registry with list IDs: [`ceo/trello.yaml`](../ceo/trello.yaml)

## Automation

| Agent | Trello list | Env |
|-------|-------------|-----|
| Marketing Analyst | SEO & Marketing | `TRELLO_MARKETING_LIST_ID` |
| Finance Agent | Company HQ | `TRELLO_COMPANY_HQ_LIST_ID` |

## Cursor workflow

After finishing work → create/move **card** on the right list (via Trello MCP). CEO Update in Notion when product/deploy changed.

## Deprecated

ClickUp docs kept for reference only: [`CLICKUP_VELIFORM.md`](CLICKUP_VELIFORM.md)
