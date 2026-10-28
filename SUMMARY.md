# Portfolio verification results

Generated UTC: 2026-10-28T08:14:59.165361+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 60.0 | 292.5 |
| work.html | 115.0 | 365.0 |
| evidence.html | 104.5 | 379.0 |
| engineering.html | 65.5 | 330.0 |
| proof-map.html | 95.0 | 366.5 |
| hiring.html | 70.5 | 326.0 |
| interview.html | 71.5 | 330.5 |
| profile.html | 49.5 | 205.0 |
| contact.html | 114.0 | 354.0 |
| resumes.html | 51.5 | 217.5 |
| quality.html | 71.0 | 350.5 |
| cases/demandpilot.html | 71.0 | 333.0 |
| cases/transactionshield.html | 73.5 | 368.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
