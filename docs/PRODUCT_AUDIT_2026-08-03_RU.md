# Veliform: продуктовый аудит и план выхода к выручке

**Дата:** 2026-08-03  
**Фокус:** Veliform Voice  
**Режим принятия решений:** факты из кода и реестра отделены от гипотез

## 1. Решение

Veliform не должен сейчас строить ещё одну широкую AI-платформу. Главный продукт — **управляемый голосовой сотрудник для одного повторяемого бизнес-процесса**.

Принятые решения:

1. **Voice — единственный основной revenue workstream.**
2. **Hospitality — следующий коммерческий wedge.** Florist остаётся публичным proof demo; real estate остаётся прототипом до подтверждения hospitality.
3. **Никаких бесплатных “пилотов ради количества tenants”.** Цель — три платных design partner pilot с измеримым исходом.
4. **Launchpad остаётся закрытым**, пока identity/state machine, production knowledge runtime и readiness не подтверждены тестами.
5. **WeOffice остаётся dogfood-продуктом и максимум одним design partner.** Только Marketing Analyst называется live worker; остальные роли — preview.
6. **Маркетинг описывает только работающие возможности.** Неподтверждённые отзывы, выручка, “25 integrations”, “12 agents”, dental/HVAC и setup за три минуты удаляются.

Это не отказ от платформы. Это порядок доказательств: сначала воспроизводимая ценность и деньги, затем self-service и горизонтальное расширение.

## 2. Текущее положение

### Подтверждённые факты

| Показатель | Состояние |
|---|---:|
| MRR | $0 |
| Платящие Voice-клиенты | 0 |
| Публичный Voice demo | 1 florist tenant |
| Реализованные business toolkits | 3: florist, hospitality, real estate |
| Платящие WeOffice-клиенты | 0 |
| Live workers в WeOffice | 1: Marketing Analyst |
| Launchpad | код существует, публичный запуск paused |
| Основные языки Voice | Hebrew, Russian, English |

### Что Voice действительно делает

Фактический live path:

```text
Twilio webhook
  → проверка подписи
  → tenant по входящему номеру
  → подписанный Media Stream
  → OpenAI Realtime
  → tenant prompt + vertical tools
  → Postgres / SMS / Telegram / human handoff
```

Работающие business outcomes:

- florist: каталог, delivery slots, заказ, SMS, owner alert, handoff;
- hospitality: меню, dining capacity, reservation, waitlist, order, handoff;
- real estate: listings, lead capture, public web search, handoff;
- tenant-scoped data и блокировка cross-tenant mutation;
- personal assistant и secretary существуют, но не являются текущим B2B wedge;
- Copilot является beta-функцией, а не отдельным готовым SKU.

### Что нельзя продавать как готовое

- universal agent “из любого сайта за три минуты”;
- self-service SaaS onboarding;
- 25 integrations;
- dental, HVAC и произвольные verticals;
- отдельный production Copilot;
- customer portal, RBAC, billing и автоматический provisioning;
- доказанный ROI или customer testimonials;
- WeOffice как команду из десяти работающих агентов.

## 3. Почему выручки нет

### 3.1. Нет узкого коммерческого обещания

Сайт продавал одновременно receptionist, call center, chatbot, callback, personal assistant, copilot, dental, HVAC, POS и 25 integrations. Код решает более узкую и полезную задачу: **входящий звонок → структурированный бизнес-результат**.

Широкое обещание создаёт три потери:

1. лид не понимает, для какого звонка покупать продукт;
2. sales обещает scope, который engineering не может быстро повторить;
3. доверие падает при переходе из “website import” в общий florist demo.

### 3.2. Измеряется наличие функций, а не outcome

Количество agents, integrations и tenants не доказывает ценность. Для Voice единица ценности:

```text
звонок отвечен
→ намерение определено
→ бизнес-действие завершено
→ подтверждение доставлено
или
→ корректный handoff выполнен
```

### 3.3. Фокус разделён между тремя продуктами

Voice, WeOffice и Launchpad одновременно требуют GTM, reliability, auth, billing и support. Для компании с одним human founder это три параллельных стартапа.

### 3.4. Production quality ещё не измеряется

