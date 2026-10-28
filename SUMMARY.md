# Portfolio verification results

Generated UTC: 2026-10-28T07:20:03.483090+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 60.0 | 350.5 |
| work.html | 86.5 | 359.0 |
| proof-map.html | 63.0 | 382.5 |
| hiring.html | 48.5 | 337.0 |
| interview.html | 72.5 | 337.5 |
| profile.html | 43.0 | 233.0 |
| contact.html | 70.5 | 363.5 |
| resumes.html | 39.0 | 217.5 |
| quality.html | 49.0 | 333.5 |
| cases/demandpilot.html | 46.5 | 375.0 |
| cases/transactionshield.html | 52.0 | 342.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
