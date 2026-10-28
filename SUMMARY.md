# Portfolio verification results

Generated UTC: 2026-10-28T08:16:02.406996+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 122 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 61.0 | 283.5 |
| work.html | 65.0 | 357.0 |
| evidence.html | 75.0 | 356.5 |
| engineering.html | 76.5 | 329.5 |
| proof-map.html | 74.5 | 348.5 |
| hiring.html | 72.0 | 312.0 |
| interview.html | 68.0 | 346.5 |
| profile.html | 63.5 | 341.5 |
| contact.html | 67.5 | 344.0 |
| resumes.html | 53.0 | 198.5 |
| quality.html | 64.0 | 304.5 |
| cases/demandpilot.html | 68.0 | 329.0 |
| cases/transactionshield.html | 66.5 | 333.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
