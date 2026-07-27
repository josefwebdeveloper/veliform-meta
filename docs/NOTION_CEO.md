# Notion — CEO Project Registry

Veliform **CEO** layer: all company products, stages, and an append-only activity log.

> Personal Tasks / Memory: [`NOTION_MEMORY.md`](../../voice/docs/NOTION_MEMORY.md) in voice repo.

## Hierarchy

```
Veliform (company page in Notion — optional)
├── Veliform Company Site     [Product]  slug: veliform-company  → veliform.com
│   └── veliform-landing repo [Workstream] slug: veliform-landing
├── Veliform Voice Agent      [Product]  slug: veliform-voice
│   └── voice repo            [Workstream] slug: voice-agent
└── … other products / ideas
```

## 1. Create CEO Projects database

1. Notion → **New database** → name: **CEO Projects**
2. Properties:

| Property | Type | Notes |
|----------|------|--------|
| **Name** | Title | |
| **Slug** | Text | e.g. `veliform-voice`, `voice-agent` |
| **Type** | Select | `Product`, `Workstream`, `Idea` |
| **Parent** | Relation → CEO Projects | self-relation |
| **Stage** | Select | `Discovery`, `Planning`, `Building`, `Live`, `Paused`, `Archived` |
| **Tier** | Select | `Active`, `Maintenance`, `Paused`, `Idea`, `Archived` |
| **Priority** | Select | `P0`, `P1`, `P2`, `P3` |
| **Next action** | Text | one line |
| **Last touch** | Date | updated by API / manual |
| **Repo URL** | URL | GitHub |
| **Prod URL** | URL | Railway / live site |
| **Docs** | URL | optional |

3. **Connections** → add integration **assistant** (same token as Tasks/Memory)
4. Copy database ID from URL → `NOTION_CEO_PROJECTS_DATABASE_ID`

### Views

- **CEO Dashboard** — filter Type = Product, sort Priority
- **Active workstreams** — Type = Workstream, Tier = Active
- **Stale** — Last touch is empty OR older than 30 days; Tier ≠ Archived
- **Ideas** — Type = Idea

### Bootstrap rows

| Name | Slug | Type | Stage | Tier | Parent |
|------|------|------|-------|------|--------|
| Veliform Company Site | veliform-company | Product | Live | Active | — |
| veliform-landing repo | veliform-landing | Workstream | Live | Active | Veliform Company Site |
| Veliform Voice Agent | veliform-voice | Product | Building | Active | — |
| voice-agent repo | voice-agent | Workstream | Building | Active | Veliform Voice Agent |

### Ideas backlog

Add rows with **Type = Idea**, **Tier = Idea**. Full spec in git: [`docs/ideas/AGENT_COMPANY_SAAS.md`](ideas/AGENT_COMPANY_SAAS.md).

| Name | Slug | Type | Stage | Tier | Priority | Next action |
|------|------|------|-------|------|----------|-------------|
| Agent Company SaaS | agent-company-saas | Idea → Building | Idea | P2 | Auth + Postgres v1; port Marketing Analyst |

Registry mirror: [`ceo/ideas.yaml`](../ceo/ideas.yaml).

## 2. Create CEO Updates database

| Property | Type | Notes |
|----------|------|--------|
| **Title** | Title | short headline |
| **Project** | Relation → CEO Projects | link to product or workstream |
| **Summary** | Text | what happened |
| **Source** | Select | `cursor`, `git`, `voice`, `telegram`, `manual`, `deploy` |
| **Link** | URL | commit, PR, page |

Copy ID → `NOTION_CEO_UPDATES_DATABASE_ID`

Optional Notion automation: when CEO Updates row created → set CEO Projects **Last touch** to today.

## 3. Env (personal-server Railway)

```
NOTION_API_KEY=...                    # same integration
NOTION_CEO_PROJECTS_DATABASE_ID=
NOTION_CEO_UPDATES_DATABASE_ID=
NOTION_CEO_SLUG_PROPERTY=Slug
NOTION_CEO_STAGE_PROPERTY=Stage
NOTION_CEO_TIER_PROPERTY=Tier
NOTION_CEO_NEXT_ACTION_PROPERTY=Next action
NOTION_CEO_LAST_TOUCH_PROPERTY=Last touch
NOTION_CEO_UPDATES_TITLE_PROPERTY=Title
NOTION_CEO_UPDATES_SUMMARY_PROPERTY=Summary
NOTION_CEO_UPDATES_SOURCE_PROPERTY=Source
NOTION_CEO_UPDATES_LINK_PROPERTY=Link
NOTION_CEO_UPDATES_PROJECT_PROPERTY=Project
```

## 4. How updates arrive

| Channel | Source value |
|---------|----------------|
| Git push to main | `git` (GitHub Action) |
| Personal assistant / voice | `voice` |
| Telegram `/ceo` | `telegram` |
| Cursor end-of-session | `cursor` (manual via Notion or future MCP) |
| You in Notion | `manual` |

## 5. Telegram (personal-server)

- `/ceo` or `/ceo status` — product stages + last touch (owner chat only)
- Voice: «что по компании?» → tool `get_ceo_status`

## 6. GitHub Action secrets (voice repo)

- `NOTION_API_KEY`
- `NOTION_CEO_UPDATES_DATABASE_ID`
- `NOTION_CEO_PROJECTS_DATABASE_ID` (optional, for last-touch patch)

Workstream slug for voice repo: **`voice-agent`** (see `ceo/projects.yaml` in meta repo).
