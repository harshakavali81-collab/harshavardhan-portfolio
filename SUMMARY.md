# Portfolio verification results

Generated UTC: 2026-10-28T08:31:37.583396+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 107 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 52.0 | 354.0 |
| work.html | 49.5 | 408.5 |
| evidence.html | 59.5 | 423.5 |
| engineering.html | 40.5 | 323.0 |
| proof-map.html | 53.0 | 405.0 |
| hiring.html | 42.0 | 398.0 |
| interview.html | 43.0 | 356.0 |
| profile.html | 44.5 | 400.0 |
| contact.html | 59.5 | 390.5 |
| resumes.html | 43.0 | 307.0 |
| quality.html | 42.5 | 330.5 |
| cases/demandpilot.html | 41.5 | 374.5 |
| cases/transactionshield.html | 39.0 | 368.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
