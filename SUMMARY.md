# Portfolio verification results

Generated UTC: 2026-10-28T07:38:13.752592+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 311.0 | 373.0 |
| work.html | 90.5 | 377.0 |
| proof-map.html | 57.0 | 452.0 |
| hiring.html | 86.5 | 535.0 |
| interview.html | 102.5 | 374.5 |
| profile.html | 43.0 | 308.5 |
| contact.html | 92.0 | 378.0 |
| resumes.html | 41.0 | 289.5 |
| quality.html | 55.0 | 371.0 |
| cases/demandpilot.html | 179.5 | 398.5 |
| cases/transactionshield.html | 111.5 | 398.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
