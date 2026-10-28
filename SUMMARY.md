# Portfolio verification results

Generated UTC: 2026-10-28T07:46:17.548919+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 67 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 112.0 | 342.5 |
| work.html | 412.0 | 369.0 |
| evidence.html | 188.0 | 377.5 |
| engineering.html | 60.5 | 308.0 |
| proof-map.html | 356.0 | 374.0 |
| hiring.html | 279.0 | 412.0 |
| interview.html | 112.0 | 326.5 |
| profile.html | 74.5 | 216.5 |
| contact.html | 125.0 | 358.5 |
| resumes.html | 111.5 | 178.5 |
| quality.html | 114.5 | 411.5 |
| cases/demandpilot.html | 124.5 | 333.0 |
| cases/transactionshield.html | 120.0 | 408.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
