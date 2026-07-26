# ClickUp — Veliform Company (landing, SEO, HQ)

> Workspace: Joseph Shain (`90182909934`). Voice lists — [`voice/docs/CLICKUP_PROJECT.md`](../../voice/docs/CLICKUP_PROJECT.md).

## Структура (live)

| Уровень | Название | ID / URL |
|---------|----------|----------|
| Workspace | Joseph Shain | `90182909934` |
| Space | `VeliForm` | `901812090844` |
| Folder | `Company Site` | [folder](https://app.clickup.com/90182909934/v/f/901815639926) · `901815639926` |
| List | `🌐 SEO & Marketing` | [list](https://app.clickup.com/90182909934/v/l/li/901819936121) · `901819936121` |
| List | `🏗 Company HQ` | [list](https://app.clickup.com/90182909934/v/l/li/901819936119) · `901819936119` |
| List | `📋 Backlog` | [list](https://app.clickup.com/90182909934/v/l/li/901819936120) · `901819936120` |

Voice lists — [`voice/docs/CLICKUP_PROJECT.md`](../../voice/docs/CLICKUP_PROJECT.md) (folder `Voice Agents` · `901815577245`).

## Custom fields (Folder level)

| Field | Type | Use |
|-------|------|-----|
| Repo | dropdown | `veliform-landing`, `meta` |
| Workstream slug | text | `veliform-landing` |
| Prod URL | URL | https://veliform.com |

## SEO Agent — типичные задачи

Создавать/закрывать в `🌐 SEO & Marketing`:

- Sitemap / robots.txt update
- Meta tags / OG / JSON-LD on key pages
- `.well-known/agent-skills` index
- Core Web Vitals / Lighthouse follow-up
- New industry page or blog (when added)

## Marketing Analyst

Scheduled GitHub Actions writes to `🌐 SEO & Marketing` through the ClickUp REST
API. It creates at most one daily anomaly task or three weekly opportunity tasks,
with a deterministic fingerprint to prevent duplicates. Interactive Cursor work
continues to use ClickUp MCP.

## HQ Agent — типичные задачи

List `🏗 Company HQ`:

- Notion CEO sync issues
- New agent in `ceo/org.yaml`
- Vercel env / auth fixes

## Связь с Notion

- **Не** дублировать CEO Updates в ClickUp descriptions
- В задаче: slug `veliform-landing`, ссылка на commit
- Stage/Tier — только в Notion CEO Projects
