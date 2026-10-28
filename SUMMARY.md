# Portfolio verification results

Generated UTC: 2026-10-28T09:37:55.476903+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 168/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 240.5 | 968.5 |
| work.html | 200.0 | 1346.5 |
| job-platforms.html | 146.5 | 752.0 |
| evidence.html | 181.5 | 1373.0 |
| engineering.html | 89.5 | 957.5 |
| proof-map.html | 152.0 | 1314.0 |
| hiring.html | 90.5 | 954.5 |
| interview.html | 87.0 | 1316.0 |
| profile.html | 82.0 | 947.0 |
| contact.html | 142.5 | 954.0 |
| resumes.html | 134.0 | 932.0 |
| quality.html | 83.5 | 713.5 |
| cases/demandpilot.html | 88.5 | 957.5 |
| cases/transactionshield.html | 82.0 | 954.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
