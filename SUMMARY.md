# Portfolio verification results

Generated UTC: 2026-10-28T08:10:46.605941+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 116 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 80.0 | 322.0 |
| work.html | 108.5 | 383.0 |
| evidence.html | 110.5 | 391.0 |
| engineering.html | 87.5 | 387.5 |
| proof-map.html | 77.5 | 370.5 |
| hiring.html | 139.0 | 351.0 |
| interview.html | 94.0 | 356.5 |
| profile.html | 93.5 | 217.0 |
| contact.html | 82.0 | 398.5 |
| resumes.html | 129.0 | 218.0 |
| quality.html | 101.0 | 365.5 |
| cases/demandpilot.html | 106.5 | 371.0 |
| cases/transactionshield.html | 136.0 | 393.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
