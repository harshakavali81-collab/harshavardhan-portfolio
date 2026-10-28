# Portfolio verification results

Generated UTC: 2026-10-28T08:14:47.958274+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 206.5 | 337.0 |
| work.html | 376.5 | 380.5 |
| evidence.html | 140.5 | 481.5 |
| engineering.html | 185.5 | 372.5 |
| proof-map.html | 212.5 | 373.5 |
| hiring.html | 90.0 | 426.5 |
| interview.html | 204.5 | 358.0 |
| profile.html | 193.5 | 237.0 |
| contact.html | 211.5 | 437.5 |
| resumes.html | 203.5 | 210.5 |
| quality.html | 119.0 | 364.0 |
| cases/demandpilot.html | 203.0 | 385.5 |
| cases/transactionshield.html | 87.5 | 438.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
