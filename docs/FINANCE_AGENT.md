# Finance Analyst — autonomous spend monitoring

Finance Analyst watches **Veliform company infrastructure spend** (Railway first; Vercel/Twilio/OpenAI later). It runs in `josefwebdeveloper/veliform-landing` via GitHub Actions — same pattern as Marketing Analyst.

## Outputs

- **Pulse (every 2 hours):** read Railway usage; **Telegram alert only on anomalies** (no spam when spend is OK).
- **Weekly (Monday):** full snapshot → Notion CEO Updates + Telegram digest + optional ClickUp task on **🏗 Company HQ** list (`901819936119`).
- Every run: JSON artifact retained 30 days.

## Schedule

When `FINANCE_SCHEDULE_ENABLED=true` (repo variable):

| Mode | Cron (UTC) | Approx Israel (summer) |
|------|------------|-------------------------|
| Pulse | `0 */2 * * *` | every 2 hours |
| Weekly | `0 7 * * 1` | Monday ~10:00 |

## Alerts (configurable in `config/finance-agent.json`)

- Estimated Railway bill ≥ **$8** (warn) or **$15** (critical)
- Burn pace ahead of billing period vs Hobby **$5** included credit
- `voice-agent` project dominates workspace spend (>65%)

## Secrets (`veliform-landing`)

| Secret | Purpose |
|--------|---------|
| `RAILWAY_TOKEN` | Railway API token (Account → Tokens) |
| `CLICKUP_API_TOKEN` | Same as Marketing Analyst |
| `NOTION_API_KEY` + CEO DB IDs | Weekly CEO Updates |
| `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` | Owner digest (same as Marketing) |

## Activation

1. Local test:

   ```bash
   cd veliform-landing
   python3 -m unittest tests.test_finance_agent
   python3 scripts/finance_agent.py --mode pulse --fixture tests/fixtures/finance/pulse.json --dry-run
   ```

2. GitHub Actions → **Autonomous finance agent** → mode `access`, `dry_run=true`.

3. Add `RAILWAY_TOKEN` secret if not present.

4. Run `pulse` with `dry_run=true`, then once with `dry_run=false`.

5. Enable schedule:

   ```bash
   gh variable set FINANCE_SCHEDULE_ENABLED \
     --repo josefwebdeveloper/veliform-landing \
     --body true
   ```

## Roadmap

- Vercel project usage / bandwidth
- Twilio spend
- OpenAI usage dashboard
- Stripe when billing goes live

HQ org registry: `meta/ceo/org.yaml` → agent `finance-analyst`.
