# Veliform presentations

Markdown slide decks (Marp-compatible). Open in VS Code/Cursor with the [Marp extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode), or export via CLI:

```bash
npx @marp-team/marp-cli meta/docs/presentations/VELIFORM_BUSINESS_PRESENTATION_2026-07-28.md -o veliform-business-2026-07-28.pdf
npx @marp-team/marp-cli meta/docs/presentations/VELIFORM_BUSINESS_PRESENTATION_2026-07-28.md -o veliform-business-2026-07-28.pptx --pptx
```

Sync to Notion CEO + ClickUp (requires env):

```bash
cd meta
export NOTION_API_KEY=... NOTION_CEO_UPDATES_DATABASE_ID=... NOTION_CEO_PROJECTS_DATABASE_ID=...
export CLICKUP_API_TOKEN=...
python3 scripts/sync_presentation_ops.py
```

| Deck | Date | Formats |
|------|------|---------|
| [VELIFORM_BUSINESS_PRESENTATION_2026-07-28.md](./VELIFORM_BUSINESS_PRESENTATION_2026-07-28.md) | 2026-07-28 | [PDF](./VELIFORM_BUSINESS_PRESENTATION_2026-07-28.pdf) · [PPTX](./VELIFORM_BUSINESS_PRESENTATION_2026-07-28.pptx) |
| [VELIFORM_BUSINESS_PRESENTATION_2026-07-28_RU.md](./VELIFORM_BUSINESS_PRESENTATION_2026-07-28_RU.md) | 2026-07-28 | [PDF RU](./VELIFORM_BUSINESS_PRESENTATION_2026-07-28_RU.pdf) |
