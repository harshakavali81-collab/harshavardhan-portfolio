# Portfolio verification results

Generated UTC: 2026-10-28T08:11:52.806282+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 36.5 | 346.5 |
| work.html | 47.0 | 368.5 |
| evidence.html | 43.5 | 382.5 |
| engineering.html | 26.5 | 322.5 |
| proof-map.html | 45.0 | 363.5 |
| hiring.html | 28.5 | 355.5 |
| interview.html | 31.0 | 321.0 |
| profile.html | 23.5 | 206.0 |
| contact.html | 40.0 | 355.5 |
| resumes.html | 21.0 | 183.0 |
| quality.html | 29.5 | 293.0 |
| cases/demandpilot.html | 31.0 | 292.5 |
| cases/transactionshield.html | 27.0 | 366.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
