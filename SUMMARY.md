# Portfolio verification results

Generated UTC: 2026-10-28T07:47:57.221031+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 99 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 37.0 | 316.0 |
| work.html | 43.5 | 353.5 |
| evidence.html | 46.0 | 367.5 |
| engineering.html | 30.5 | 319.5 |
| proof-map.html | 51.5 | 357.0 |
| hiring.html | 26.0 | 348.5 |
| interview.html | 25.5 | 318.5 |
| profile.html | 22.0 | 230.5 |
| contact.html | 41.5 | 348.5 |
| resumes.html | 22.5 | 200.5 |
| quality.html | 29.5 | 319.0 |
| cases/demandpilot.html | 32.5 | 327.0 |
| cases/transactionshield.html | 27.0 | 357.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
