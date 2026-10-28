# Portfolio verification results

Generated UTC: 2026-10-28T08:15:16.515707+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 121 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 39.5 | 345.0 |
| work.html | 52.5 | 372.5 |
| evidence.html | 53.0 | 375.0 |
| engineering.html | 29.5 | 324.5 |
| proof-map.html | 44.0 | 366.5 |
| hiring.html | 28.0 | 324.0 |
| interview.html | 28.5 | 330.5 |
| profile.html | 23.5 | 397.0 |
| contact.html | 42.5 | 355.0 |
| resumes.html | 19.0 | 204.5 |
| quality.html | 27.5 | 356.0 |
| cases/demandpilot.html | 30.5 | 329.5 |
| cases/transactionshield.html | 27.5 | 366.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
