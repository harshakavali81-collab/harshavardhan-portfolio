# Portfolio verification results

Generated UTC: 2026-10-28T08:22:21.691726+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 111.5 | 346.5 |
| work.html | 126.0 | 402.5 |
| evidence.html | 206.5 | 412.0 |
| engineering.html | 112.0 | 350.0 |
| proof-map.html | 75.5 | 390.0 |
| hiring.html | 62.0 | 314.5 |
| interview.html | 107.5 | 345.5 |
| profile.html | 96.5 | 349.0 |
| contact.html | 115.5 | 383.5 |
| resumes.html | 97.5 | 300.5 |
| quality.html | 106.5 | 356.0 |
| cases/demandpilot.html | 98.5 | 330.0 |
| cases/transactionshield.html | 59.0 | 365.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
