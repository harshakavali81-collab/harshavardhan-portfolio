# Portfolio verification results

Generated UTC: 2026-10-28T07:37:01.153045+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 38.0 | 327.5 |
| work.html | 41.0 | 355.5 |
| proof-map.html | 65.0 | 363.5 |
| hiring.html | 30.5 | 354.0 |
| interview.html | 34.5 | 348.0 |
| profile.html | 23.0 | 205.5 |
| contact.html | 41.0 | 350.5 |
| resumes.html | 22.5 | 168.0 |
| quality.html | 29.0 | 322.5 |
| cases/demandpilot.html | 28.0 | 295.5 |
| cases/transactionshield.html | 26.5 | 365.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
