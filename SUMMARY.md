# Portfolio verification results

Generated UTC: 2026-10-28T07:16:44.379974+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 104.0 | 367.0 |
| work.html | 152.5 | 380.5 |
| proof-map.html | 117.5 | 397.0 |
| hiring.html | 116.0 | 391.0 |
| interview.html | 113.5 | 383.5 |
| profile.html | 93.0 | 253.0 |
| contact.html | 126.0 | 388.0 |
| resumes.html | 93.0 | 236.0 |
| quality.html | 112.0 | 353.5 |
| cases/demandpilot.html | 112.5 | 397.0 |
| cases/transactionshield.html | 116.0 | 399.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
