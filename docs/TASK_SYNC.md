# Veliform — где что обновляется

Три слоя — не дублировать ops-детали, только ссылки.

```
Linear           → задачи (issues: что делать, статус)
Notion CEO       → реестр продуктов + лог активности (что произошло)
veliform.com/hq  → live-дашборд (org + Notion)
```

## Кто что пишет

| Событие | Linear | Notion CEO | Git / deploy |
|---------|--------|------------|--------------|
| Закрыли фичу в коде | issue → Done | CEO Update (cursor/git) | push → Action |
| SEO правка landing | Company + `seo` | Update `veliform-landing` | push landing |
| Voice / Railway | Voice project | Update `voice-agent` | push voice |
| «Что по компании?» | — | read only | — |

## Slugs (Notion)

| Repo | Workstream slug |
|------|-----------------|
| veliform-landing | `veliform-landing` |
| voice | `voice-agent` |
| agent-company | `agent-company` |
| meta | — |

## Linear

- Guide: [`docs/LINEAR_VELIFORM.md`](LINEAR_VELIFORM.md)
- Registry: `meta/ceo/linear.yaml`
- Cursor rule: `meta/.cursor/rules/linear-sync.mdc`

## Cursor rules

- `meta/.cursor/rules/ceo-registry.mdc` — Notion CEO после работы
- `meta/.cursor/rules/linear-sync.mdc` — Linear после задач

## MCP

1. **Linear:** Settings → Tools & MCP → Linear → Connect
2. **Notion:** Cursor → Settings → Tools & MCP → Notion → Connect

## Deprecated

- **Trello** retired as primary tracker 2026-08-08. Boards kept as archive. Docs: `TRELLO_VELIFORM.md`, `voice/docs/TRELLO_PROJECT.md`.
- ClickUp retired 2026-07-29. Old docs: `CLICKUP_VELIFORM.md`, `voice/docs/CLICKUP_PROJECT.md`.
