# Portfolio verification results

Generated UTC: 2026-10-28T07:46:34.944094+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 83 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 56.0 | 337.0 |
| work.html | 78.0 | 359.5 |
| evidence.html | 77.5 | 375.5 |
| engineering.html | 46.5 | 325.0 |
| proof-map.html | 57.0 | 365.0 |
| hiring.html | 53.5 | 361.0 |
| interview.html | 38.5 | 304.0 |
| profile.html | 38.5 | 222.5 |
| contact.html | 59.0 | 358.5 |
| resumes.html | 36.5 | 206.0 |
| quality.html | 44.0 | 327.5 |
| cases/demandpilot.html | 40.0 | 333.5 |
| cases/transactionshield.html | 41.0 | 329.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
