# Portfolio verification results

Generated UTC: 2026-10-28T07:45:04.729983+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 65 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 42.5 | 331.5 |
| work.html | 45.5 | 354.5 |
| evidence.html | 51.5 | 376.5 |
| engineering.html | 31.0 | 360.0 |
| proof-map.html | 42.0 | 370.5 |
| hiring.html | 36.5 | 325.0 |
| interview.html | 30.5 | 354.5 |
| profile.html | 35.0 | 222.0 |
| contact.html | 46.5 | 355.0 |
| resumes.html | 29.0 | 186.5 |
| quality.html | 38.0 | 325.0 |
| cases/demandpilot.html | 36.5 | 328.5 |
| cases/transactionshield.html | 32.5 | 371.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
