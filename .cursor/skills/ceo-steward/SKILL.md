# CEO Steward — Veliform project registry

Use when the user asks about company projects, stages, stale projects, or logging work to CEO Notion.

## Registry location

- **Notion**: CEO Projects + CEO Updates (setup: `docs/NOTION_CEO.md` in veliform-meta)
- **Slugs**: `ceo/projects.yaml` (repos) + `ceo/ideas.yaml` (future products)
- **Ideas docs**: `docs/ideas/*.md`

## Slugs (bootstrap)

| Slug | Name | Type |
|------|------|------|
| `veliform-voice` | Veliform Voice Agent | Product |
| `voice-agent` | voice-agent repo | Workstream |
| `agent-company-saas` | Agent Company SaaS | Idea |

## Log an update (template)

```
Title: [what changed]
Project slug: voice-agent
Source: cursor
Summary: [1-3 sentences, include next step if known]
Link: [commit URL or PR if any]
```

## Voice / personal-server tools

When CEO Notion env is set on personal-server:

- `get_ceo_status` — all products with Stage, Tier, Last touch, Next action
- `log_ceo_update` — append CEO Updates row
- `list_stale_projects` — projects not touched in N days

## End of session

Always offer to record a CEO Update after non-trivial changes in any Veliform repo.
