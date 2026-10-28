# Portfolio verification results

Generated UTC: 2026-10-28T08:53:27.552102+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 145 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 461.0 | 1037.0 |
| work.html | 334.0 | 1432.0 |
| evidence.html | 325.0 | 1451.0 |
| engineering.html | 193.5 | 1030.0 |
| proof-map.html | 282.0 | 1398.5 |
| hiring.html | 247.0 | 1027.5 |
| interview.html | 175.0 | 1379.0 |
| profile.html | 252.0 | 1025.5 |
| contact.html | 312.0 | 1036.5 |
| resumes.html | 196.5 | 1014.0 |
| quality.html | 224.5 | 1037.5 |
| cases/demandpilot.html | 190.5 | 1040.5 |
| cases/transactionshield.html | 193.5 | 1040.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
