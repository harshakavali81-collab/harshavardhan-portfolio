# Portfolio verification results

Generated UTC: 2026-10-28T08:27:25.819861+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 39.0 | 365.5 |
| work.html | 40.5 | 416.5 |
| evidence.html | 46.0 | 421.0 |
| engineering.html | 27.0 | 356.0 |
| proof-map.html | 45.0 | 405.0 |
| hiring.html | 28.0 | 390.5 |
| interview.html | 25.5 | 379.5 |
| profile.html | 28.5 | 399.0 |
| contact.html | 44.0 | 386.0 |
| resumes.html | 27.5 | 349.0 |
| quality.html | 24.5 | 351.0 |
| cases/demandpilot.html | 25.5 | 297.0 |
| cases/transactionshield.html | 27.5 | 370.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
