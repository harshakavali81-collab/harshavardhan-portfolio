# Portfolio verification results

Generated UTC: 2026-10-28T06:44:18.932159+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 53 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 55.5 | 393.0 |
| work.html | 77.0 | 374.5 |
| proof-map.html | 52.5 | 405.0 |
| profile.html | 34.0 | 230.5 |
| contact.html | 48.5 | 381.0 |
| resumes.html | 28.0 | 226.5 |
| quality.html | 38.0 | 339.5 |
| cases/demandpilot.html | 40.5 | 403.0 |
| cases/transactionshield.html | 38.5 | 311.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