До этого аудита отсутствовал единый call lifecycle: начало, первый audio, tool result, handoff, disconnect, duration, outcome и provider error. Без него невозможно доказать SLA, найти drop-off и посчитать cost per completed outcome.

## 4. ICP и JTBD

### Primary ICP

Независимый ресторан, кафе или небольшая hospitality-группа, где:

- телефонные запросы повторяются;
- персонал занят обслуживанием гостей;
- есть понятные часы, меню, capacity и правила бронирования;
- пропущенный звонок означает потерянную бронь или заказ;
- владелец готов выделить безопасный pilot scope и human fallback.

### Primary JTBD

> Когда персонал не может поднять трубку, я хочу, чтобы звонок завершился бронью, заказом или корректной передачей человеку, чтобы не терять выручку и не отвлекать команду от гостей.

### Не ICP сейчас

- enterprise contact center;
- регулируемые medical/payment flows;
- outbound campaigns;
- бизнес без структурированных данных и правил;
- клиент, требующий десять integrations до первого pilot;
- покупатель “универсального AI-сотрудника”.

## 5. Почему hospitality

Это продуктовая гипотеза, которую нужно подтвердить продажами, но она лучше согласована с текущим кодом:

| Критерий | Hospitality | Real estate |
|---|---|---|
| Частота повторяемых звонков | высокая | ниже и неравномерна |
| Outcome | reservation/order/waitlist | lead |
| Мгновенная ценность | понятна владельцу | зависит от последующей продажи |
| Runtime в коде | capacity + locking + waitlist + orders | listings + lead capture |
| Integration burden | можно начать с внутреннего inventory | быстро нужен актуальный CRM/feed |
| Pilot feedback cycle | короткий | длиннее |

Florist остаётся публичным доказательством end-to-end commerce, но не обязан быть главным сегментом продаж.

## 6. Новый коммерческий оффер

### Формулировка

**Managed AI receptionist pilot for one repeatable call workflow.**

В pilot входят:

- карта call intents и запретных сценариев;
- tenant-scoped business data;
- один основной outcome;
- язык и голос;
- SMS/owner notification, если применимо;
- explicit handoff и fallback;
- staff acceptance test;
- weekly outcome review;
- лимиты usage и аварийное отключение.

### Pricing hypothesis

Цена должна исходить из сохранённой брони/заказа, а не из стоимости LLM.

Проверяемая гипотеза:

- setup fee покрывает конфигурацию и acceptance testing;
- monthly base включает согласованный объём минут;
- overage прозрачен;
- pilot всегда платный, даже если цена снижена;
- скидка обменивается на доступ к метрикам и structured feedback, а не на testimonial.

Точный price point нельзя объявлять фактом до customer interviews и первых invoices.

## 7. North-star metric и scorecard

### North-star

**Completed business outcomes per 100 eligible calls.**

Eligible call — звонок, соответствующий согласованному pilot scope.

### Acquisition

| Metric | Зачем |
|---|---|
| `/voice` sessions | размер верхней воронки |
| demo click rate | интерес к реальному продукту |
| pilot application click rate | коммерческий intent |
| qualified applications | качество ICP |
| application → paid pilot | эффективность продажи |

### Activation

| Metric | Цель gate |
|---|---:|
| config acceptance tests passed | 100% |
| staff test calls completed | обязательный gate |
| unsafe/unsupported intents documented | 100% |
| handoff path verified | 100% |

### Runtime

| Metric | Initial target |
|---|---:|
| webhook / stream authentication failures | 0 unexplained |
| call connection success | ≥95% |
| p95 first audio latency | <2.5 s |
| tool-call success | ≥98% |
| completed outcome rate | baseline per workflow, then improve |
| successful human handoff | ≥95% of requested handoffs |
| calls missing lifecycle record | 0 |
| cross-tenant incidents | 0 |
| provider cost / completed outcome | tracked on every pilot |

Targets являются operating thresholds, а не уже достигнутыми результатами.

### Revenue

- paid pilots;
- pilot MRR;
- gross margin after Twilio + OpenAI + support;
- pilot → retained subscription;
- expansion from one workflow to a second;
- revenue per completed outcome.

