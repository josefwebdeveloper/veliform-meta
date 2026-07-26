# Veliform — где что обновляется

Три слоя — не дублировать ops-детали, только ссылки.

```
ClickUp          → задачи (что делать, статус, приоритет)
Notion CEO       → реестр продуктов + лог активности (что произошло)
veliform.com/hq  → live-дашборд (org + Notion)
```

## Кто что пишет

| Событие | ClickUp | Notion CEO | Git / deploy |
|---------|---------|------------|--------------|
| Закрыли фичу в коде | задача → Done | CEO Update (cursor/git) | push → Action |
| SEO правка landing | задача в Marketing list | Update `veliform-landing` | push landing |
| Voice / Railway | list по сервису | Update `voice-agent` | push voice |
| «Что по компании?» | — | read only | — |

## Slugs (Notion)

| Repo | Workstream slug |
|------|-----------------|
| veliform-landing | `veliform-landing` |
| voice | `voice-agent` |
| meta | — |

## ClickUp

- Voice: [`voice/docs/CLICKUP_PROJECT.md`](../../voice/docs/CLICKUP_PROJECT.md)
- Company / SEO: [`docs/CLICKUP_VELIFORM.md`](CLICKUP_VELIFORM.md)

## Cursor rules

- `meta/.cursor/rules/ceo-registry.mdc` — Notion CEO после работы
- `meta/.cursor/rules/clickup-sync.mdc` — ClickUp после задач
- `meta/.cursor/rules/seo-steward.mdc` — SEO + ClickUp Marketing list
- `voice/.cursor/rules/clickup.mdc` — Voice ClickUp structure

## MCP

1. **ClickUp:** Cursor → Settings → Tools & MCP → ClickUp → **Connect** (OAuth)
2. Конфиг: `meta/.cursor/mcp.json`, `voice/.cursor/mcp.json`
3. После Connect: «ClickUp подключён» → агент создаст/обновит lists
