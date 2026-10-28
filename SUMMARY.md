# Portfolio verification results

Generated UTC: 2026-10-28T08:26:54.900124+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 79.5 | 386.0 |
| work.html | 150.5 | 412.0 |
| evidence.html | 136.5 | 437.5 |
| engineering.html | 91.0 | 368.5 |
| proof-map.html | 89.5 | 417.0 |
| hiring.html | 80.5 | 362.5 |
| interview.html | 89.0 | 355.0 |
| profile.html | 82.0 | 400.5 |
| contact.html | 96.0 | 411.0 |
| resumes.html | 80.5 | 370.5 |
| quality.html | 81.0 | 365.0 |
| cases/demandpilot.html | 96.5 | 336.5 |
| cases/transactionshield.html | 79.5 | 384.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
