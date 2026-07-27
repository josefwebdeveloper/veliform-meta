# Marketing Analyst — autonomous reporting

Marketing Analyst monitors `veliform.com` without publishing content or changing ad
spend. It runs in `josefwebdeveloper/veliform-landing` through GitHub Actions.

## Outputs

- Daily: detect a material traffic or key-event drop. Create at most one ClickUp task.
- Weekly: compare GA4 and Search Console periods, rank evidence-backed opportunities,
  ask Gemini for wording/angles, create at most three ClickUp tasks, and append one
  Notion CEO update.
- Every run: put a readable summary in GitHub Actions and retain a JSON artifact for
  30 days.

Tasks go to ClickUp list `SEO & Marketing` (`901819936121`). Notion uses workstream
slug `veliform-landing`. The HQ activity feed receives the Notion update automatically.

After each **daily** or **weekly** run (when not `dry_run`), a compact digest is sent to
Telegram (`TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` GitHub secrets — same bot as Voice).

From the owner Telegram bot (personal-server):

- `/marketing status` — last Notion marketing report
- `/marketing run` — trigger daily check now
- `/marketing run weekly` — trigger full weekly report

Requires `MARKETING_GITHUB_TOKEN` on **personal-server** Railway (PAT with `workflow` scope).

## Schedule

When `MARKETING_SCHEDULE_ENABLED=true` (repo variable):

- **Daily** anomaly check: **twice daily** at 05:00 and 17:00 UTC (~08:00 and ~20:00 Israel summer)
- **Weekly** full report: Monday 06:00 UTC (~09:00 Israel summer)

## Safety model

- Google access is read-only.
- Search queries are untrusted input and are never treated as agent instructions.
- Gemini may select only opportunity IDs produced by deterministic analysis.
- Low-traffic samples do not generate anomaly alerts.
- Existing ClickUp fingerprints prevent duplicate tasks.
- Content publishing, repository writes, ad changes, and budget changes are not
  available to the scheduled agent.
- Scheduled runs remain disabled until the access audit and one manual live run pass.

## One-time Google setup

The site loads GA4 measurement tag `G-KW31ZW9NMY`. This is not the numeric
GA4 property ID required by the Data API.

1. In Google Cloud, create or select a project.
2. Enable **Google Analytics Data API** and **Google Search Console API**.
3. Create a service account and download one JSON key.
4. In GA4 Admin, add the service-account email as **Viewer** to the Veliform property.
5. In Search Console, verify `veliform.com` if needed and add the same email as a
   user for `sc-domain:veliform.com`.
6. Record the numeric GA4 property ID from GA4 Admin.

This setup is the only required Google-console involvement. Do not send the JSON key
through chat or commit it.

## GitHub configuration

Configure these repository secrets on `josefwebdeveloper/veliform-landing`:

- `GOOGLE_SERVICE_ACCOUNT_JSON`
- `GA4_PROPERTY_ID`
- `GSC_SITE_URL` (`sc-domain:veliform.com`)
- `GEMINI_API_KEY`
- `CLICKUP_API_TOKEN`
- Existing `NOTION_API_KEY`
- Existing `NOTION_CEO_PROJECTS_DATABASE_ID`
- Existing `NOTION_CEO_UPDATES_DATABASE_ID`

Safe CLI examples:

```bash
gh secret set GOOGLE_SERVICE_ACCOUNT_JSON \
  --repo josefwebdeveloper/veliform-landing < service-account.json
gh secret set GA4_PROPERTY_ID --repo josefwebdeveloper/veliform-landing
gh secret set GSC_SITE_URL --repo josefwebdeveloper/veliform-landing
gh secret set GEMINI_API_KEY --repo josefwebdeveloper/veliform-landing
gh secret set CLICKUP_API_TOKEN --repo josefwebdeveloper/veliform-landing
```

ClickUp MCP remains the interactive Cursor connection. The scheduled job needs a
ClickUp personal API token because an unattended GitHub runner cannot depend on the
interactive MCP OAuth session.

## Validation and activation

1. Local fixture test:

   ```bash
   npm run test:marketing
   python3 scripts/marketing_agent.py \
     --mode weekly \
     --fixture tests/fixtures/marketing/weekly.json \
     --dry-run
   ```

2. In GitHub Actions, run **Autonomous marketing agent** with mode `access` and
   `dry_run=true`. All four integrations must show `ok`.
3. Run mode `weekly` with `dry_run=true`; inspect the job summary and JSON artifact.
4. Run mode `weekly` once with `dry_run=false`; confirm no more than three ClickUp
   tasks and one Notion CEO update.
5. Enable scheduled runs:

   ```bash
   gh variable set MARKETING_SCHEDULE_ENABLED \
     --repo josefwebdeveloper/veliform-landing \
     --body true
   ```

The workflow uses UTC cron. Runs are approximately 08:00 daily and 09:00 Monday
during Israel summer time; they shift by one hour in winter.

## Configuration and events

Non-secret thresholds live in `veliform-landing/config/marketing-agent.json`.
Tracked events:

- `ai_consultation_started`
- `ai_consultation_completed`
- `book_consultation_click`
- `contact_email_click`

GA4 reports event counts immediately after collection. To include any event in the
GA4 `keyEvents` metric, mark it as a key event in GA4 Admin.

Technical SEO remains owned by `SEO Agent`; Marketing Analyst owns traffic,
conversion, search-demand, and content-opportunity analysis.
