# Portfolio verification results

Generated UTC: 2026-10-28T12:52:37.904242+00:00

## Direct checks
- Live URL HTTP 200: 22/22
- External links: 161 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 173/176 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 500.5 | 1975.5 |
| career-portfolio.html | 276.0 | 1264.5 |
| work.html | 392.0 | 1724.5 |
| job-platforms.html | 411.5 | 1419.0 |
| evidence.html | 307.0 | 1794.0 |
| engineering.html | 181.0 | 1363.5 |
| proof-map.html | 410.5 | 1669.0 |
| hiring.html | 158.5 | 1344.5 |
| interview.html | 193.5 | 1670.5 |
| profile.html | 323.0 | 1474.0 |
| contact.html | 389.5 | 1415.0 |
| resumes.html | 247.5 | 1303.5 |
| quality.html | 173.0 | 1337.0 |
| cases/demandpilot.html | 238.5 | 976.0 |
| cases/transactionshield.html | 180.5 | 1621.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
