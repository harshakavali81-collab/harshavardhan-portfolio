# Portfolio verification results

Generated UTC: 2026-10-28T08:20:27.302124+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 45.0 | 356.0 |
| work.html | 50.5 | 410.0 |
| evidence.html | 60.0 | 420.5 |
| engineering.html | 38.0 | 390.5 |
| proof-map.html | 50.5 | 402.0 |
| hiring.html | 35.5 | 353.5 |
| interview.html | 32.0 | 318.0 |
| profile.html | 30.0 | 403.0 |
| contact.html | 47.0 | 395.5 |
| resumes.html | 28.0 | 334.5 |
| quality.html | 27.0 | 354.0 |
| cases/demandpilot.html | 29.0 | 381.0 |
| cases/transactionshield.html | 29.0 | 379.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
