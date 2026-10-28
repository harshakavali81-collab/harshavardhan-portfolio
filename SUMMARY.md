# Portfolio verification results

Generated UTC: 2026-10-28T08:12:39.155139+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 74.5 | 358.0 |
| work.html | 67.0 | 387.0 |
| evidence.html | 60.0 | 392.0 |
| engineering.html | 41.5 | 336.0 |
| proof-map.html | 64.0 | 387.5 |
| hiring.html | 171.5 | 341.5 |
| interview.html | 50.0 | 362.0 |
| profile.html | 43.0 | 232.0 |
| contact.html | 60.0 | 369.5 |
| resumes.html | 39.5 | 197.5 |
| quality.html | 46.5 | 375.0 |
| cases/demandpilot.html | 45.0 | 379.0 |
| cases/transactionshield.html | 48.0 | 375.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
