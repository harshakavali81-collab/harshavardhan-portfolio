# Portfolio verification results

Generated UTC: 2026-10-28T08:25:59.628804+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 66.0 | 301.0 |
| work.html | 71.5 | 392.0 |
| evidence.html | 83.0 | 404.0 |
| engineering.html | 67.0 | 354.0 |
| proof-map.html | 84.0 | 382.5 |
| hiring.html | 60.0 | 385.0 |
| interview.html | 60.0 | 365.5 |
| profile.html | 72.5 | 377.0 |
| contact.html | 75.5 | 405.5 |
| resumes.html | 70.5 | 344.0 |
| quality.html | 61.5 | 327.0 |
| cases/demandpilot.html | 64.0 | 329.0 |
| cases/transactionshield.html | 60.5 | 352.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
