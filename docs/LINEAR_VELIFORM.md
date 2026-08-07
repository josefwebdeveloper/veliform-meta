# Linear — Veliform (primary task tracker)

> Cutover from Trello **2026-08-08**. Archive docs: [`TRELLO_VELIFORM.md`](TRELLO_VELIFORM.md).

## Three-layer ops

| Layer | System |
|-------|--------|
| Tasks | **Linear** (issues / projects) |
| Product registry + activity | Notion CEO |
| Dashboard | HQ (`veliform.com/hq`) |

## Workspace

- URL: https://linear.app/veliform
- Team: **Veliform** (`VEL`)
- Registry: [`ceo/linear.yaml`](../ceo/linear.yaml)

### Projects

| Project | Was Trello board |
|---------|------------------|
| [Veliform Voice](https://linear.app/veliform/project/veliform-voice-30fb67766210) | Veliform Voice |
| [Veliform Company](https://linear.app/veliform/project/veliform-company-e14fd4faeace) | Veliform Company |

### Labels (ex-lists)

| Label | Was Trello list |
|-------|-----------------|
| `ops` | 🔧 Ops & Integrations |
| `personal` | 👤 Personal Line |
| `business` | 🏢 Business Platform |
| `seo` | 🌐 SEO & Marketing |
| `hq` | 🏗 Company HQ |

Statuses: **Backlog** · **Todo** · **In Progress** · **Done**

## Cursor MCP

Official remote MCP (already in `~/.cursor/mcp.json`):

```json
"Linear": { "url": "https://mcp.linear.app/mcp" }
```

Settings → Tools & MCP → **Linear** → Connect (OAuth) → Reload if needed.

Agent workflow rule: `meta/.cursor/rules/linear-sync.mdc`.

## Automation (GitHub Actions)

Marketing / Finance agents prefer Linear when `LINEAR_API_KEY` is set on `veliform-landing`; otherwise they fall back to Trello list IDs.

```bash
# Create key: https://linear.app/veliform/settings/account/security
gh secret set LINEAR_API_KEY --repo josefwebdeveloper/veliform-landing
# Optional overrides (defaults live in config/*-agent.json):
gh secret set LINEAR_TEAM_ID --repo josefwebdeveloper/veliform-landing
gh secret set LINEAR_PROJECT_ID --repo josefwebdeveloper/veliform-landing
gh secret set LINEAR_LABEL_IDS --repo josefwebdeveloper/veliform-landing
```

Tracking issue: [VEL-38](https://linear.app/veliform/issue/VEL-38/wire-marketingfinance-github-actions-linear-api)

## Migration status

- [x] Linear MCP authenticated
- [x] Projects + labels created
- [x] Open Trello cards imported (Voice + Company); Done history preserved
- [x] Registry `ceo/linear.yaml` + docs / Cursor rules
- [x] Agent configs + Linear client (API key secret still required for scheduled runs)
- [ ] Archive Trello boards as read-only when comfortable
