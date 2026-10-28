# Portfolio verification results

Generated UTC: 2026-10-28T09:36:34.372251+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 271.0 | 982.5 |
| work.html | 262.5 | 1376.0 |
| evidence.html | 210.5 | 1402.0 |
| engineering.html | 132.5 | 980.5 |
| proof-map.html | 197.0 | 1335.0 |
| hiring.html | 138.0 | 964.0 |
| interview.html | 132.5 | 1382.5 |
| profile.html | 133.0 | 721.0 |
| contact.html | 193.0 | 980.5 |
| resumes.html | 128.5 | 960.5 |
| quality.html | 127.0 | 969.5 |
| cases/demandpilot.html | 129.0 | 972.5 |
| cases/transactionshield.html | 133.0 | 976.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
