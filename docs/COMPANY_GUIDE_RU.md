# Veliform — что мы делаем и как устроена компания

> **Для кого:** команда, новые сотрудники, клиенты и партнёры, которым нужно понять не «что мы умеем», а **что реально происходит** — продукты, агенты, системы и текущий статус.  
> **Обновлено:** 2026-07-27 · Источник правды: [`ceo/org.yaml`](../ceo/org.yaml), [`ceo/projects.yaml`](../ceo/projects.yaml)

---

## 1. Одним абзацем

**Veliform** — компания, которая строит AI, который **работает за бизнес**: отвечает на звонки, принимает заказы, ведёт календарь, следит за SEO и трафиком, консультирует потенциальных клиентов на сайте. Мы не продаём «ещё один чат-бот». Мы собираем **организацию из AI-агентов** — у каждого имя, роль, инструменты и зона ответственности — и показываем это на внутреннем дашборде [veliform.com/hq](https://veliform.com/hq).

Снаружи клиент видит результат: агент отвечает на телефон, сайт находят в Google, на главной можно описать бизнес и получить план автоматизации. Внутри команда видит **три связанных слоя** — задачи, реестр продуктов и live-дашборд.

---

## 2. Три слоя — как компания «помнит» себя

Это не три копии одного и того же. Каждый слой отвечает на свой вопрос.

| Слой | Вопрос | Где смотреть |
|------|--------|--------------|
| **ClickUp** | *Что нужно сделать?* Статус, приоритет, исполнитель | Space **VeliForm** → папки Company Site, Voice Agents |
| **Notion CEO** | *Что произошло?* Стадия продукта, последнее касание, история | Базы **CEO Projects** и **CEO Updates** |
| **HQ Dashboard** | *Как выглядит компания прямо сейчас?* | [veliform.com/hq](https://veliform.com/hq) — обновляется каждые ~30 сек из Notion |

```
                    ┌─────────────────┐
   Работа в коде ──► │  Git push main  │ ──► CEO Update (Notion)
                    └────────┬────────┘
                             │
   Задача закрыта ──► ClickUp Done          Activity feed на HQ
   Сессия в Cursor ──► CEO Update (cursor)  Product board на HQ
   Звонок Alice ──► «что по компании?» ──► read Notion CEO
```

**Правило для команды:** не дублировать ops-детали. В ClickUp — задача и ссылка на commit. В Notion — что изменилось и на какой стадии продукт. На HQ — живая картина без ручного обновления.

Подробнее: [`TASK_SYNC.md`](TASK_SYNC.md)

---

## 3. Продукты компании

### 3.1 Veliform Voice — главный коммерческий продукт

**Суть:** голосовой AI для бизнеса и для личного использования. Клиент звонит на номер — AI отвечает, использует инструменты (каталог, заказы, календарь, handoff на человека).

**Три линии продукта** (не смешиваются):

| Линия | Для кого | Пример |
|-------|----------|--------|
| **Business Platform** | B2B — клиенты бизнеса звонят AI | Rose у флориста, Maya у риэлтора (план) |
| **Personal** | Владелец компании — личный номер | Alice (ассистент) + Secretary (секретарь для звонящих) |
| **Voice Copilot** *(строится)* | Человек говорит с клиентом, AI шлёт подсказки в Telegram | HR Copilot сейчас в beta |

**Техника (упрощённо):**

- Twilio принимает звонок → Railway-сервис → OpenAI Realtime → агент выбирает tool → ответ клиенту / SMS / перевод на человека.
- Business: один сервер `business-server`, много **tenant'ов** (магазин, агентство и т.д.) — номер телефона определяет, какой агент отвечает.
- Personal: отдельный сервер `personal-server`, один владелец.

**Что строим сейчас — Launchpad:** путь для нового клиента «сайт → черновик агента → тестовый звонок за 5 минут → активация». Сейчас пилот invite-only, concierge-онбординг. Спека: `voice/docs/VOICE_LAUNCHPAD.md`.

**Prod URL (план):** `app.veliform.com` · Деплой: Railway (`voice-server`, `business-server`, `personal-server`).

---

### 3.2 Veliform Company Site — сайт и внутренний HQ

**Суть:** [veliform.com](https://veliform.com) — публичное лицо компании + внутренний control plane.

На сайте:
- Описание услуг (voice, интеграции, отрасли).
- **AI Architect** — интерактивная консультация на Gemini: клиент описывает бизнес → получает tagline, стек, фичи, сложность, совет.
- SEO-разметка, sitemap, agent-skills для AI-краулеров.

Внутри (пароль): **HQ** — org chart, roster агентов, product board, activity stream из Notion.

**Деплой:** Vercel, проект `porqa` (production env vars именно там).

---

### 3.3 Crewdesk (Agent Company SaaS) — будущий B2B продукт

**Суть:** SaaS, где **клиент открывает свою AI-компанию** — нанимает automation-агентов из каталога, смотрит dashboard. Без голоса, без нашего внутреннего HQ.

**Статус:** MVP v0 локально в `agent-company/` — landing, onboarding, demo dashboard. Репозиторий ещё не в GitHub.

Мы **dogfood'им** эту модель на себе: наш `org.yaml` + HQ + SEO/Marketing агенты — прототип того, что потом продадим.

Спека: [`docs/ideas/AGENT_COMPANY_SAAS.md`](ideas/AGENT_COMPANY_SAAS.md)

---

## 4. Отделы

| Отдел | Зона |
|-------|------|
| **Product** | Voice-агенты, демо-tenant'ы, Launchpad, Crewdesk |
| **Engineering** | Код, CI, деплой, инфра |
| **Marketing & SEO** | Сайт, трафик, контент, консультации на главной |
| **Operations** | CEO-реестр, HQ, личные ассистенты, процессы |

Люди и агенты привязаны к отделам в [`ceo/org.yaml`](../ceo/org.yaml) — это видно на карте org в HQ.

---

## 5. Все агенты — что каждый реально делает

### Голосовые агенты (Voice)

#### Rose — **live**
- **Кто:** AI-реceptionist демо-магазина цветов (Bloom & Petal / Veliform Demo Shop).
- **Номер:** `+972535647910` (business line).
- **Когда работает:** 24/7, когда клиент звонит в «магазин».
- **Что делает по шагам:**
  1. Приветствует, уточняет повод и бюджет.
  2. Ищет букеты в каталоге (`search_products`).
  3. Проверяет слот доставки (`check_delivery_slot`).
  4. Оформляет заказ (`create_order`) → SMS клиенту, Telegram владельцу.
  5. Если клиент злится или просит человека — переводит звонок (`handoff`).
- **Для клиента Veliform:** это **живое демо** Business Platform — «вот как будет звучать ваш агент».
- **Сервис:** `business-server` · tenant `bloom-petal`.

#### Alice — **live**
- **Кто:** личный AI-ассистент владельца (Josef).
- **Номер:** `+972533885100` — звонит **только owner** → режим assistant.
- **Что делает:**
  - Читает календарь на сегодня, создаёт события.
  - Работает с Gmail, Notion tasks.
  - Отвечает на «что по компании?» через `get_ceo_status` (стадии продуктов из Notion).
  - Может записать CEO Update голосом (`log_ceo_update`).
- **Не делает:** заказы Rose, business admin, секретарские сценарии для чужих звонков.
- **Сервис:** `personal-server`.

#### Secretary — **live**
- **Кто:** тот же номер `+972533885100`, но когда звонит **не owner**.
- **Что делает:**
  - Вежливо представляется, выясняет цель звонка.
  - Принимает сообщение (`take_message`) → alert в Telegram/SMS.
  - Проверяет «доступен ли Josef» (`check_availability`) — без раскрытия календаря.
  - При необходимости — handoff.
- **Зачем:** фильтрация входящих, пока владелец занят; отделение «мой ассистент» от «секретарь для всех остальных».
- **Сервис:** `personal-server`.

#### Maya — **planned**
- **Кто:** AI-агент для **недвижимости** — второй business-tenant.
- **Что будет делать:** listings, лиды, просмотры, web search, handoff.
- **Статус:** Phase D — второй tenant на том же `business-server`, отдельный Twilio-номер TBD.
- **Связь с планом:** `voice-phase-d` в org.yaml.

#### HR Copilot — **beta**
- **Кто:** не говорит в трубку клиенту.
- **Что делает:** во время **живого** разговора человека с кандидатом/клиентом шлёт **подсказки в Telegram** (`copilot_hints`).
- **Продуктовая линия:** Voice Copilot (отдельный deploy `copilot-server` — в планах).
- **Сервис сейчас:** `personal-server`.

---

### Automation-агенты (без голоса)

#### SEO Agent — **active**
- **Отдел:** Marketing.
- **Репо:** `veliform-landing`.
- **Что делает (не «один раз в месяц», а постоянная зона ответственности):**
  - Актуальный sitemap и robots.txt.
  - Meta tags, Open Graph, JSON-LD на ключевых страницах.
  - `.well-known/agent-skills` — чтобы AI-ассистенты (ChatGPT, Cursor и др.) находили наш consult skill.
  - Follow-up по Core Web Vitals / Lighthouse после изменений.
- **Как попадает в работу:** задачи в ClickUp list **🌐 SEO & Marketing**; изменения в коде → push → CEO Update.
- **Не делает:** анализ трафика и «что писать в блог» — это Marketing Analyst.

#### Marketing Analyst — **beta**
- **Отдел:** Marketing.
- **Где живёт:** GitHub Actions в `veliform-landing`, скрипт `marketing_agent.py`.
- **Что делает автономно:**
  - **Ежедневно:** смотрит GA4 — если заметное падение трафика или key events → **одна** задача в ClickUp (не спамит).
  - **Еженедельно:** сравнивает GA4 + Search Console, ранжирует возможности, Gemini формулирует углы → до **трёх** задач в ClickUp + **одна** запись в Notion CEO Updates.
- **Безопасность:** только read Google; не публикует контент, не меняет рекламу, не пишет в репозиторий без человека.
- **Отслеживаемые события:** `ai_consultation_started/completed`, `book_consultation_click`, `contact_email_click`.
- **Подробнее:** [`MARKETING_AGENT.md`](MARKETING_AGENT.md)

#### AI Architect — **live**
- **Отдел:** Marketing (лидоген).
- **Где:** секция `#architect` на [veliform.com](https://veliform.com).
- **Что делает:** клиент вводит описание бизнеса → Gemini (persona «CTO Veliform») возвращает структурированный план: tagline, tech stack, 3 core features, complexity, strategic advice.
- **Зачем компании:** квалификация лидов + демонстрация экспертизы без созвона; события уходят в GA4 для Marketing Analyst.
- **Для внешних AI:** skill `consult-ai-architect` в `.well-known/agent-skills/`.

#### CEO Steward — **live**
- **Отдел:** Operations.
- **Репо:** `meta`.
- **Что делает:** следит, чтобы **важные изменения не терялись** — после сессий в Cursor и значимой работы предлагает/пишет строку в **CEO Updates** (Notion): что изменилось, slug проекта, ссылка на commit.
- **Не заменяет:** ClickUp-задачи; дополняет **историю** для HQ activity stream.

#### GitHub CI — **live**
- **Отдел:** Engineering.
- **Что делает:** при **push в main** (voice-agent, veliform-landing) GitHub Action создаёт CEO Update (`source: git`) и при необходимости обновляет **Last touch** в CEO Projects.
- **Зачем:** activity feed на HQ наполняется автоматически — не нужно вручную «отчитываться о деплое».

---

## 6. Текущие планы (Plans rail на HQ)

| ID | Название | Статус | Смысл |
|----|----------|--------|-------|
| `voice-phase-d` | Voice Phase D — второй business tenant | building | Maya / real estate + admin UI для tenant #2 |
| `copilot-server` | Dedicated Copilot deploy | planned | Отдельный Railway для Voice Copilot |
| `hq-v1` | Company HQ dashboard | live | veliform.com/hq |
| `agent-company-saas-discovery` | Crewdesk | building | MVP v0, будущий SaaS |

---

## 7. Репозитории и где что лежит

```
~/WORKSPACE/veliform/
├── meta/              CEO-реестр, org.yaml, документация, bootstrap
├── veliform-landing/  veliform.com + HQ + SEO + Marketing Analyst
├── voice/             Voice Agent (monorepo: business/personal servers)
└── agent-company/     Crewdesk MVP (локально, не в GitHub)
```

| Repo | GitHub | Prod |
|------|--------|------|
| meta | josefwebdeveloper/veliform-meta | — |
| veliform-landing | josefwebdeveloper/veliform-landing | veliform.com (Vercel `porqa`) |
| voice | josefwebdeveloper/voice-agent | Railway |

---

## 8. ClickUp — куда смотреть в работе

**Workspace:** Joseph Shain · Space **VeliForm**

| Папка / List | Для чего |
|--------------|----------|
| **Company Site → 🌐 SEO & Marketing** | SEO Agent, Marketing Analyst outputs, контент, CWV |
| **Company Site → 🏗 Company HQ** | HQ, Notion sync, новые агенты в org.yaml |
| **Company Site → 📋 Backlog** | Идеи без репо (Crewdesk epic) |
| **Voice Agents** *(отдельная папка)* | Voice runtime, Launchpad, tenant'ы, Railway |

Marketing Analyst **сам** создаёт задачи в SEO & Marketing. Человек закрывает их после выполнения.

Подробнее: [`CLICKUP_VELIFORM.md`](CLICKUP_VELIFORM.md)

---

## 9. HQ Dashboard — как читать экран

URL: [veliform.com/hq](https://veliform.com/hq) (пароль — env `HQ_PASSWORD` на Vercel).

| Блок | Что показывает |
|------|----------------|
| **Org map** | Отделы, люди, агенты — из `org.yaml` (обновляется при деплое landing) |
| **Agent roster** | Имя, тип (voice/automation), focus, tools, status + Last touch из Notion |
| **Product board** | Продукты/workstream'и: Stage, Tier, Next action |
| **Activity stream** | CEO Updates: git, cursor, voice, manual, deploy |
| **Plans rail** | Крупные инициативы из org.yaml |

**Статусы агентов:** `live` / `active` — работает в prod; `beta` — ограниченно; `planned` — в спеке/roadmap.

HQ **не** заменяет ClickUp для задач. HQ — «как выглядит AI-компания и что недавно произошло».

---

## 10. Типичный день компании (сквозной сценарий)

1. **Утро:** Marketing Analyst (если schedule включён) проверил GA4 — падения нет, задач не создал.
2. **Клиент** зашёл на veliform.com → AI Architect → событие в GA4 → возможная weekly-задача «усилить страницу X».
3. **Prospect** позвонил на demo-номер Rose → заказ или handoff → запись в business DB, Telegram owner.
4. **Josef** звонит на personal line → Alice: «что в календаре?», «что по Voice?» → read Notion CEO.
5. **Незнакомый** звонит на тот же personal → Secretary принимает сообщение.
6. **Разработчик** пушит fix в `voice-agent` main → GitHub CI → CEO Update → строка в HQ activity stream.
7. **SEO правка** на landing → задача в ClickUp Done + push → Update `veliform-landing`.

---

## 11. Для нового человека в команде

### С чего начать (30 минут)

1. Прочитать этот документ.
2. Открыть [veliform.com/hq](https://veliform.com/hq) — увидеть roster и activity.
3. Открыть Notion CEO Projects — стадии `veliform-voice`, `veliform-company`.
4. ClickUp → VeliForm → пробежать открытые задачи в SEO & Marketing и Voice Agents.
5. Позвонить на demo Rose (номер в admin / PRODUCT_ARCHITECTURE) — услышать продукт.

### Где что искать

| Вопрос | Куда |
|--------|------|
| Что делать сегодня? | ClickUp |
| На какой стадии продукт? | Notion CEO Projects |
| Что изменилось вчера? | HQ Activity / Notion CEO Updates |
| Как устроен Voice? | `voice/docs/PRODUCT_ARCHITECTURE.md` |
| Launchpad для клиентов? | `voice/docs/VOICE_LAUNCHPAD.md` |
| Как логировать работу? | CEO Steward skill / Notion CEO Updates |

### Чего не делать

- Не дублировать CEO Updates текстом в ClickUp description.
- Не менять production env на Vercel project `veliform-landing` — prod на **`porqa`**.
- Не смешивать Personal и Business сценарии Voice.

---

## 12. Для клиентов — что вы получаете

| Обещание | Как мы это делаем |
|----------|-------------------|
| AI отвечает на звонки 24/7 | Business Platform, tenant на ваш номер, vertical tools |
| Агент знает ваш бизнес | Launchpad: анализ сайта → prompt + tools → тестовый звонок |
| Эскалация на человека | Handoff на ваш mobile; Secretary-паттерн для личных линий |
| Вас находят в Google | SEO Agent + Marketing Analyst на вашем сайте (или аналог as a service в Crewdesk) |
| Понятный план до старта | AI Architect на veliform.com или консультация с командой |

**Пилот сейчас:** invite-only concierge — мы помогаем пройти онбординг вручную, пока Launchpad и billing не в public beta.

---

## 13. Глоссарий

| Термин | Значение |
|--------|----------|
| **Tenant** | Отдельный бизнес на Business Platform (свой номер, persona, tools) |
| **Workstream slug** | ID репозитория в Notion CEO (`voice-agent`, `veliform-landing`) |
| **Product slug** | ID продукта (`veliform-voice`, `veliform-company`) |
| **Handoff** | Перевод звонка на живого человека |
| **CEO Update** | Строка в Notion — «что произошло» |
| **Dogfooding** | Используем свои же агенты/HQ как прототип будущего SaaS (Crewdesk) |

---

## 14. Связанные документы

- [COMPANY_HQ.md](COMPANY_HQ.md) — HQ технически
- [NOTION_CEO.md](NOTION_CEO.md) — настройка Notion
- [TASK_SYNC.md](TASK_SYNC.md) — три слоя
- [CLICKUP_VELIFORM.md](CLICKUP_VELIFORM.md) — списки ClickUp
- [MARKETING_AGENT.md](MARKETING_AGENT.md) — Marketing Analyst
- `voice/docs/PRODUCT_ARCHITECTURE.md` — архитектура Voice
- `voice/docs/VOICE_LAUNCHPAD.md` — онбординг клиентов Voice

---

*Вопросы по документу → задача в ClickUp **🏗 Company HQ** или правка этого файла в `meta/docs/`.*
