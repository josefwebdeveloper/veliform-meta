# Veliform Meta

Company-level registry for **Veliform**: CEO Notion hub config, bootstrap scripts, shared Cursor rules.

## Layout

```
~/WORKSPACE/veliform/
├── meta/              ← this repo (CEO registry, bootstrap)
├── veliform-landing/  ← veliform.com company site (Vercel)
├── agent-company/     ← WeOffice — Agent Company SaaS (MVP)
├── voice/             ← Veliform Voice Agent
└── …
```

## New Mac setup

```bash
git clone https://github.com/josefwebdeveloper/veliform-meta.git ~/WORKSPACE/veliform/meta
cd ~/WORKSPACE/veliform/meta
./scripts/bootstrap.sh
```

Open **`veliform.code-workspace`** in Cursor.

## CEO Notion

Setup guide: [docs/NOTION_CEO.md](docs/NOTION_CEO.md)

Project registry: [ceo/projects.yaml](ceo/projects.yaml)

Ideas backlog: [ceo/ideas.yaml](ceo/ideas.yaml) · [docs/ideas/AGENT_COMPANY_SAAS.md](docs/ideas/AGENT_COMPANY_SAAS.md)

Org + agents (HQ dashboard): [ceo/org.yaml](ceo/org.yaml) · [docs/COMPANY_HQ.md](docs/COMPANY_HQ.md)

Task sync (ClickUp + Notion + HQ): [docs/TASK_SYNC.md](docs/TASK_SYNC.md) · ClickUp company lists: [docs/CLICKUP_VELIFORM.md](docs/CLICKUP_VELIFORM.md)

Autonomous traffic + content-opportunity reporting: [docs/MARKETING_AGENT.md](docs/MARKETING_AGENT.md)

## Push this repo

```bash
cd ~/WORKSPACE/veliform/meta
git init
git remote add origin git@github.com:josefwebdeveloper/veliform-meta.git
git add -A && git commit -m "Veliform meta: CEO registry bootstrap"
git push -u origin main
```

Create the GitHub repo `veliform-meta` first if it does not exist.
