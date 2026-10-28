# Portfolio verification results

Generated UTC: 2026-10-28T08:58:51.140126+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 146 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 474.5 | 1004.5 |
| work.html | 421.0 | 1390.0 |
| evidence.html | 292.5 | 1405.5 |
| engineering.html | 166.5 | 996.0 |
| proof-map.html | 297.5 | 1342.0 |
| hiring.html | 212.0 | 997.5 |
| interview.html | 135.5 | 1352.0 |
| profile.html | 265.5 | 981.0 |
| contact.html | 279.0 | 995.5 |
| resumes.html | 200.5 | 972.0 |
| quality.html | 264.0 | 986.5 |
| cases/demandpilot.html | 256.0 | 992.5 |
| cases/transactionshield.html | 242.5 | 981.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
