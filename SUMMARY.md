# Portfolio verification results

Generated UTC: 2026-10-28T08:34:02.472244+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 33 reachable; 0 broken; 107 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 135/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 333.5 | 1049.0 |
| work.html | 473.5 | 1368.0 |
| evidence.html | 431.5 | 1399.5 |
| engineering.html | 169.0 | 981.0 |
| proof-map.html | 263.5 | 1408.5 |
| hiring.html | 267.5 | 984.0 |
| interview.html | 171.0 | 1335.5 |
| profile.html | 270.0 | 1044.5 |
| contact.html | 341.5 | 984.0 |
| resumes.html | 260.0 | 967.5 |
| quality.html | 297.5 | 983.5 |
| cases/demandpilot.html | 149.0 | 984.5 |
| cases/transactionshield.html | 149.5 | 984.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
