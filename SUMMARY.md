# Portfolio verification results

Generated UTC: 2026-10-28T08:25:45.809992+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 67.5 | 303.5 |
| work.html | 81.5 | 405.0 |
| evidence.html | 74.0 | 429.5 |
| engineering.html | 72.5 | 366.5 |
| proof-map.html | 76.0 | 397.5 |
| hiring.html | 79.5 | 362.0 |
| interview.html | 75.0 | 380.0 |
| profile.html | 79.0 | 348.0 |
| contact.html | 74.5 | 392.0 |
| resumes.html | 69.5 | 358.0 |
| quality.html | 74.5 | 351.5 |
| cases/demandpilot.html | 73.0 | 359.0 |
| cases/transactionshield.html | 60.0 | 353.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
