# Portfolio verification results

Generated UTC: 2026-10-28T08:26:41.400962+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 35 reachable; 0 broken; 102 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 53.5 | 432.5 |
| work.html | 217.0 | 423.0 |
| evidence.html | 324.0 | 447.5 |
| engineering.html | 161.5 | 393.5 |
| proof-map.html | 165.0 | 406.5 |
| hiring.html | 77.5 | 382.0 |
| interview.html | 76.5 | 385.5 |
| profile.html | 55.5 | 400.0 |
| contact.html | 70.0 | 402.5 |
| resumes.html | 162.0 | 343.0 |
| quality.html | 42.0 | 293.0 |
| cases/demandpilot.html | 53.0 | 378.5 |
| cases/transactionshield.html | 51.5 | 380.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
