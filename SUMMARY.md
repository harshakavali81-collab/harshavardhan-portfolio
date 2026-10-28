# Portfolio verification results

Generated UTC: 2026-10-28T08:19:15.656268+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 136 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 31.5 | 317.5 |
| work.html | 56.0 | 387.0 |
| evidence.html | 43.5 | 405.0 |
| engineering.html | 30.5 | 350.5 |
| proof-map.html | 40.0 | 386.0 |
| hiring.html | 28.0 | 378.0 |
| interview.html | 26.0 | 343.0 |
| profile.html | 27.5 | 347.0 |
| contact.html | 44.0 | 377.5 |
| resumes.html | 25.5 | 321.5 |
| quality.html | 26.0 | 318.0 |
| cases/demandpilot.html | 26.0 | 324.0 |
| cases/transactionshield.html | 27.5 | 294.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
