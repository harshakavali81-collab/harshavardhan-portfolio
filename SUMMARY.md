# Portfolio verification results

Generated UTC: 2026-10-28T08:14:07.228135+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 147.0 | 384.0 |
| work.html | 267.0 | 399.0 |
| evidence.html | 145.0 | 476.0 |
| engineering.html | 101.5 | 373.5 |
| proof-map.html | 143.5 | 404.0 |
| hiring.html | 88.0 | 318.5 |
| interview.html | 124.5 | 343.0 |
| profile.html | 189.5 | 246.5 |
| contact.html | 140.5 | 381.0 |
| resumes.html | 124.0 | 236.0 |
| quality.html | 122.5 | 386.5 |
| cases/demandpilot.html | 85.5 | 396.0 |
| cases/transactionshield.html | 115.0 | 353.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
