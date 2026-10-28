# Portfolio verification results

Generated UTC: 2026-10-28T07:32:58.411478+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 133.0 | 309.5 |
| work.html | 103.5 | 360.0 |
| proof-map.html | 181.5 | 366.0 |
| hiring.html | 91.0 | 337.0 |
| interview.html | 100.0 | 335.0 |
| profile.html | 96.5 | 201.5 |
| contact.html | 107.0 | 359.5 |
| resumes.html | 77.5 | 215.5 |
| quality.html | 101.5 | 337.5 |
| cases/demandpilot.html | 72.0 | 312.0 |
| cases/transactionshield.html | 66.0 | 340.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
