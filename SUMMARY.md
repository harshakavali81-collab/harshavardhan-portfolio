# Portfolio verification results

Generated UTC: 2026-10-28T08:10:19.051237+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 112 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 37.5 | 366.5 |
| work.html | 51.0 | 384.5 |
| evidence.html | 65.5 | 391.5 |
| engineering.html | 31.5 | 335.0 |
| proof-map.html | 46.0 | 395.0 |
| hiring.html | 34.0 | 374.0 |
| interview.html | 28.5 | 367.5 |
| profile.html | 23.5 | 237.5 |
| contact.html | 76.0 | 365.5 |
| resumes.html | 35.5 | 216.5 |
| quality.html | 46.0 | 333.0 |
| cases/demandpilot.html | 55.0 | 381.5 |
| cases/transactionshield.html | 34.5 | 345.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
