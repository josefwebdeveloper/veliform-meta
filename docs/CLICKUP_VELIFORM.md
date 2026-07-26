# ClickUp — Veliform Company (landing, SEO, HQ)

> Workspace: Joseph Shain (`90182909934`). Voice lists — [`voice/docs/CLICKUP_PROJECT.md`](../../voice/docs/CLICKUP_PROJECT.md).

## Предлагаемая структура (создать через MCP после OAuth)

| Уровень | Название | Назначение |
|---------|----------|------------|
| Space | `Veliform` *(или Folder в Team Space)* | Вся компания |
| Folder | `Company Site` | veliform.com, meta, HQ |
| List | `🌐 SEO & Marketing` | sitemap, meta, JSON-LD, agent-skills, content |
| List | `🏗 Company HQ` | /hq dashboard, org.yaml, Notion integration |
| List | `📋 Backlog` | идеи по сайту |

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

## HQ Agent — типичные задачи

List `🏗 Company HQ`:

- Notion CEO sync issues
- New agent in `ceo/org.yaml`
- Vercel env / auth fixes

## Связь с Notion

- **Не** дублировать CEO Updates в ClickUp descriptions
- В задаче: slug `veliform-landing`, ссылка на commit
- Stage/Tier — только в Notion CEO Projects
