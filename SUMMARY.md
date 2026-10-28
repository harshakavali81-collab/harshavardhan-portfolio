# Portfolio verification results

Generated UTC: 2026-10-28T07:47:07.866957+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 84 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 140.0 | 369.5 |
| work.html | 82.5 | 394.5 |
| evidence.html | 163.5 | 415.0 |
| engineering.html | 124.0 | 319.0 |
| proof-map.html | 124.5 | 399.5 |
| hiring.html | 106.0 | 379.5 |
| interview.html | 143.5 | 390.0 |
| profile.html | 106.5 | 204.0 |
| contact.html | 143.5 | 388.5 |
| resumes.html | 97.5 | 235.5 |
| quality.html | 101.5 | 384.0 |
| cases/demandpilot.html | 97.0 | 363.5 |
| cases/transactionshield.html | 199.5 | 357.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