## 8. Release gates

### Gate A — reliable managed pilot

- full automated suite green;
- migration rehearsal green;
- proactive greeting verified;
- provider errors and call lifecycle recorded;
- tool/handoff failures visible;
- no PII in application logs;
- SSRF and stored XSS closed;
- rollback and manual kill switch documented.

### Gate B — repeatable vertical

- three paying hospitality pilots;
- same onboarding checklist used without custom code forks;
- one primary workflow reaches an agreed outcome threshold;
- support effort and gross margin measured;
- at least one customer renews without a founder-created feature sprint.

### Gate C — self-service

Launchpad may reopen only when:

- account sessions authorize project APIs;
- anonymous token rotates after claim;
- OTP never appears outside explicit test mode;
- configuration is immutable during review;
- knowledge survives activation into production runtime;
- readiness is based on observed tool behavior, not checkboxes;
- provisioning is idempotent;
- billing and tenant admin exist.

## 9. Engineering priorities

### P0 — before adding capabilities

1. Call lifecycle and status callbacks:
   - initiated, connected, first audio, completed, disconnected;
   - duration, outcome, tool failures, handoff result;
   - idempotent Twilio callbacks.
2. Make the full test matrix green:
   - business and personal product isolation;
   - migration head/drift;
   - clean DB → head and legacy → head.
3. Finish Launchpad identity/state hardening before enabling `/start`.
4. Remove startup schema mutation; Alembic becomes the only schema owner.
5. Add CI for tests, migrations, static security checks, and deploy smoke.

### Уже исправлено этим delivery

- assistant explicitly greets first;
- generic web fetch revalidates DNS and redirects, pins the connection, and caps bytes;
- tool/caller PII is removed from logs;
- Telegram webhook fails closed without secret;
- Twilio transfer/hangup no longer block the media loop and handle API failures;
- admin renders untrusted values as text instead of executable HTML;
- public Voice page now matches implemented capabilities and tracks demo/pilot conversions;
- WeOffice local demo no longer requires Clerk hooks;
- cron and migration endpoints fail closed without `CRON_SECRET`;
- simulated WeOffice roles are labelled preview.

### P1 — after runtime evidence

- outbox/queue for SMS, Telegram, and external side effects;
- per-tenant credentials and customer access;
- pilot dashboard with call outcome review;
- configurable retention/deletion and consent evidence;
- CRM/POS integration chosen by the first paying vertical, not by a generic roadmap.

## 10. Что не строить сейчас

- новый vertical до Gate B;
- WhatsApp/chat omnichannel;
- separate Copilot deployment;
- billing UI before a manual paid invoice proves willingness to pay;
- universal website-to-agent generation;
- more WeOffice catalog roles;
- “AI call center for 2,500 locations” infrastructure;
- vanity dashboard without actionable call outcomes.

## 11. WeOffice

WeOffice не закрывается, но меняет роль:

- продуктовая лаборатория и dogfood для Veliform operations;
- Marketing Analyst — единственный live worker;
- остальные роли — preview until connected worker + tests + observable output;
- no Stripe work before one design partner repeatedly uses the live worker;
- Voice и WeOffice не объединяются в runtime: cross-sell возможен только после отдельного PMF.

## 12. Главные риски

| Риск | Контроль |
|---|---|
| Founder bottleneck | один vertical, один workflow, standard checklist |
| Voice quality / latency | first-audio and interruption telemetry |
| Hallucinated business facts | tenant-scoped data + tool-only critical facts |
| Provider outage | scripted fallback + Twilio action/fallback URL |
| Compliance | disclosure, consent, retention, no medical/payment pilot |
| Cost overrun | hard call cap + cost/outcome |
| Custom-work trap | no pilot requiring a code fork |
| Reputation | only verified claims and attributable case studies |

## 13. Следующее управленческое действие

Не открывать новый feature sprint. Провести продажи по одному hospitality offer и одновременно закрыть runtime observability/test gate.

Каждый новый запрос оценивается одним вопросом:

> Повышает ли это долю успешно завершённых reservation/order calls у текущего платного pilot?

Если нет — задача не P0.
