# Veliform Company HQ

Live internal dashboard: **https://veliform.com/hq**

## What it shows

- Org structure (departments, people, AI agents)
- Agent roster with focus, tools, and status
- Product/workstream stages from Notion CEO Projects
- Activity feed from Notion CEO Updates (git, voice, cursor, manual)

## Source of truth

| Layer | File / system |
|-------|----------------|
| Static org | [`ceo/org.yaml`](../ceo/org.yaml) |
| Live registry | Notion CEO Projects + CEO Updates |
| Products/repos | [`ceo/projects.yaml`](../ceo/projects.yaml) |

Build sync: `veliform-landing/scripts/sync-org.mjs` reads `org.yaml` → `data/org.generated.ts`.

## Access

- **URL:** `/hq` on veliform.com
- **Auth:** HTTP Basic Auth via Vercel env `HQ_PASSWORD`
- **robots.txt:** `Disallow: /hq`

## Vercel environment variables

Set on **veliform-landing** project:

| Variable | Purpose |
|----------|---------|
| `HQ_PASSWORD` | Basic auth password for `/hq` and `/api/hq/*` |
| `NOTION_API_KEY` | Integration **veliform** (same as GitHub Actions) |
| `NOTION_CEO_PROJECTS_DATABASE_ID` | `d88ea5e589a24669bcf5822dfcfbca2c` |
| `NOTION_CEO_UPDATES_DATABASE_ID` | `ffd99e25f7c146e688d7e624f3dca92e` |

## Local dev

```bash
cd veliform-landing
cp .env.example .env.local
# fill HQ_PASSWORD + NOTION_*
npm run dev
# open http://localhost:5173/hq — browser will prompt for password
```

For API routes locally, use `vercel dev` (Vite alone does not serve `/api/hq`).

## Edit agents or departments

1. Edit `meta/ceo/org.yaml`
2. Rebuild landing (`npm run build` runs sync-org automatically)
3. Deploy veliform-landing

Live Stage/Tier/Last touch come from Notion — no rebuild needed for those.
