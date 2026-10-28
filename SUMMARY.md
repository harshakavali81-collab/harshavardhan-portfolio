# Portfolio verification results

Generated UTC: 2026-10-28T08:16:51.925276+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 115.5 | 343.0 |
| work.html | 201.0 | 409.0 |
| evidence.html | 187.5 | 377.0 |
| engineering.html | 66.0 | 323.0 |
| proof-map.html | 65.0 | 367.0 |
| hiring.html | 68.0 | 358.0 |
| interview.html | 217.0 | 324.5 |
| profile.html | 194.5 | 348.5 |
| contact.html | 158.5 | 387.5 |
| resumes.html | 103.0 | 351.0 |
| quality.html | 65.0 | 362.5 |
| cases/demandpilot.html | 63.0 | 366.0 |
| cases/transactionshield.html | 106.0 | 330.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
