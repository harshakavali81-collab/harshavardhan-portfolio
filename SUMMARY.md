# Portfolio verification results

Generated UTC: 2026-10-28T09:02:08.390946+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 150 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 235.5 | 979.5 |
| work.html | 177.0 | 1335.5 |
| evidence.html | 150.0 | 1362.0 |
| engineering.html | 67.0 | 942.5 |
| proof-map.html | 114.0 | 1302.0 |
| hiring.html | 59.0 | 935.5 |
| interview.html | 82.0 | 1297.0 |
| profile.html | 63.0 | 925.5 |
| contact.html | 115.0 | 940.0 |
| resumes.html | 66.5 | 920.5 |
| quality.html | 74.0 | 939.0 |
| cases/demandpilot.html | 60.5 | 933.0 |
| cases/transactionshield.html | 64.5 | 935.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
