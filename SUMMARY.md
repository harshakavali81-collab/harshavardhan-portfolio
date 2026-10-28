# Portfolio verification results

Generated UTC: 2026-10-28T08:11:05.976229+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 116 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 57.0 | 341.0 |
| work.html | 66.5 | 379.0 |
| evidence.html | 59.0 | 376.0 |
| engineering.html | 44.5 | 331.0 |
| proof-map.html | 51.5 | 377.5 |
| hiring.html | 44.0 | 365.0 |
| interview.html | 44.0 | 330.5 |
| profile.html | 34.0 | 204.5 |
| contact.html | 57.0 | 367.0 |
| resumes.html | 36.5 | 214.0 |
| quality.html | 45.5 | 364.0 |
| cases/demandpilot.html | 47.0 | 336.5 |
| cases/transactionshield.html | 47.5 | 378.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
