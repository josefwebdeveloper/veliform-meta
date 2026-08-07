# Veliform site map — canonical URLs and DNS

> Source of truth for public URLs, display names, and infrastructure mapping.  
> Updated: 2026-08-07

## Structure

```
VELIFORM (company)
├── veliform.com              → Veliform Voice SEO landing (primary)
├── veliform.com/company      → company marketing + AI Architect
└── veliform.com/hq           → internal HQ (noindex)

VELIFORM VOICE (product)
├── app.veliform.com          → redirects to veliform.com/ (301)
│   ├── /start                → Launchpad paused page (noindex) or launchpad when enabled
│   ├── /test                 → voice test (noindex, admin)
│   └── /admin                → Voice Admin (noindex)
└── my.veliform.com           → personal line — Alice (noindex)

WEOFFICE (product — building)
└── office.veliform.com       → WeOffice SaaS landing + app
```

## Canonical URLs

| Display name | URL | SEO | Deploy | Repo |
|--------------|-----|-----|--------|------|
| Veliform Voice (SEO) | https://veliform.com/ | index | Vercel `porqa` | veliform-landing |
| Veliform Company | https://veliform.com/company | index | Vercel `porqa` | veliform-landing |
| Veliform HQ | https://veliform.com/hq | noindex | Vercel `porqa` | veliform-landing |
| Veliform Voice App root | https://app.veliform.com | noindex (301 → /) | Railway `voice-server` | voice-agent |
| Launchpad / paused | https://app.veliform.com/start | noindex | Railway `voice-server` | voice-agent |
| Voice Admin | https://app.veliform.com/admin | noindex | Railway `voice-server` | voice-agent |
| Alice (personal) | https://my.veliform.com | noindex | Railway `personal-server` | voice-agent |
| WeOffice | https://office.veliform.com | index (landing) | Vercel `agent-company` | agent-company |

## Legacy URLs (redirect / stop using)

| Old URL | Replace with |
|---------|--------------|
| veliform.com/voice | veliform.com/ (301) |
| voice-server-production-f958.up.railway.app | app.veliform.com |
| personal-server-production-3d89.up.railway.app | my.veliform.com |
| agent-company-navy.vercel.app | office.veliform.com |

## DNS records (GoDaddy — veliform.com)

Add at your DNS provider (nameservers: domaincontrol.com):

| Host | Type | Value | Purpose |
|------|------|-------|---------|
| `office` | A | `76.76.21.21` | WeOffice → Vercel |
| `app` | CNAME | `voice-server-production-f958.up.railway.app` | Voice business (or Railway custom domain target) |
| `my` | CNAME | `personal-server-production-3d89.up.railway.app` | Personal line |

After adding `app` and `my` in Railway dashboard (Settings → Networking → Custom Domain), Railway may provide specific CNAME targets — use those instead of the `.up.railway.app` host if shown.

### office.veliform.com

Added to Vercel project `agent-company`. Pending DNS:

```
A  office.veliform.com  →  76.76.21.21
```

## Railway env (after DNS live)

**voice-server** (`app.veliform.com`):

```
PUBLIC_BASE_URL=https://app.veliform.com
```

**personal-server** (`my.veliform.com`):

```
PUBLIC_BASE_URL=https://my.veliform.com
```

## SEO rules

- **Primary Voice SEO URL:** `veliform.com/` — marketing landing (sitemap, GSC)
- **Company site:** `veliform.com/company`
- **Legacy:** `veliform.com/voice` → 301 to `veliform.com/`
- **app.veliform.com `/`:** 301 to `veliform.com/`
- **app.veliform.com `/start`:** Launchpad paused (or launchpad when `LAUNCHPAD_ENABLED=true`)
- **Admin / Launchpad / HQ / my:** noindex
- **WeOffice landing** on `office.veliform.com` — index; dashboard routes noindex

## Agents → surfaces

| Agent | Surface |
|-------|---------|
| Rose | app.veliform.com/admin + business phone |
| Alice | my.veliform.com |
| Secretary | my.veliform.com/admin |
| SEO / Marketing Analyst | veliform.com/hq roster |
| WeOffice catalog | office.veliform.com |
