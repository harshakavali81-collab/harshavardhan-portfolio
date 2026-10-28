# Portfolio verification results

Generated UTC: 2026-10-28T08:59:56.833697+00:00

## Direct checks
- Live URL HTTP 200: 18/19
- External links: 146 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 337.0 | 1003.0 |
| work.html | 433.0 | 1391.5 |
| evidence.html | 382.5 | 1432.5 |
| engineering.html | 240.5 | 999.0 |
| proof-map.html | 310.0 | 1356.0 |
| hiring.html | 206.0 | 1066.5 |
| interview.html | 262.0 | 1356.0 |
| profile.html | 240.0 | 984.5 |
| contact.html | 277.0 | 997.0 |
| resumes.html | 188.0 | 976.5 |
| quality.html | 189.0 | 998.5 |
| cases/demandpilot.html | 204.0 | 999.5 |
| cases/transactionshield.html | 216.0 | 1305.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
