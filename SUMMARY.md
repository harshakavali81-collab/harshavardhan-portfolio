# Portfolio verification results

Generated UTC: 2026-10-28T07:50:32.671656+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 101 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 78.5 | 345.0 |
| work.html | 52.0 | 373.0 |
| evidence.html | 65.5 | 381.5 |
| engineering.html | 60.5 | 337.0 |
| proof-map.html | 60.5 | 377.5 |
| hiring.html | 46.5 | 373.5 |
| interview.html | 49.0 | 329.5 |
| profile.html | 38.0 | 232.0 |
| contact.html | 69.0 | 362.5 |
| resumes.html | 37.0 | 212.0 |
| quality.html | 48.0 | 332.5 |
| cases/demandpilot.html | 49.5 | 340.0 |
| cases/transactionshield.html | 49.0 | 335.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
