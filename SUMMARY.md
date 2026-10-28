# Portfolio verification results

Generated UTC: 2026-10-28T07:14:14.060901+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 43.0 | 324.0 |
| work.html | 50.5 | 348.5 |
| proof-map.html | 47.5 | 362.0 |
| profile.html | 28.0 | 215.0 |
| contact.html | 44.0 | 353.5 |
| resumes.html | 31.0 | 200.5 |
| quality.html | 34.0 | 320.0 |
| cases/demandpilot.html | 35.0 | 326.0 |
| cases/transactionshield.html | 38.5 | 326.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
