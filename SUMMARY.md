# Portfolio verification results

Generated UTC: 2026-10-28T08:12:30.163014+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 39.5 | 314.5 |
| work.html | 50.5 | 357.0 |
| evidence.html | 50.0 | 367.0 |
| engineering.html | 35.5 | 319.0 |
| proof-map.html | 49.0 | 359.0 |
| hiring.html | 49.0 | 358.5 |
| interview.html | 28.5 | 329.0 |
| profile.html | 26.5 | 214.5 |
| contact.html | 43.0 | 346.5 |
| resumes.html | 29.5 | 197.5 |
| quality.html | 36.5 | 342.0 |
| cases/demandpilot.html | 31.0 | 354.0 |
| cases/transactionshield.html | 30.0 | 353.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
