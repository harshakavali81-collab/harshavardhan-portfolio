# Portfolio verification results

Generated UTC: 2026-10-28T08:29:32.396258+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 104 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 38.5 | 357.5 |
| work.html | 41.0 | 411.5 |
| evidence.html | 53.0 | 417.0 |
| engineering.html | 28.0 | 389.5 |
| proof-map.html | 46.5 | 401.0 |
| hiring.html | 35.5 | 396.5 |
| interview.html | 29.0 | 387.5 |
| profile.html | 27.0 | 392.0 |
| contact.html | 44.0 | 391.5 |
| resumes.html | 27.5 | 301.0 |
| quality.html | 25.5 | 323.5 |
| cases/demandpilot.html | 27.0 | 364.5 |
| cases/transactionshield.html | 27.5 | 371.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
