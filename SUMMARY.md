# Portfolio verification results

Generated UTC: 2026-10-28T08:31:03.899117+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 106 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 50.0 | 356.5 |
| work.html | 103.0 | 417.0 |
| evidence.html | 108.0 | 425.5 |
| engineering.html | 41.0 | 321.5 |
| proof-map.html | 52.5 | 413.5 |
| hiring.html | 42.0 | 402.5 |
| interview.html | 43.5 | 391.0 |
| profile.html | 41.0 | 361.0 |
| contact.html | 59.0 | 395.0 |
| resumes.html | 44.0 | 341.0 |
| quality.html | 44.0 | 359.0 |
| cases/demandpilot.html | 42.5 | 335.5 |
| cases/transactionshield.html | 38.5 | 376.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
