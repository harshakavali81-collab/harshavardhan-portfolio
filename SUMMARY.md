# Portfolio verification results

Generated UTC: 2026-10-28T07:49:30.690327+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 99 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 137.5 | 357.0 |
| work.html | 180.0 | 381.0 |
| evidence.html | 162.0 | 390.0 |
| engineering.html | 84.0 | 358.0 |
| proof-map.html | 110.0 | 390.5 |
| hiring.html | 108.0 | 381.0 |
| interview.html | 75.0 | 371.5 |
| profile.html | 104.5 | 237.0 |
| contact.html | 181.0 | 373.5 |
| resumes.html | 86.0 | 189.0 |
| quality.html | 102.5 | 343.0 |
| cases/demandpilot.html | 102.5 | 393.5 |
| cases/transactionshield.html | 81.5 | 334.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
