# Portfolio verification results

Generated UTC: 2026-10-28T07:39:16.460929+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 54.5 | 360.5 |
| work.html | 70.5 | 363.0 |
| evidence.html | 66.5 | 398.0 |
| engineering.html | 47.0 | 370.0 |
| proof-map.html | 62.0 | 375.0 |
| hiring.html | 49.5 | 367.0 |
| interview.html | 57.0 | 362.5 |
| profile.html | 41.0 | 236.5 |
| contact.html | 61.5 | 368.5 |
| resumes.html | 41.0 | 218.5 |
| quality.html | 44.0 | 370.5 |
| cases/demandpilot.html | 49.0 | 381.5 |
| cases/transactionshield.html | 50.5 | 377.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
