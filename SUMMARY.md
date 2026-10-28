# Portfolio verification results

Generated UTC: 2026-10-28T07:14:34.550152+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 52.5 | 368.0 |
| work.html | 94.5 | 364.0 |
| proof-map.html | 70.5 | 397.0 |
| profile.html | 44.0 | 238.0 |
| contact.html | 62.0 | 373.0 |
| resumes.html | 42.5 | 202.5 |
| quality.html | 48.5 | 341.0 |
| cases/demandpilot.html | 49.0 | 389.0 |
| cases/transactionshield.html | 50.0 | 380.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
