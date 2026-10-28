# Portfolio verification results

Generated UTC: 2026-10-28T07:36:30.626773+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 55.0 | 359.0 |
| work.html | 64.0 | 359.0 |
| proof-map.html | 60.0 | 368.5 |
| hiring.html | 47.0 | 332.5 |
| interview.html | 50.0 | 327.5 |
| profile.html | 39.5 | 211.0 |
| contact.html | 63.0 | 357.5 |
| resumes.html | 39.5 | 215.5 |
| quality.html | 46.5 | 300.0 |
| cases/demandpilot.html | 52.0 | 372.5 |
| cases/transactionshield.html | 47.0 | 372.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
