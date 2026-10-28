# Portfolio verification results

Generated UTC: 2026-10-28T08:25:13.731803+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 107.5 | 368.5 |
| work.html | 409.0 | 430.5 |
| evidence.html | 196.0 | 435.0 |
| engineering.html | 57.0 | 407.5 |
| proof-map.html | 111.0 | 420.0 |
| hiring.html | 73.5 | 374.5 |
| interview.html | 93.5 | 404.5 |
| profile.html | 114.5 | 401.5 |
| contact.html | 71.0 | 414.5 |
| resumes.html | 56.0 | 349.0 |
| quality.html | 75.5 | 392.5 |
| cases/demandpilot.html | 55.5 | 379.0 |
| cases/transactionshield.html | 53.0 | 383.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
