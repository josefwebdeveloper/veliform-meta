# Veliform — где что обновляется

Три слоя — не дублировать ops-детали, только ссылки.

```
Trello           → задачи (cards: что делать, статус)
Notion CEO       → реестр продуктов + лог активности (что произошло)
veliform.com/hq  → live-дашборд (org + Notion)
```

## Кто что пишет

| Событие | Trello | Notion CEO | Git / deploy |
|---------|--------|------------|--------------|
| Закрыли фичу в коде | card → ✅ Done list | CEO Update (cursor/git) | push → Action |
| SEO правка landing | card в SEO & Marketing | Update `veliform-landing` | push landing |
| Voice / Railway | Voice board list | Update `voice-agent` | push voice |
| «Что по компании?» | — | read only | — |

## Slugs (Notion)

| Repo | Workstream slug |
|------|-----------------|
| veliform-landing | `veliform-landing` |
| voice | `voice-agent` |
| agent-company | `agent-company` |
| meta | — |

## Trello

- Company / SEO: [`docs/TRELLO_VELIFORM.md`](TRELLO_VELIFORM.md)
- Voice: [`voice/docs/TRELLO_PROJECT.md`](../../voice/docs/TRELLO_PROJECT.md)
- Bootstrap: `meta/scripts/trello_bootstrap.py`
- Registry: `meta/ceo/trello.yaml`

## Cursor rules

- `meta/.cursor/rules/ceo-registry.mdc` — Notion CEO после работы
- `meta/.cursor/rules/trello-sync.mdc` — Trello после задач
- `voice/.cursor/rules/trello.mdc` — Voice board structure

## MCP

1. **Trello:** fill `TRELLO_API_KEY` + `TRELLO_TOKEN` in `.cursor/mcp.json` → Reload
2. **Notion:** Cursor → Settings → Tools & MCP → Notion → Connect

## Deprecated

ClickUp retired 2026-07-29. Old docs: `CLICKUP_VELIFORM.md`, `voice/docs/CLICKUP_PROJECT.md`.
