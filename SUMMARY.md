# Portfolio verification results

Generated UTC: 2026-10-28T08:23:32.652013+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 101.0 | 397.0 |
| work.html | 162.5 | 441.0 |
| evidence.html | 134.0 | 451.5 |
| engineering.html | 110.0 | 414.0 |
| proof-map.html | 88.0 | 422.0 |
| hiring.html | 111.5 | 387.5 |
| interview.html | 111.0 | 366.0 |
| profile.html | 105.0 | 330.0 |
| contact.html | 98.0 | 406.0 |
| resumes.html | 118.5 | 385.0 |
| quality.html | 75.5 | 379.5 |
| cases/demandpilot.html | 80.0 | 392.0 |
| cases/transactionshield.html | 101.0 | 391.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
