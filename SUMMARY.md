# Portfolio verification results

Generated UTC: 2026-10-28T09:04:25.502594+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 152 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 382.0 | 1062.5 |
| work.html | 472.0 | 1431.0 |
| evidence.html | 350.5 | 1480.5 |
| engineering.html | 201.5 | 1041.0 |
| proof-map.html | 403.0 | 1395.0 |
| hiring.html | 243.5 | 1038.0 |
| interview.html | 204.5 | 1386.5 |
| profile.html | 199.5 | 1026.0 |
| contact.html | 389.0 | 1044.0 |
| resumes.html | 265.0 | 993.5 |
| quality.html | 170.0 | 534.0 |
| cases/demandpilot.html | 208.0 | 1043.0 |
| cases/transactionshield.html | 184.5 | 533.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
