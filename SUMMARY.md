# Portfolio verification results

Generated UTC: 2026-10-28T08:33:36.672641+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 107 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 142/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 360.5 | 1063.0 |
| work.html | 352.0 | 1433.5 |
| evidence.html | 377.0 | 1469.5 |
| engineering.html | 204.5 | 1045.5 |
| proof-map.html | 344.5 | 1420.5 |
| hiring.html | 290.5 | 1044.0 |
| interview.html | 209.5 | 1410.0 |
| profile.html | 297.0 | 1062.5 |
| contact.html | 326.0 | 1053.0 |
| resumes.html | 314.0 | 1032.5 |
| quality.html | 196.5 | 1043.5 |
| cases/demandpilot.html | 256.5 | 1040.5 |
| cases/transactionshield.html | 326.5 | 1046.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
