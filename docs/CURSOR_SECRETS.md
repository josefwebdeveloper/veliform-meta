# Cursor secrets (Veliform workspace)

## Local IDE (done automatically)

File: **`veliform/.cursor/.env`** (gitignored, mode 600)

Regenerate from Railway:

```bash
./scripts/sync-cursor-secrets.sh
```

MCP Trello reads this via `envFile` in `.cursor/mcp.json`.

After sync: **Cursor → Reload Window**.

## Cloud Agents (manual — no CLI)

Dashboard: [cursor.com/dashboard/cloud-agents](https://cursor.com/dashboard/cloud-agents) → your environment → **Secrets**

Paste **name = value** pairs from `.cursor/.env` (open locally — never commit):

| Secret | Source |
|--------|--------|
| `NOTION_API_KEY` | Railway personal-server |
| `NOTION_TASKS_DATABASE_ID` | Railway |
| `NOTION_MEMORY_DATABASE_ID` | Railway |
| `NOTION_CEO_PROJECTS_DATABASE_ID` | Railway |
| `NOTION_CEO_UPDATES_DATABASE_ID` | Railway |
| `TELEGRAM_BOT_TOKEN` | Railway |
| `TELEGRAM_CHAT_ID` | Railway |
| `TRELLO_API_KEY` | Trello Power-Up / shell |
| `TRELLO_TOKEN` | Trello |
| `GEMINI_API_KEY` | GitHub secret or [Google AI Studio](https://aistudio.google.com/apikey) |

Optional non-secret config (can be Environment Variable, not Runtime Secret):

- `NOTION_*_PROPERTY` defaults
- `TELEGRAM_ENABLED=true`
- `TRELLO_MARKETING_LIST_ID`, `TRELLO_COMPANY_HQ_LIST_ID`

Notion MCP plugin uses OAuth (`mcp_auth`) — separate from `NOTION_API_KEY`.
