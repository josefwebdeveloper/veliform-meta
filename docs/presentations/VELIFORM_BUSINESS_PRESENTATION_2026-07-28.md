---
marp: true
theme: default
paginate: true
title: Veliform — Company Goal & Profit Model
description: Numbers, dates, and roadmap as of 2026-07-28
---

# Veliform
## AI that runs your business

**Presentation date:** 2026-07-28  
**Founder:** Josef Shainskiy  
**Production:** [veliform.com](https://veliform.com) · [veliform.com/hq](https://veliform.com/hq)

> **Strategy update (2026-08-03):** this deck is a historical snapshot. The current operating plan is in [`PRODUCT_AUDIT_2026-08-03_RU.md`](../PRODUCT_AUDIT_2026-08-03_RU.md): Voice-first, hospitality paid pilots, Launchpad paused until release gates, and WeOffice limited to dogfood plus one design partner.

---

# Slide 1 — Company goal

| | |
|---|---|
| **Mission** | Build AI that **works for the business** — not chatbots, but an **organization of agents** with names, roles, and tools |
| **Tagline** | *AI that runs your business* |
| **For customers** | 24/7 phone coverage, orders, bookings, lead capture, SEO, marketing ops |
| **For Veliform** | Recurring SaaS revenue on **Voice** (now) and **WeOffice** (next) |

**One-line thesis:** Small businesses lose money on missed calls and manual ops. Veliform replaces that with AI agents at a fraction of human cost.

---

# Slide 2 — What we sell (3 product lines)

| Product | Slug | Status (Jul 2026) | Revenue model |
|---------|------|-------------------|---------------|
| **Veliform Voice** | `veliform-voice` | Live pilot (invite-only) | B2B subscription per business line |
| **Veliform Company Site** | `veliform-company` | Live | Lead gen → Voice / WeOffice sales |
| **WeOffice** | `agent-company-saas` | Building (MVP v2) | B2B SaaS — hire automation agents |

**4 repos · 3 commercial products · 1 meta registry**

```
meta/  veliform-landing/  voice/  agent-company/
```

---

# Slide 3 — Veliform Voice (main revenue engine)

### Three non-overlapping lines

| Line | Who pays | What they get | Deploy |
|------|----------|---------------|--------|
| **Business Platform** | B2B owner | AI receptionist 24/7 — orders, leads, handoff | `business-server` (Railway) |
| **Personal** | Owner | Alice (assistant) + Secretary (call screening) | `personal-server` (Railway) |
| **Voice Copilot** | Sales / HR / RE | Live hints in Telegram during real calls | `copilot-server` (planned) |

### Live numbers (prod)

| Asset | Value |
|-------|-------|
| Demo tenant | **Rose** · florist · slug `bloom-petal` |
| Business line | `+972535647910` |
| Personal line | `+972533885100` |
| Max call length (business/personal) | **480 sec (8 min)** |
| Max call length (copilot) | **1,800 sec (30 min)** |
| Multi-tenant businesses on one server | **1 live** · **1 planned** (Maya / real estate) |

---

# Slide 4 — Launchpad promise (Voice GTM)

**Spec date:** 2026-07-27 · Owner: Veliform Product

> **Build your AI receptionist. Your first test call in five minutes.**

| Step | Time target | Status |
|------|-------------|--------|
| Enter website URL | ~30 sec | Spec complete |
| Auto-generate agent draft | ~2 min | Building |
| Browser test call | ~2 min | Partial (WebRTC exists) |
| Phone activation | Manual (pilot) | Invite-only concierge |

**Company objective (Launchpad):** Prove **2 different business tenants** through **1 repeatable onboarding** by end of Phase D.

**Pilot today:** No public billing · no self-signup · concierge onboarding only.

---

# Slide 5 — Customer ROI (why they pay)

### Problem → math

| Pain | Industry benchmark | Veliform answer |
|------|-------------------|-----------------|
| Missed after-hours call | 1 lost order / lead per week | Rose answers 24/7 |
| Part-time receptionist | **$1,500–3,000/mo** (varies by market) | AI line subscription |
| SEO + marketing ops | Freelancer **$500–2,000/mo** | Automation agents (WeOffice) |

### Example florist (demo tenant Rose)

1. Customer calls at **23:00** → AI takes order  
2. SMS confirmation + Telegram alert to owner  
3. **1 extra order/week × $40 avg = $160/mo** recovered revenue  
4. If subscription **< $160/mo** → positive ROI for owner

*Veliform margin:* shared `business-server` — marginal cost per new tenant ↓ as N grows.

---

# Slide 6 — Veliform Company Site (funnel)

**Prod URL:** [veliform.com](https://veliform.com) · Vercel project **`porqa`**

| Surface | Agent | Purpose | Status |
|---------|-------|---------|--------|
| `#architect` | AI Architect | Lead qualification + expertise demo | **Live** |
| SEO layer | SEO Agent | Sitemap, JSON-LD, agent-skills | **Active** |
| Traffic ops | Marketing Analyst | GA4 + Search Console monitoring | **Beta** |
| Internal | HQ dashboard | Org map, roster, activity (30s poll) | **Live since 2026-07** |

### GA4 (Veliform Website)

| Metric | ID |
|--------|-----|
| Property ID | **547070151** |
| Measurement tag | **G-KW31ZW9NMY** |
| Key conversion events | 4 (`ai_consultation_*`, `book_consultation_click`, `contact_email_click`) |

---

# Slide 7 — WeOffice (next SaaS revenue)

**Idea captured:** Jul 2026 · **Prod preview:** [agent-company-navy.vercel.app](https://agent-company-navy.vercel.app)

> Open your AI company → hire automation agents → monitor on dashboard

### MVP milestone (documented target)

| KPI | Target | Deadline style |
|-----|--------|----------------|
| Paying design partners | **1** | Before GA |
| OR beta orgs | **10** orgs × **2+ agents** × **30 days** | Before GA |

### MVP version ladder

| Version | Deliverable | Status |
|---------|-------------|--------|
| v0 | Local demo UI | ✅ Done |
| v1 | WeOffice brand + catalog | ✅ Done |
| v2 | Clerk + Neon + Vercel API + cron | ✅ Done |
| v3 | Live GA4 Marketing Analyst worker | Building |
| v4 | **Stripe billing** | Planned |

### Agent catalog size

**10 agents** in catalog (6 core roles + 4 automation: SEO, Marketing, Ops, Content)

---

# Slide 8 — AI organization today (11 agents)

**Source:** `ceo/org.yaml` · Updated 2026-07-27

| Status | Count | Agents |
|--------|-------|--------|
| **Live / Active** | **7** | Rose, Alice, Secretary, SEO Agent, AI Architect, CEO Steward, GitHub CI |
| **Beta** | **3** | HR Copilot, Marketing Analyst, Finance Analyst |
| **Planned** | **1** | Maya (real estate) |

**5 departments:** Product · Engineering · Marketing & SEO · Operations · Finance  
**1 human:** Josef Shainskiy (Founder / CEO)

---

# Slide 9 — Automation schedules (ops at scale)

| Agent | Frequency | Output cap |
|-------|-----------|------------|
| **Marketing Analyst** | 2× daily (05:00, 17:00 UTC) + weekly Mon 06:00 UTC | ≤ **1** ClickUp task/day · ≤ **3**/week + **1** Notion update |
| **Finance Analyst** | Every **2 hours** + weekly Mon 07:00 UTC | Telegram alert on anomaly only |
| **GitHub CI** | Every push to `main` | 1 CEO Update per deploy |
| **HQ dashboard** | Poll Notion every **~30 sec** | Live product board + activity |

### Marketing alert thresholds

- Min baseline sessions: **20** before anomaly fires  
- Traffic drop trigger: **≥40%**  
- Key event drop trigger: **≥50%**

---

# Slide 10 — Infrastructure cost (Jul 2026)

**Finance Analyst monitors Railway first** (Vercel / Twilio / OpenAI later)

| Threshold | USD | Action |
|-----------|-----|--------|
| Hobby included credit | **$5/mo** | Baseline plan |
| Estimated bill **warn** | **≥ $8** | Telegram alert |
| Estimated bill **critical** | **≥ $15** | Telegram alert |
| Voice project share warn | **>65%** of workspace spend | Review voice-agent project |

**Burn pace warn:** > **1.35×** expected for billing period

*When customer billing goes live → Stripe revenue tracked; Finance Analyst roadmap includes Stripe.*

---

# Slide 11 — Revenue model (planned pricing structure)

> **Note:** Public pricing TBD. Structure below follows product architecture + MVP specs.

| Product | Unit | Indicative model | When |
|---------|------|------------------|------|
| **Voice Business** | Per tenant / phone line | Monthly subscription + usage (minutes) | After Launchpad GA |
| **Voice Personal** | Per owner line | Monthly subscription | After Launchpad GA |
| **Voice Copilot** | Per seat / vertical | Monthly + per-minute cap (30 min) | Phase copilot-server |
| **WeOffice** | Per org | Stripe plans + per-agent limits | MVP v4 |

### Near-term revenue gates

| Gate | Date context | Metric |
|------|--------------|--------|
| Voice pilot → paid pilot | Q3 2026 target | First **3–5** concierge customers |
| WeOffice beta | Q3–Q4 2026 | **10** orgs or **1** design partner |
| Stripe live | WeOffice v4 | First MRR |

---

# Slide 12 — Timeline (key dates)

| Date | Milestone |
|------|-----------|
| **2026-07-23** | Product Architecture agreed (3 Voice lines, multi-tenant business) |
| **2026-07-24–25** | Voice Copilot MVP + real estate market search |
| **2026-07-26** | CEO Notion registry · Veliform Voice rebrand · 8-min call cap · HQ CI |
| **2026-07-27** | Launchpad spec v1 · Company Guide · org.yaml v2 (11 agents) |
| **2026-07-28** | This presentation · Finance Analyst registered |
| **H2 2026** | Voice Phase D — tenant #2 (Maya / real estate) |
| **H2 2026** | Launchpad public beta + billing |
| **H2 2026** | WeOffice v3 (live GA4 worker) → v4 (Stripe) |

---

# Slide 13 — Active plans (HQ Plans rail)

| Plan ID | Title | Status | Target outcome |
|---------|-------|--------|----------------|
| `voice-phase-d` | Second business tenant (Maya) | **Building** | 2 verticals, 1 onboarding flow |
| `copilot-server` | Dedicated Copilot deploy | Planned | Separate Railway service |
| `hq-v1` | Company HQ dashboard | **Live** | Internal + demo of WeOffice UX |
| `agent-company-saas-discovery` | WeOffice MVP | **Building** | First paying SaaS customers |

---

# Slide 14 — How profit flows (summary)

```
                    ┌─────────────────────────────────┐
  veliform.com      │  AI Architect · SEO · GA4       │
  (lead gen)        └───────────────┬─────────────────┘
                                    │ qualified leads
                                    ▼
                    ┌─────────────────────────────────┐
  Veliform Voice    │  $/mo per business line         │  ← primary revenue (2026)
  (B2B + Personal)  │  ROI: captured calls & orders   │
                    └───────────────┬─────────────────┘
                                    │ upsell / expand
                                    ▼
                    ┌─────────────────────────────────┐
  WeOffice SaaS     │  $/mo per org + agent tiers     │  ← scale revenue (2026–27)
  (automation)      │  Replace freelancers & DIY ops  │
                    └─────────────────────────────────┘

  Veliform cost base: ~$5–15/mo Railway today → scales sub-linearly with tenants
```

---

# Slide 15 — KPIs to track

| KPI | Baseline (Jul 2026) | Target (Dec 2026) |
|-----|---------------------|-------------------|
| Live Voice business tenants | **1** | **5+** |
| Concierge → paid conversions | **0** (pilot) | **3–5** |
| Launchpad: URL → test call | Partial | **< 5 min** E2E |
| GA4 `ai_consultation_completed` / mo | Track in GA4 | **+50%** vs Q3 baseline |
| WeOffice beta orgs | **0** | **10** or **1** paid partner |
| MRR | **$0** (pre-billing) | First **$1K** MRR |
| Railway infra / tenant | ~$5–15 total | **< $3** marginal per tenant |

---

# Slide 16 — Three-layer ops (how we run lean)

| Layer | Tool | Question | Update cadence |
|-------|------|----------|----------------|
| Tasks | **ClickUp** | What to do? | Daily |
| History | **Notion CEO** | What happened? | Per git push + agent runs |
| Live view | **HQ** | How does the company look now? | **~30 sec** |

**Result:** 1 founder + **11 AI agents** operate marketing, finance pulse, voice, and CEO logging without a large headcount.

---

# Slide 17 — Competitive wedge

| Competitor type | Examples | Veliform difference |
|-----------------|----------|-------------------|
| Voice AI | Dialzara, etc. | Launchpad: **website first**, hear agent in **5 min** |
| Agent SaaS | Agent.ceo, Agentyfy, Preplix | We ship **real agents internally** (SEO, GA4) — not slides |
| DIY automation | Zapier, n8n | **Company metaphor** — hire Rose, not "configure a node" |

**Documented wedge options (WeOffice):** out-of-the-box SEO+GA4 agents · simpler than Agent.ceo · usage-based pricing

---

# Slide 18 — Ask & next steps

### For investors / partners

- Veliform is **pre-revenue**, **post-product**: live voice demo, live site, automation agents running
- **Near-term:** close paid Voice pilots · ship Launchpad · WeOffice Stripe v4
- **Proof point by Dec 2026:** 5 Voice tenants + $1K MRR

### Contact

- **Web:** [veliform.com](https://veliform.com)  
- **Email:** hello@veliform.com  
- **Demo call:** Rose · `+972535647910`  
- **HQ (internal):** [veliform.com/hq](https://veliform.com/hq)

---

*Generated 2026-07-28 · Sources: `meta/ceo/org.yaml`, `meta/docs/COMPANY_GUIDE_RU.md`, `voice/docs/VOICE_LAUNCHPAD.md`, `meta/docs/ideas/AGENT_COMPANY_SAAS.md`, `veliform-landing/config/*-agent.json`*
