# Portfolio verification results

Generated UTC: 2026-10-28T12:14:22.597325+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 160 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 144/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 293.5 | 1842.0 |
| work.html | 184.5 | 1647.0 |
| job-platforms.html | 551.5 | 1285.0 |
| evidence.html | 220.0 | 1652.5 |
| engineering.html | 359.5 | 1502.0 |
| proof-map.html | 136.0 | 1602.0 |
| hiring.html | 66.5 | 1269.5 |
| interview.html | 73.0 | 1609.0 |
| profile.html | 178.0 | 1409.0 |
| contact.html | 148.0 | 1288.0 |
| resumes.html | 75.5 | 1243.0 |
| quality.html | 69.5 | 1287.5 |
| cases/demandpilot.html | 356.0 | 1301.5 |
| cases/transactionshield.html | 75.0 | 1283.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
