# Portfolio verification results

Generated UTC: 2026-10-28T07:37:18.045350+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 51.0 | 347.5 |
| work.html | 46.0 | 360.5 |
| proof-map.html | 49.5 | 377.0 |
| hiring.html | 48.0 | 293.0 |
| interview.html | 41.5 | 300.5 |
| profile.html | 24.5 | 204.0 |
| contact.html | 48.0 | 359.5 |
| resumes.html | 22.0 | 208.0 |
| quality.html | 32.0 | 329.5 |
| cases/demandpilot.html | 27.0 | 378.5 |
| cases/transactionshield.html | 31.0 | 365.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
