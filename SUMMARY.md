# Portfolio verification results

Generated UTC: 2026-10-28T08:25:06.833921+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 67.5 | 375.5 |
| work.html | 165.5 | 435.5 |
| evidence.html | 132.0 | 438.5 |
| engineering.html | 77.0 | 344.5 |
| proof-map.html | 83.0 | 420.0 |
| hiring.html | 78.5 | 370.5 |
| interview.html | 73.0 | 401.0 |
| profile.html | 75.0 | 366.5 |
| contact.html | 96.5 | 414.0 |
| resumes.html | 76.0 | 376.5 |
| quality.html | 75.5 | 315.0 |
| cases/demandpilot.html | 70.0 | 385.5 |
| cases/transactionshield.html | 85.5 | 385.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
