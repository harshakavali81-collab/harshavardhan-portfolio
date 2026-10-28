# Portfolio verification results

Generated UTC: 2026-10-28T08:23:21.654095+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 55.5 | 346.5 |
| work.html | 83.5 | 410.0 |
| evidence.html | 80.5 | 423.0 |
| engineering.html | 46.5 | 321.5 |
| proof-map.html | 63.5 | 411.5 |
| hiring.html | 53.0 | 395.0 |
| interview.html | 47.5 | 322.5 |
| profile.html | 48.5 | 353.0 |
| contact.html | 63.5 | 390.0 |
| resumes.html | 46.5 | 331.0 |
| quality.html | 45.0 | 327.0 |
| cases/demandpilot.html | 48.0 | 373.0 |
| cases/transactionshield.html | 47.0 | 301.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
