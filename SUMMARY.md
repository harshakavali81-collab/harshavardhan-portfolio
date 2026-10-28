# Portfolio verification results

Generated UTC: 2026-10-28T08:49:21.209938+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 145 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 326.5 | 1040.5 |
| work.html | 347.0 | 1420.0 |
| evidence.html | 342.0 | 1461.5 |
| engineering.html | 190.5 | 1042.0 |
| proof-map.html | 310.0 | 1397.5 |
| hiring.html | 265.5 | 1033.0 |
| interview.html | 254.5 | 1387.0 |
| profile.html | 156.0 | 1017.5 |
| contact.html | 285.5 | 1039.5 |
| resumes.html | 224.5 | 1018.0 |
| quality.html | 218.0 | 1036.5 |
| cases/demandpilot.html | 259.0 | 767.0 |
| cases/transactionshield.html | 148.0 | 787.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
