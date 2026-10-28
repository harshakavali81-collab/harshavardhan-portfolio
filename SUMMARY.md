# Portfolio verification results

Generated UTC: 2026-10-28T08:29:59.618293+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 104 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 49.5 | 330.5 |
| work.html | 60.5 | 401.0 |
| evidence.html | 51.0 | 417.0 |
| engineering.html | 49.5 | 324.0 |
| proof-map.html | 63.0 | 390.5 |
| hiring.html | 37.5 | 360.0 |
| interview.html | 51.0 | 347.5 |
| profile.html | 52.5 | 352.5 |
| contact.html | 63.5 | 381.5 |
| resumes.html | 50.0 | 339.0 |
| quality.html | 50.5 | 356.0 |
| cases/demandpilot.html | 53.5 | 336.5 |
| cases/transactionshield.html | 50.0 | 307.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
