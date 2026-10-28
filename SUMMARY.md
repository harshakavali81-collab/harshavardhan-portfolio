# Portfolio verification results

Generated UTC: 2026-10-28T07:32:40.391837+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 134.5 | 335.5 |
| work.html | 255.0 | 378.5 |
| proof-map.html | 89.0 | 393.0 |
| hiring.html | 81.0 | 384.0 |
| interview.html | 117.0 | 360.5 |
| profile.html | 68.5 | 222.0 |
| contact.html | 126.5 | 372.0 |
| resumes.html | 90.0 | 225.0 |
| quality.html | 105.5 | 363.5 |
| cases/demandpilot.html | 87.5 | 370.0 |
| cases/transactionshield.html | 96.0 | 383.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
