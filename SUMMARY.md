# Portfolio verification results

Generated UTC: 2026-10-28T08:15:05.330623+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 118 reachable; 0 broken; 0 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 47.0 | 377.0 |
| work.html | 56.5 | 391.0 |
| evidence.html | 69.5 | 390.5 |
| engineering.html | 29.0 | 369.5 |
| proof-map.html | 51.0 | 381.5 |
| hiring.html | 78.0 | 333.5 |
| interview.html | 54.5 | 339.0 |
| profile.html | 41.5 | 237.0 |
| contact.html | 68.0 | 372.5 |
| resumes.html | 41.5 | 229.0 |
| quality.html | 161.0 | 335.5 |
| cases/demandpilot.html | 54.5 | 401.0 |
| cases/transactionshield.html | 73.5 | 384.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
