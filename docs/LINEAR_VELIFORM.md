# Linear — Veliform (replacing Trello)

> **Primary task tracker** (migrating from Trello 2026-08-08). Trello docs kept until cutover: [`TRELLO_VELIFORM.md`](TRELLO_VELIFORM.md).

## Why

Same three-layer ops, better agent UX in Cursor:

| Layer | System |
|-------|--------|
| Tasks | **Linear** (issues / projects) |
| Product registry + activity | Notion CEO |
| Dashboard | HQ (`veliform.com/hq`) |

## Cursor MCP

Official remote MCP (preferred over Zapier/GitLens for this workspace):

```json
"Linear": { "url": "https://mcp.linear.app/mcp" }
```

1. Settings → Cursor Settings → **Tools & MCP** → connect **Linear** (OAuth).
2. Or open: [Linear MCP install](https://linear.app/docs/mcp).
3. Reload Window. Agent should see Linear tools (list teams, create issue, etc.).

Zapier Linear actions are also enabled but require a separate Zapier↔Linear auth if used as fallback.

## Target structure (mirror of Trello)

### Team: **Veliform Voice**

| Linear status / label | Was Trello list |
|----------------------|-----------------|
| Backlog | 📋 Backlog |
| In Progress | 🚧 In Progress |
| Done | ✅ Done |
| Label `ops` | 🔧 Ops & Integrations |
| Label `business` | 🏢 Business Platform |
| Label `personal` | 👤 Personal Line |

### Team: **Veliform Company** (or Projects under one team)

| Project / label | Was Trello list |
|-----------------|-----------------|
| SEO & Marketing | 🌐 SEO & Marketing |
| Company HQ | 🏗 Company HQ |
| Backlog | 📋 Backlog |

Automation agents (Marketing / Finance) will post Linear issues instead of Trello cards once `LINEAR_*` secrets replace `TRELLO_*`.

## Migration checklist

- [ ] Linear MCP authenticated in Cursor
- [ ] Create teams / projects / labels above
- [ ] Import open Trello cards (skip pure Done archive or mark Done)
- [ ] Registry: `meta/ceo/linear.yaml`
- [ ] Update `AGENTS.md` three-layer ops → Linear
- [ ] Update `TASK_SYNC.md`, Cursor rules (`trello-sync` → `linear-sync`)
- [ ] Marketing / Finance GitHub Actions → Linear API
- [ ] Deprecate Trello MCP usage (keep boards read-only archive)

## Open cards inventory (source)

See Trello boards at cutover; Voice board had ~27 cards (Backlog / In Progress / Ops / Personal / Done). Company board: SEO + HQ + Backlog lists.
