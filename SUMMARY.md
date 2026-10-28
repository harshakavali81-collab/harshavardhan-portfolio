# Portfolio verification results

Generated UTC: 2026-10-28T08:26:30.903763+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 81.5 | 377.0 |
| work.html | 93.5 | 439.0 |
| evidence.html | 111.0 | 451.0 |
| engineering.html | 91.0 | 433.5 |
| proof-map.html | 101.0 | 428.5 |
| hiring.html | 89.5 | 423.0 |
| interview.html | 88.5 | 416.5 |
| profile.html | 89.5 | 331.0 |
| contact.html | 105.0 | 419.5 |
| resumes.html | 90.0 | 389.5 |
| quality.html | 89.0 | 361.5 |
| cases/demandpilot.html | 90.0 | 362.0 |
| cases/transactionshield.html | 88.5 | 402.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
