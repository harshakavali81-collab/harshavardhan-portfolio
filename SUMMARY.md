# Portfolio verification results

Generated UTC: 2026-10-28T07:36:55.194115+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 43.5 | 341.5 |
| work.html | 54.0 | 353.0 |
| proof-map.html | 56.5 | 376.5 |
| hiring.html | 46.5 | 328.0 |
| interview.html | 38.0 | 356.5 |
| profile.html | 29.0 | 229.5 |
| contact.html | 90.5 | 357.5 |
| resumes.html | 31.0 | 188.5 |
| quality.html | 38.0 | 323.5 |
| cases/demandpilot.html | 35.0 | 333.5 |
| cases/transactionshield.html | 45.0 | 369.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
