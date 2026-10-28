# Portfolio verification results

Generated UTC: 2026-10-28T08:38:26.876206+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 33 reachable; 0 broken; 110 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 133/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 518.5 | 985.5 |
| work.html | 289.0 | 1342.5 |
| evidence.html | 268.5 | 1374.5 |
| engineering.html | 152.5 | 961.5 |
| proof-map.html | 186.0 | 1328.0 |
| hiring.html | 214.0 | 970.0 |
| interview.html | 173.0 | 1320.0 |
| profile.html | 171.5 | 942.0 |
| contact.html | 223.0 | 969.0 |
| resumes.html | 206.5 | 935.5 |
| quality.html | 120.5 | 955.0 |
| cases/demandpilot.html | 174.5 | 961.5 |
| cases/transactionshield.html | 183.5 | 968.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
