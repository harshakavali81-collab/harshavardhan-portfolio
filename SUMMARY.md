# Portfolio verification results

Generated UTC: 2026-10-28T07:48:02.294061+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 83 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 156.0 | 344.5 |
| work.html | 130.0 | 368.5 |
| evidence.html | 217.0 | 370.5 |
| engineering.html | 74.0 | 355.5 |
| proof-map.html | 127.5 | 368.0 |
| hiring.html | 29.0 | 377.5 |
| interview.html | 26.5 | 326.0 |
| profile.html | 23.0 | 220.0 |
| contact.html | 42.5 | 356.0 |
| resumes.html | 20.5 | 206.0 |
| quality.html | 62.0 | 323.0 |
| cases/demandpilot.html | 25.5 | 369.0 |
| cases/transactionshield.html | 81.5 | 333.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
