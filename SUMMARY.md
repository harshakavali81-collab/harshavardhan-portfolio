# Portfolio verification results

Generated UTC: 2026-10-28T06:47:31.650942+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 53 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 125.0 | 274.5 |
| work.html | 162.5 | 348.5 |
| proof-map.html | 123.5 | 357.0 |
| profile.html | 72.5 | 219.5 |
| contact.html | 116.5 | 372.5 |
| resumes.html | 92.5 | 216.0 |
| quality.html | 89.5 | 324.0 |
| cases/demandpilot.html | 109.0 | 308.0 |
| cases/transactionshield.html | 101.0 | 353.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
