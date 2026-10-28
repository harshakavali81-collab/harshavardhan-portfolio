# Portfolio verification results

Generated UTC: 2026-10-28T08:17:46.373351+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 136 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 179.5 | 279.5 |
| work.html | 358.5 | 381.0 |
| evidence.html | 277.0 | 364.5 |
| engineering.html | 125.5 | 354.0 |
| proof-map.html | 124.5 | 359.5 |
| hiring.html | 127.5 | 365.0 |
| interview.html | 156.5 | 327.5 |
| profile.html | 184.5 | 365.5 |
| contact.html | 167.5 | 375.5 |
| resumes.html | 140.0 | 315.5 |
| quality.html | 118.5 | 323.0 |
| cases/demandpilot.html | 127.0 | 353.5 |
| cases/transactionshield.html | 125.5 | 399.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
