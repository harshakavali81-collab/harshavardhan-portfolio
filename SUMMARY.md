# Portfolio verification results

Generated UTC: 2026-10-28T09:05:35.529988+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 152 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 389.0 | 1054.0 |
| work.html | 340.5 | 1445.5 |
| evidence.html | 327.0 | 1474.5 |
| engineering.html | 250.0 | 1034.0 |
| proof-map.html | 395.0 | 1403.0 |
| hiring.html | 292.0 | 1028.5 |
| interview.html | 276.0 | 1406.0 |
| profile.html | 342.0 | 1033.5 |
| contact.html | 286.5 | 1048.0 |
| resumes.html | 259.0 | 999.5 |
| quality.html | 189.5 | 1047.5 |
| cases/demandpilot.html | 284.0 | 1043.5 |
| cases/transactionshield.html | 310.5 | 1047.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
