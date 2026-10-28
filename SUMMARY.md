# Portfolio verification results

Generated UTC: 2026-10-28T09:32:49.281563+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 157 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 542.0 | 1109.0 |
| work.html | 240.5 | 1431.0 |
| evidence.html | 634.5 | 1418.0 |
| engineering.html | 235.5 | 1029.5 |
| proof-map.html | 268.0 | 1448.0 |
| hiring.html | 264.5 | 740.5 |
| interview.html | 308.0 | 1393.0 |
| profile.html | 187.5 | 973.0 |
| contact.html | 334.0 | 973.0 |
| resumes.html | 183.0 | 1090.0 |
| quality.html | 260.5 | 1051.0 |
| cases/demandpilot.html | 326.5 | 1040.0 |
| cases/transactionshield.html | 984.0 | 1115.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
