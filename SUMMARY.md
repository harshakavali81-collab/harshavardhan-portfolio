# Portfolio verification results

Generated UTC: 2026-10-28T07:45:44.125143+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 67 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 156.0 | 327.0 |
| work.html | 238.5 | 625.5 |
| evidence.html | 240.5 | 386.0 |
| engineering.html | 192.5 | 397.5 |
| proof-map.html | 158.5 | 379.5 |
| hiring.html | 144.5 | 420.5 |
| interview.html | 107.0 | 351.0 |
| profile.html | 154.0 | 270.5 |
| contact.html | 94.0 | 365.0 |
| resumes.html | 129.0 | 209.5 |
| quality.html | 175.5 | 415.5 |
| cases/demandpilot.html | 105.0 | 377.5 |
| cases/transactionshield.html | 184.5 | 439.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
