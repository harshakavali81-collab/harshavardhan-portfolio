# Portfolio verification results

Generated UTC: 2026-10-28T08:24:38.682152+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 41.0 | 350.0 |
| work.html | 112.0 | 414.5 |
| evidence.html | 164.5 | 416.5 |
| engineering.html | 79.5 | 351.5 |
| proof-map.html | 78.0 | 402.5 |
| hiring.html | 29.0 | 351.5 |
| interview.html | 61.0 | 345.0 |
| profile.html | 64.0 | 400.0 |
| contact.html | 77.5 | 389.5 |
| resumes.html | 26.0 | 353.5 |
| quality.html | 62.0 | 323.5 |
| cases/demandpilot.html | 27.5 | 365.0 |
| cases/transactionshield.html | 26.5 | 331.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
