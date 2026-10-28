# Portfolio verification results

Generated UTC: 2026-10-28T08:10:04.566986+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 112 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 104.0 | 319.0 |
| work.html | 148.5 | 369.5 |
| evidence.html | 134.5 | 385.5 |
| engineering.html | 88.5 | 354.5 |
| proof-map.html | 98.5 | 372.0 |
| hiring.html | 86.5 | 359.5 |
| interview.html | 97.0 | 355.5 |
| profile.html | 70.5 | 211.0 |
| contact.html | 104.5 | 363.5 |
| resumes.html | 71.5 | 212.5 |
| quality.html | 94.0 | 355.5 |
| cases/demandpilot.html | 98.5 | 344.5 |
| cases/transactionshield.html | 91.5 | 367.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
