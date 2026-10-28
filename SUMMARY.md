# Portfolio verification results

Generated UTC: 2026-10-28T08:17:12.207743+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 122 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 46.5 | 357.5 |
| work.html | 51.0 | 402.5 |
| evidence.html | 62.5 | 385.0 |
| engineering.html | 42.5 | 331.5 |
| proof-map.html | 44.0 | 381.5 |
| hiring.html | 37.5 | 336.0 |
| interview.html | 34.5 | 359.5 |
| profile.html | 30.0 | 401.5 |
| contact.html | 46.5 | 400.0 |
| resumes.html | 28.0 | 359.5 |
| quality.html | 28.0 | 331.0 |
| cases/demandpilot.html | 27.0 | 375.5 |
| cases/transactionshield.html | 27.5 | 376.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
