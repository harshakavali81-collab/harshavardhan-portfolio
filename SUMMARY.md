# Portfolio verification results

Generated UTC: 2026-10-28T06:44:23.577157+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 53 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 35.5 | 337.5 |
| work.html | 41.5 | 354.0 |
| proof-map.html | 48.0 | 380.5 |
| profile.html | 24.0 | 205.0 |
| contact.html | 45.5 | 372.0 |
| resumes.html | 22.0 | 200.5 |
| quality.html | 28.0 | 300.5 |
| cases/demandpilot.html | 27.0 | 345.0 |
| cases/transactionshield.html | 27.5 | 381.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
