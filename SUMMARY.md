# Portfolio verification results

Generated UTC: 2026-10-28T08:28:27.397154+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 104 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 82.0 | 380.0 |
| work.html | 107.0 | 437.5 |
| evidence.html | 109.0 | 456.5 |
| engineering.html | 88.5 | 386.5 |
| proof-map.html | 102.5 | 423.5 |
| hiring.html | 90.5 | 422.5 |
| interview.html | 92.0 | 348.0 |
| profile.html | 89.0 | 429.0 |
| contact.html | 106.5 | 425.0 |
| resumes.html | 90.5 | 355.0 |
| quality.html | 89.5 | 384.0 |
| cases/demandpilot.html | 87.5 | 397.0 |
| cases/transactionshield.html | 89.5 | 407.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
