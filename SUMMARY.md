# Portfolio verification results

Generated UTC: 2026-10-28T12:13:39.929349+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 160 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 144/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 1291.5 | 1900.5 |
| work.html | 202.0 | 1682.5 |
| job-platforms.html | 189.5 | 1316.5 |
| evidence.html | 198.0 | 1682.5 |
| engineering.html | 187.5 | 1318.0 |
| proof-map.html | 179.5 | 1627.0 |
| hiring.html | 92.5 | 1298.5 |
| interview.html | 1824.5 | 1623.5 |
| profile.html | 216.5 | 1637.5 |
| contact.html | 176.5 | 1302.0 |
| resumes.html | 192.0 | 1255.0 |
| quality.html | 535.5 | 920.5 |
| cases/demandpilot.html | 106.5 | 1288.0 |
| cases/transactionshield.html | 88.0 | 1297.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
