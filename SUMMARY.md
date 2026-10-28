# Portfolio verification results

Generated UTC: 2026-10-28T08:13:36.391996+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 83.0 | 365.5 |
| work.html | 130.5 | 391.0 |
| evidence.html | 124.5 | 387.5 |
| engineering.html | 108.0 | 343.5 |
| proof-map.html | 87.5 | 386.5 |
| hiring.html | 84.5 | 376.0 |
| interview.html | 101.5 | 340.5 |
| profile.html | 73.0 | 239.5 |
| contact.html | 108.0 | 379.5 |
| resumes.html | 76.5 | 227.5 |
| quality.html | 98.0 | 374.5 |
| cases/demandpilot.html | 96.5 | 389.0 |
| cases/transactionshield.html | 94.5 | 351.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
