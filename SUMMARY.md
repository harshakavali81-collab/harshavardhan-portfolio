# Portfolio verification results

Generated UTC: 2026-10-28T06:43:08.780437+00:00

## Direct checks
- Live URL HTTP 200: 14/14
- External links: 53 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 112/112 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 35.0 | 341.5 |
| work.html | 49.0 | 352.0 |
| profile.html | 27.5 | 207.0 |
| contact.html | 44.0 | 359.5 |
| resumes.html | 22.5 | 210.0 |
| quality.html | 28.0 | 358.0 |
| cases/demandpilot.html | 32.5 | 338.5 |
| cases/transactionshield.html | 35.5 | 375.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
