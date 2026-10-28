# Portfolio verification results

Generated UTC: 2026-10-28T08:51:05.958312+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 145 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 435.0 | 1067.0 |
| work.html | 452.5 | 1376.5 |
| evidence.html | 265.0 | 1455.5 |
| engineering.html | 205.5 | 988.0 |
| proof-map.html | 301.0 | 1339.5 |
| hiring.html | 262.0 | 1033.0 |
| interview.html | 264.5 | 1410.0 |
| profile.html | 291.5 | 1053.5 |
| contact.html | 237.0 | 980.0 |
| resumes.html | 483.5 | 1022.0 |
| quality.html | 304.0 | 991.0 |
| cases/demandpilot.html | 195.0 | 1043.5 |
| cases/transactionshield.html | 270.5 | 990.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
