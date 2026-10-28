# Portfolio verification results

Generated UTC: 2026-10-28T06:49:58.579713+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 54 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 75.5 | 320.0 |
| work.html | 89.0 | 351.0 |
| proof-map.html | 57.5 | 364.5 |
| profile.html | 43.5 | 221.0 |
| contact.html | 61.0 | 352.5 |
| resumes.html | 41.5 | 207.5 |
| quality.html | 41.5 | 323.0 |
| cases/demandpilot.html | 41.5 | 363.0 |
| cases/transactionshield.html | 51.5 | 363.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
