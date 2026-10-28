# Portfolio verification results

Generated UTC: 2026-10-28T07:47:47.654688+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 100 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 63.0 | 348.0 |
| work.html | 50.5 | 361.0 |
| evidence.html | 58.0 | 372.5 |
| engineering.html | 31.0 | 357.5 |
| proof-map.html | 39.0 | 373.5 |
| hiring.html | 40.0 | 330.5 |
| interview.html | 31.0 | 351.5 |
| profile.html | 33.5 | 223.5 |
| contact.html | 46.5 | 361.0 |
| resumes.html | 26.0 | 213.0 |
| quality.html | 34.0 | 358.5 |
| cases/demandpilot.html | 36.0 | 370.5 |
| cases/transactionshield.html | 29.5 | 330.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
