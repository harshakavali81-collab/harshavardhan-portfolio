# Portfolio verification results

Generated UTC: 2026-10-28T07:50:16.513700+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 99 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 57.5 | 327.0 |
| work.html | 73.5 | 364.0 |
| evidence.html | 75.5 | 382.0 |
| engineering.html | 45.0 | 359.0 |
| proof-map.html | 52.0 | 369.0 |
| hiring.html | 46.0 | 353.5 |
| interview.html | 47.0 | 354.5 |
| profile.html | 40.5 | 229.5 |
| contact.html | 57.0 | 354.0 |
| resumes.html | 43.5 | 205.5 |
| quality.html | 87.5 | 352.0 |
| cases/demandpilot.html | 46.5 | 366.0 |
| cases/transactionshield.html | 47.0 | 332.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
