# Portfolio verification results

Generated UTC: 2026-10-28T11:02:46.803373+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 72/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 221.0 | 1879.0 |
| work.html | 97.0 | 844.5 |
| job-platforms.html | 123.5 | 1381.5 |
| evidence.html | 116.5 | 870.5 |
| engineering.html | 62.0 | 789.0 |
| proof-map.html | 107.5 | 910.0 |
| hiring.html | 72.5 | 788.5 |
| interview.html | 69.0 | 784.5 |
| profile.html | 155.5 | 823.0 |
| contact.html | 112.5 | 796.5 |
| resumes.html | 60.5 | 762.5 |
| quality.html | 73.5 | 795.5 |
| cases/demandpilot.html | 83.5 | 1335.5 |
| cases/transactionshield.html | 63.0 | 1384.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
