# Veliform Meta

Company-level registry for **Veliform**: CEO Notion hub config, bootstrap scripts, shared Cursor rules.

## Layout

```
~/WORKSPACE/veliform/
├── meta/              ← this repo (CEO registry, bootstrap)
├── veliform-landing/  ← veliform.com company site (Vercel)
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

## Push this repo

```bash
cd ~/WORKSPACE/veliform/meta
git init
git remote add origin git@github.com:josefwebdeveloper/veliform-meta.git
git add -A && git commit -m "Veliform meta: CEO registry bootstrap"
git push -u origin main
```

Create the GitHub repo `veliform-meta` first if it does not exist.
