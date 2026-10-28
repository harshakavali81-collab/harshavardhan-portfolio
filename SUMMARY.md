# Portfolio verification results

Generated UTC: 2026-10-28T07:48:24.989981+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 84 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 127.0 | 331.0 |
| work.html | 173.0 | 357.5 |
| evidence.html | 116.5 | 368.5 |
| engineering.html | 105.0 | 292.0 |
| proof-map.html | 119.5 | 366.0 |
| hiring.html | 64.5 | 297.0 |
| interview.html | 103.5 | 320.0 |
| profile.html | 96.5 | 218.5 |
| contact.html | 111.0 | 357.0 |
| resumes.html | 100.5 | 204.0 |
| quality.html | 101.0 | 351.5 |
| cases/demandpilot.html | 95.5 | 293.0 |
| cases/transactionshield.html | 106.0 | 363.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
