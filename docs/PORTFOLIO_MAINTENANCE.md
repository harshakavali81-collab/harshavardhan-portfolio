# Portfolio maintenance and verification runbook

This guide is for maintaining the public, static GitHub Pages portfolio at
https://harshakavali81-collab.github.io/harshavardhan-portfolio/.

## Architecture

```text
Browser (public HTTPS)
  │
  ├─ index.html                    : candidate home and featured projects
  ├─ work.html / cases/*.html       : five detailed case studies
  ├─ evidence.html                  : interactive source-backed evidence register
  │    ├─ assets/evidence.js        : filter + compare, no external framework
  │    ├─ assets/evidence.css       : accessible responsive styling
  │    └─ data/project-evidence.json: metric/provenance single source
  ├─ engineering.html               : decision log and reproduction boundaries
  ├─ profile.html / hiring.html     : complete profile and recruiter facts
  ├─ interview.html / proof-map.html: role-specific interview evidence
  ├─ resumes.html                   : downloadable role-specific PDFs
  ├─ contact.html                   : copy/Gmail/mailto composer (no backend)
  └─ quality.html                   : recorded QA results and methodology
        │
        └─ GitHub Actions           : static audit, live browser and link QA
```

All pages are static assets. The evidence register loads JSON from the same GitHub Pages origin and does **not** transmit candidate or visitor form data to an application server.

## Safe editing procedure

1. Change the relevant HTML, CSS, JavaScript, and, for metrics, `data/project-evidence.json`.
2. Update the matching `cases/<slug>.html` and `docs/ENGINEERING_DECISIONS.md` if a project result changes.
3. Preserve source URLs, unit labels and dataset provenance with every metric.
4. Keep the About/Hiring Desk facts synchronized with the candidate-supplied resumes, with no invented salary or employment tenure.
5. For privacy, do not expose national IDs, passwords, date of birth or private addresses in public project files.
6. Before merging/pushing, run:

```bash
python3 scripts/audit_site.py
```

7. Check GitHub Actions for **Portfolio quality checks**, **pages build and deployment**, and **Live performance and browser QA**. The last run publishes `SUMMARY.md`, JSON records and representative screenshots on the `qa-reports` branch.
8. Open all modified pages in a real browser and inspect mobile width. CI Chromium/Firefox/WebKit engines are simulated browser environments, not physical phone certification.

## Reproducing site QA

- Source: `scripts/audit_site.py` checks local file/link existence, HTML IDs, images and all six deep case-study sections. It only traverses public portfolio pages under the project root and `cases/`, not separate nested frontend projects.
- Source: `scripts/live_qa.py` checks published URLs, public external links, link reachability classification, desktop/tablet/mobile viewport layouts, interactions, and p75 navigation load-event timing in desktop and a specified synthetic mobile 4G profile.
- Workflow: `.github/workflows/live-qa.yml` runs on relevant pushes, manual trigger and weekly schedule; artifact retention is limited to 30 days.
- A HTTP 403, 429, or LinkedIn 999 is **unknown/access-restricted**, not automatically a broken link or a successful retrieval.
- Historical speed measurements apply only to the tested run and simulator settings; don't claim every real user loads under three seconds.

## Project evidence checks

- [Evidence Ledger](../evidence.html) uses data from `data/project-evidence.json`.
- [Engineering Notebook](../engineering.html) details major trade-offs and known gaps.
- [Source-by-source ADRs](ENGINEERING_DECISIONS.md) identifies exactly what can be independently read.
- Binary reports, unpublished API integrations and real production security assurances must not be described as verified unless there is clear evidence.

## Release validation and rollback

- Use `main` for releases. GitHub built-in **pages build and deployment** publishes the checked-in static repository. The separate `pages.yml` compiles a MobilityPulse React **build artifact** for download and does not deploy or modify the Pages site.
- Verify the most recent successful commit SHA and page URL in GitHub Actions; do not confuse a passed HTML audit with a fully passed live browser suite.
- On regression, revert the introducing commit through GitHub, then repeat deployment and QA checks.
- GitHub Pages requires no visitor login. The content owner's login is the GitHub account, **not** a credential issued by this portfolio.
- Publishing personal resume contact details makes them public on the web; confirm that is desired when adding new contact information.

## Accessibility and privacy

- Use semantic heading levels, descriptive link text, labeled controls, visible keyboard focus, alt text for actual images, and a skip-to-content link.
- The contact form supports copying a complete message, an optional Gmail popup and the installed mail app. No visitor message is transmitted to this portfolio. Clipboard-denied browsers reveal a selectable fallback.
- Static pages do not install custom analytics or a contact-collection backend. GitHub/other linked platforms have their own hosting, analytics and privacy policies.
- Never advertise independent physical-device QA, WCAG certification, genuine real-time integrations, or production ML performance without appropriate evidence.

## Optional future upgrades (not yet verified)

- Run a real Lighthouse/Web Vitals audit on an independent location and compare page experience, not merely the load event.
- Audit project-source binary report refreshes with the intended desktop applications.
- Ask domain reviewers to examine any model used in healthcare, disaster response, payments or other high-stakes settings.
- Consider a custom domain only when the owner has DNS access and can validate HTTPS and redirects.


## Latest deployment and QA alignment

GitHub Pages built-in deployment succeeded for commit `b4d9d48` on 28 October 2026. A previous custom deployment failed at `actions/configure-pages` because of integration permissions and rate limits. It now produces a downloadable React build artifact rather than deploying to Pages.

Browser QA now reads actual counts from `data/project-evidence.json` (seven records, three ML records as of 28 October 2026), tests the Gmail **popup** instead of same-tab navigation, and verifies the full-message copy action. The React artifact must be separately integrated into deployment if serving that exact React build publicly is desired. The checked-in `mobilitypulse-demo/index.html` remains the existing static demo.
