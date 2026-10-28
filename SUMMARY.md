# Portfolio verification results

Generated UTC: 2026-10-28T06:42:36.689480+00:00

## Direct checks
- Live URL HTTP 200: 14/14
- External links: 52 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 112/112 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 38.5 | 317.0 |
| work.html | 37.0 | 357.0 |
| profile.html | 27.5 | 220.5 |
| contact.html | 42.0 | 351.0 |
| resumes.html | 25.0 | 209.0 |
| quality.html | 45.0 | 352.0 |
| cases/demandpilot.html | 31.0 | 365.5 |
| cases/transactionshield.html | 34.5 | 370.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
