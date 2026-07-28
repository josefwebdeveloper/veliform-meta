---
marp: true
theme: default
paginate: true
title: Veliform — цель компании и модель прибыли
description: Цифры, даты и roadmap на 2026-07-28
---

# Veliform
## AI that runs your business

**Дата презентации:** 2026-07-28  
**Основатель:** Josef Shainskiy  
**Продакшн:** [veliform.com](https://veliform.com) · [veliform.com/hq](https://veliform.com/hq)

---

# Слайд 1 — Цель компании

| | |
|---|---|
| **Миссия** | Строить AI, который **работает за бизнес** — не чат-боты, а **организация агентов** с именами, ролями и инструментами |
| **Слоган** | *AI that runs your business* |
| **Для клиентов** | 24/7 звонки, заказы, бронирования, лиды, SEO, маркетинг |
| **Для Veliform** | Подписка на **Voice** (сейчас) и **WeOffice** (далее) |

**Тезис:** Малый бизнес теряет деньги на пропущенных звонках и ручной операционке. Veliform заменяет это AI-агентами дешевле человека.

---

# Слайд 2 — Что продаём (3 продуктовые линии)

| Продукт | Slug | Статус (июль 2026) | Модель дохода |
|---------|------|---------------------|---------------|
| **Veliform Voice** | `veliform-voice` | Пилот (invite-only) | B2B подписка на бизнес-линию |
| **Veliform Company Site** | `veliform-company` | Live | Лидоген → продажи Voice / WeOffice |
| **WeOffice** | `agent-company-saas` | Building (MVP v2) | B2B SaaS — найм automation-агентов |

**4 репо · 3 коммерческих продукта · 1 meta-реестр**

```
meta/  veliform-landing/  voice/  agent-company/
```

---

# Слайд 3 — Veliform Voice (главный движок выручки)

### Три непересекающихся линии

| Линия | Кто платит | Что получает | Deploy |
|-------|------------|--------------|--------|
| **Business Platform** | B2B владелец | AI-ресепшн 24/7 — заказы, лиды, handoff | `business-server` (Railway) |
| **Personal** | Владелец | Alice (ассистент) + Secretary (фильтр звонков) | `personal-server` (Railway) |
| **Voice Copilot** | Sales / HR / RE | Подсказки в Telegram во время звонка | `copilot-server` (план) |

### Цифры prod

| Актив | Значение |
|-------|----------|
| Demo tenant | **Rose** · флорист · slug `bloom-petal` |
| Business line | `+972535647910` |
| Personal line | `+972533885100` |
| Макс. длина звонка (business/personal) | **480 сек (8 мин)** |
| Макс. длина звонка (copilot) | **1 800 сек (30 мин)** |
| Multi-tenant на одном сервере | **1 live** · **1 planned** (Maya / недвижимость) |

---

# Слайд 4 — Обещание Launchpad (Voice GTM)

**Дата спеки:** 2026-07-27 · Owner: Veliform Product

> **Соберите AI-ресепшн. Первый тестовый звонок за пять минут.**

| Шаг | Целевое время | Статус |
|-----|---------------|--------|
| Ввод URL сайта | ~30 сек | Спека готова |
| Авто-черновик агента | ~2 мин | В разработке |
| Тест в браузере | ~2 мин | Частично (WebRTC есть) |
| Активация телефона | Вручную (пилот) | Invite-only concierge |

**Цель компании (Launchpad):** Доказать **2 разных business tenant'а** через **1 повторяемый онбординг** к концу Phase D.

**Пилот сейчас:** Нет публичного billing · нет self-signup · только concierge.

---

# Слайд 5 — ROI клиента (зачем платят)

### Боль → математика

| Боль | Бенчмарк | Ответ Veliform |
|------|----------|----------------|
| Пропущенный звонок после 18:00 | 1 потерянный заказ/лид в неделю | Rose отвечает 24/7 |
| Частичная занятость ресепшн | **$1 500–3 000/мес** | Подписка на AI-линию |
| SEO + маркетинг ops | Фриланс **$500–2 000/мес** | Automation-агенты (WeOffice) |

### Пример флориста (demo Rose)

1. Клиент звонит в **23:00** → AI принимает заказ  
2. SMS + Telegram владельцу  
3. **1 лишний заказ/нед × $40 = $160/мес** восстановленной выручки  
4. Если подписка **< $160/мес** → положительный ROI

*Маржа Veliform:* общий `business-server` — marginal cost на tenant ↓ при росте N.

---

# Слайд 6 — Veliform Company Site (воронка)

**Prod URL:** [veliform.com](https://veliform.com) · Vercel проект **`porqa`**

| Поверхность | Агент | Задача | Статус |
|-------------|-------|--------|--------|
| `#architect` | AI Architect | Квалификация лидов + демо экспертизы | **Live** |
| SEO слой | SEO Agent | Sitemap, JSON-LD, agent-skills | **Active** |
| Трафик | Marketing Analyst | GA4 + Search Console | **Beta** |
| Внутренний | HQ dashboard | Org map, roster, activity (poll 30 сек) | **Live с июля 2026** |

### GA4 (Veliform Website)

| Метрика | ID |
|---------|-----|
| Property ID | **547070151** |
| Measurement tag | **G-KW31ZW9NMY** |
| Key events | **4** (`ai_consultation_*`, `book_consultation_click`, `contact_email_click`) |

---

# Слайд 7 — WeOffice (следующая SaaS-выручка)

**Идея:** июль 2026 · **Preview:** [agent-company-navy.vercel.app](https://agent-company-navy.vercel.app)

> Откройте AI-компанию → наймите automation-агентов → мониторинг на dashboard

### MVP milestone (документированная цель)

| KPI | Цель |
|-----|------|
| Платящий design partner | **1** |
| ИЛИ beta orgs | **10** org × **2+ агента** × **30 дней** |

### Лadder версий MVP

| Версия | Deliverable | Статус |
|--------|-------------|--------|
| v0 | Local demo UI | ✅ |
| v1 | WeOffice brand + catalog | ✅ |
| v2 | Clerk + Neon + Vercel API + cron | ✅ |
| v3 | Live GA4 Marketing Analyst | Building |
| v4 | **Stripe billing** | Planned |

**10 агентов** в каталоге (6 core roles + 4 automation)

---

# Слайд 8 — AI-организация сегодня (11 агентов)

**Источник:** `ceo/org.yaml` · Обновлено 2026-07-27

| Статус | Кол-во | Агенты |
|--------|--------|--------|
| **Live / Active** | **7** | Rose, Alice, Secretary, SEO Agent, AI Architect, CEO Steward, GitHub CI |
| **Beta** | **3** | HR Copilot, Marketing Analyst, Finance Analyst |
| **Planned** | **1** | Maya (недвижимость) |

**5 отделов:** Product · Engineering · Marketing & SEO · Operations · Finance  
**1 человек:** Josef Shainskiy (Founder / CEO)

---

# Слайд 9 — Расписания automation (ops в масштабе)

| Агент | Частота | Лимит output |
|-------|---------|--------------|
| **Marketing Analyst** | 2×/день (05:00, 17:00 UTC) + weekly пн 06:00 UTC | ≤ **1** ClickUp/день · ≤ **3**/нед + **1** Notion |
| **Finance Analyst** | Каждые **2 ч** + weekly пн 07:00 UTC | Telegram только при аномалии |
| **GitHub CI** | Каждый push в `main` | 1 CEO Update |
| **HQ dashboard** | Poll Notion **~30 сек** | Live board + activity |

### Пороги Marketing Analyst

- Min baseline sessions: **20**  
- Падение трафика: **≥40%**  
- Падение key events: **≥50%**

---

# Слайд 10 — Стоимость инфраструктуры (июль 2026)

**Finance Analyst мониторит Railway** (Vercel / Twilio / OpenAI — позже)

| Порог | USD | Действие |
|-------|-----|----------|
| Hobby included credit | **$5/мес** | Baseline |
| Bill **warn** | **≥ $8** | Telegram alert |
| Bill **critical** | **≥ $15** | Telegram alert |
| Доля voice-agent | **>65%** spend | Review |

**Burn pace warn:** > **1.35×** ожидаемого за период

---

# Слайд 11 — Модель выручки (структура pricing)

> Публичный pricing TBD. Структура по архитектуре продукта.

| Продукт | Единица | Модель | Когда |
|---------|---------|--------|-------|
| **Voice Business** | Tenant / линия | Подписка + минуты | После Launchpad GA |
| **Voice Personal** | Owner line | Подписка | После Launchpad GA |
| **Voice Copilot** | Seat / vertical | Подписка + cap 30 мин | copilot-server |
| **WeOffice** | Org | Stripe + лимиты агентов | MVP v4 |

### Ближайшие revenue gates

| Gate | Период | Метрика |
|------|--------|---------|
| Voice pilot → paid | Q3 2026 | **3–5** concierge клиентов |
| WeOffice beta | Q3–Q4 2026 | **10** org или **1** partner |
| Stripe live | WeOffice v4 | Первый MRR |

---

# Слайд 12 — Timeline (ключевые даты)

| Дата | Milestone |
|------|-----------|
| **2026-07-23** | Product Architecture согласована |
| **2026-07-24–25** | Voice Copilot MVP + RE market search |
| **2026-07-26** | CEO Notion registry · rebrand · 8-min cap · HQ CI |
| **2026-07-27** | Launchpad spec v1 · Company Guide · 11 agents |
| **2026-07-28** | Презентация · Finance Analyst |
| **H2 2026** | Voice Phase D — tenant #2 (Maya) |
| **H2 2026** | Launchpad public beta + billing |
| **H2 2026** | WeOffice v3 → v4 (Stripe) |

---

# Слайд 13 — Активные планы (HQ Plans rail)

| Plan ID | Название | Статус | Outcome |
|---------|----------|--------|---------|
| `voice-phase-d` | Второй business tenant (Maya) | **Building** | 2 verticals, 1 onboarding |
| `copilot-server` | Dedicated Copilot deploy | Planned | Отдельный Railway |
| `hq-v1` | Company HQ dashboard | **Live** | Demo WeOffice UX |
| `agent-company-saas-discovery` | WeOffice MVP | **Building** | Первые платящие SaaS |

---

# Слайд 14 — Как течёт прибыль

```
  veliform.com (лиды) → Voice $/мес (2026) → WeOffice $/мес (2026–27)

  Cost base Veliform: ~$5–15/мес Railway → sub-linear scale с tenants
```

**Primary revenue 2026:** Voice B2B  
**Scale revenue 2026–27:** WeOffice SaaS

---

# Слайд 15 — KPI

| KPI | Baseline (июль 2026) | Target (дек 2026) |
|-----|----------------------|-------------------|
| Live Voice business tenants | **1** | **5+** |
| Concierge → paid | **0** | **3–5** |
| Launchpad URL → test call | Partial | **< 5 мин** E2E |
| GA4 consultations / мес | Track | **+50%** vs Q3 |
| WeOffice beta orgs | **0** | **10** или **1** partner |
| MRR | **$0** | **$1K** |
| Railway / tenant | ~$5–15 total | **< $3** marginal |

---

# Слайд 16 — Три слоя ops

| Слой | Инструмент | Вопрос | Cadence |
|------|------------|--------|---------|
| Tasks | **ClickUp** | Что делать? | Daily |
| History | **Notion CEO** | Что произошло? | Per push + agents |
| Live | **HQ** | Как выглядит компания? | **~30 сек** |

**1 founder + 11 AI-агентов** — marketing, finance, voice, CEO logging без большого штата.

---

# Слайд 17 — Конкурентное преимущество

| Тип | Примеры | Отличие Veliform |
|-----|---------|------------------|
| Voice AI | Dialzara | Launchpad: **сайт первым**, звонок за **5 мин** |
| Agent SaaS | Agent.ceo, Agentyfy | **Реальные агенты** внутри (SEO, GA4) |
| DIY | Zapier, n8n | **Метафора компании** — нанять Rose |

---

# Слайд 18 — Следующие шаги

### Для инвесторов / партнёров

- **Pre-revenue, post-product:** live voice demo, site, automation agents
- **Near-term:** paid Voice pilots · Launchpad · WeOffice Stripe v4
- **Proof point дек 2026:** 5 Voice tenants + **$1K MRR**

### Контакты

- **Web:** [veliform.com](https://veliform.com)  
- **Email:** hello@veliform.com  
- **Demo:** Rose · `+972535647910`  
- **HQ:** [veliform.com/hq](https://veliform.com/hq)

---

*Сгенерировано 2026-07-28 · EN: `VELIFORM_BUSINESS_PRESENTATION_2026-07-28.md`*
