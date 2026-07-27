# WeOffice — Agent Company SaaS

> **Status:** Building — MVP in `agent-company/` (WeOffice UI)  
> **Slug:** `agent-company-saas` · **Workstream:** `agent-company`  
> **CEO Notion:** Type = Idea, Tier = Idea, Stage = Discovery, Priority = P2  
> **Separate from:** Veliform Voice (`veliform-voice`), internal HQ (`veliform-company`)

## One-liner

B2B SaaS where a customer **opens an AI company online**, **hires automation agents** from a catalog, and **monitors everything** on a dashboard — without voice, without Veliform-internal tooling.

## Problem

Founders and small teams want outcomes (SEO monitoring, marketing ops, reporting, automations) but not another workflow builder or hiring humans. They respond to the **company metaphor**: departments, hires, roster, activity feed — not “configure a LangGraph node.”

## Product vision

```
Sign up → Create company (name, goal)
       → Browse agent catalog → Hire agents
       → Dashboard: org, roster, tasks, activity, spend
       → Agents run on schedule / webhooks and report back
```

**In scope (future product):**

- Multi-tenant SaaS (each customer = one org)
- Text/automation agents (SEO, analytics, ops, content ops, integrations)
- Hire / pause / fire agents
- Activity stream + audit log
- Task queue and human approval for sensitive actions
- Per-agent or org-level budget caps

**Out of scope (explicit):**

- Voice / telephony agents (→ Veliform Voice product line)
- Veliform internal `veliform.com/hq` (dogfooding only — patterns may be reused)
- Generic “chatbot builder” without org/company narrative

## Reference inside Veliform (dogfooding)

We already run this model **for ourselves**:

| Internal piece | Reuse for product? |
|----------------|-------------------|
| `meta/ceo/org.yaml` — departments, agents, plans | Data model inspiration (per-tenant org) |
| `veliform.com/hq` — OrgMap, AgentBento, ActivityStream | UI patterns, not the product itself |
| SEO Agent, Marketing Analyst, CEO Steward | First catalog agents to productize |

## Competitors (research Jul 2026)

### Closest to our narrative

| Product | URL | Strengths to learn from |
|---------|-----|-------------------------|
| Agentyfy | https://agentyfy.ai/ | Org chart, board approval, per-agent budgets, audit log, BYOK |
| Agent.ceo | https://agent.ceo/ | SaaS onboarding, org map, task board, terminal/activity feed |
| WorkoAI | https://www.workoai.com/ | Pre-built roles (CEO, Sales, Marketing…), HITL approvals |
| Preplix | https://preplix.ai/ | “Hire” UX, priced roles, fast time-to-first-agent |

### Adjacent

| Product | Notes |
|---------|--------|
| Relevance AI | Multi-agent workforce, less “company” story |
| Ideople | No-code agents + workflows, freemium |
| CogniAgent | Enterprise virtual employees, heavy integrations |
| OrdoNova BotWorks / VoltusWave | Enterprise ARP / governance |

### Not direct competitors (engines)

LangGraph, CrewAI, n8n, Zapier AI Agents — infrastructure or automation, not “open your AI company.”

## Differentiation wedge (TBD before build)

Pick **one** primary wedge when moving to Planning:

1. **Out-of-the-box automation agents** — SEO + GA4/GSC + reporting (we already ship this internally)
2. **Simpler than Agent.ceo** — SMB founders, no Kubernetes narrative
3. **Cheaper than Preplix** — self-serve catalog, usage-based
4. **Vertical** — e.g. “AI company for Shopify / local services”

## MVP definition (when approved)

**Goal:** One paying design partner or 10 beta orgs running 2+ agents for 30 days.

| Epic | Scope |
|------|--------|
| E1 Auth & org | Sign up, create company, basic settings |
| E2 Agent catalog v1 | 3 agents: SEO Monitor, Marketing Analyst, Ops Reporter (names TBD) |
| E3 Hire flow | Enable agent, connect integrations (OAuth), set schedule |
| E4 Dashboard v1 | Roster, status, last run, activity feed |
| E5 Runtime v1 | Scheduled jobs + webhook triggers, isolated per tenant |
| E6 Billing v1 | Stripe, plan limits, soft budget warning |

**Not in MVP:** marketplace of third-party agents, mobile app, self-hosted, voice.

## Backlog (future epics)

Priority order is indicative — re-rank at Planning.

### P0 — Discovery (before any code)

- [x] **D0** MVP v0 UI shell — `agent-company/` (landing, onboarding, dashboard, local hire/run)
- [ ] **D1** Confirm wedge vs Agentyfy / Agent.ceo (30-min competitor matrix)
- [ ] **D2** 5 customer interviews: “Would you open an AI company?” — jobs, objections, price
- [ ] **D3** Name + domain shortlist (not Veliform-branded? sub-brand?)
- [ ] **D4** Legal/compliance sketch: data isolation, subprocessors, ToS for autonomous actions
- [ ] **D5** Unit economics: LLM + infra cost per agent per month vs target price

### P1 — Planning

- [ ] **P1.1** PRD v1 + user stories for MVP epics E1–E6
- [ ] **P1.2** Architecture: multi-tenant DB, job runner, secrets per tenant
- [ ] **P1.3** Agent runtime choice: reuse marketing-agent patterns vs greenfield worker
- [ ] **P1.4** Integration list for v1 (GA4, GSC, Notion?, Slack?, email?)
- [ ] **P1.5** Design: landing + onboarding + dashboard (wireframes)
- [ ] **P1.6** Notion CEO row → Stage `Planning`; create GitHub repo when ready

### P2 — Build (post-approval)

- [ ] **B1** Repo bootstrap + CI + staging env — **v0 UI done locally**
- [x] **B2** Tenant model + auth (Clerk + Neon Postgres on Vercel)
- [ ] **B3** Catalog + hire API
- [ ] **B4** Agent worker v1 (port SEO + Marketing Analyst logic)
- [ ] **B5** Dashboard (fork patterns from HQ UI, new brand)
- [ ] **B6** Audit log + approval gate for external sends
- [ ] **B7** Stripe billing + usage metering

### P3 — Growth (later)

- [ ] **G1** Agent marketplace / custom agents
- [ ] **G2** Team seats + roles (owner, operator, viewer)
- [ ] **G3** Public API + webhooks for customers
- [ ] **G4** Partner integrations (ClickUp, HubSpot, …)

## Registry & ops

| System | Action |
|--------|--------|
| **Git** | This doc: `meta/docs/ideas/AGENT_COMPANY_SAAS.md` |
| **CEO Notion** | Add row — see bootstrap table in [NOTION_CEO.md](../NOTION_CEO.md#ideas-backlog) |
| **ClickUp** | Epic in `📋 Backlog` list — [Agent Company SaaS](https://app.clickup.com/t/86eydxhzx) |
| **HQ** | Plan card in `ceo/org.yaml` → `agent-company-saas-discovery` |
| **projects.yaml** | `ideas:` entry with slug + doc path |

## Open questions

1. Separate brand from Veliform or “Veliform Agents” line?
2. BYOK (customer API keys) vs platform-managed keys?
3. First vertical or horizontal SMB?
4. Self-serve only vs sales-assisted design partners?

## CEO — next action when picking this up

> Review competitor matrix (D1), run 3 interviews (D2), decide wedge (Differentiation section), then move Notion Stage to **Planning** and create ClickUp tasks for P1 epics.

---

*Captured Jul 2026. Product name: **WeOffice**. MVP in `agent-company/`.*
