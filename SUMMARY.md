# Portfolio verification results

Generated UTC: 2026-10-28T09:31:59.983065+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 157 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 251.0 | 971.5 |
| work.html | 207.5 | 1341.5 |
| evidence.html | 227.0 | 1375.0 |
| engineering.html | 101.0 | 950.0 |
| proof-map.html | 151.0 | 1315.5 |
| hiring.html | 133.5 | 954.5 |
| interview.html | 95.0 | 1316.0 |
| profile.html | 83.0 | 943.5 |
| contact.html | 137.0 | 955.0 |
| resumes.html | 91.0 | 928.0 |
| quality.html | 89.5 | 949.5 |
| cases/demandpilot.html | 109.0 | 946.5 |
| cases/transactionshield.html | 83.0 | 947.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
