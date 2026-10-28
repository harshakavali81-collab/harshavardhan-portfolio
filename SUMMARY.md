# Portfolio verification results

Generated UTC: 2026-10-28T07:44:11.513477+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 63 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 34.5 | 335.5 |
| work.html | 42.5 | 355.5 |
| evidence.html | 51.0 | 377.5 |
| engineering.html | 33.5 | 355.5 |
| proof-map.html | 46.5 | 376.5 |
| hiring.html | 28.5 | 325.0 |
| interview.html | 39.5 | 347.5 |
| profile.html | 32.5 | 201.5 |
| contact.html | 51.0 | 359.5 |
| resumes.html | 29.5 | 190.0 |
| quality.html | 33.5 | 322.5 |
| cases/demandpilot.html | 37.0 | 370.0 |
| cases/transactionshield.html | 31.5 | 329.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
