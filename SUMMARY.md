# Portfolio verification results

Generated UTC: 2026-10-28T08:15:49.432545+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 122 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 78.5 | 317.0 |
| work.html | 74.0 | 357.0 |
| evidence.html | 67.0 | 371.5 |
| engineering.html | 58.0 | 347.0 |
| proof-map.html | 72.0 | 351.5 |
| hiring.html | 63.0 | 348.0 |
| interview.html | 58.5 | 310.5 |
| profile.html | 68.5 | 379.5 |
| contact.html | 62.0 | 350.0 |
| resumes.html | 44.5 | 208.5 |
| quality.html | 94.0 | 326.5 |
| cases/demandpilot.html | 68.5 | 333.0 |
| cases/transactionshield.html | 72.0 | 357.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
