# Portfolio verification results

Generated UTC: 2026-10-28T10:00:43.475143+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 160 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 168/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 229.0 | 954.5 |
| work.html | 186.5 | 1330.5 |
| job-platforms.html | 111.5 | 740.0 |
| evidence.html | 153.0 | 1398.0 |
| engineering.html | 522.0 | 1787.0 |
| proof-map.html | 114.0 | 1440.5 |
| hiring.html | 64.0 | 936.0 |
| interview.html | 420.0 | 1344.0 |
| profile.html | 481.0 | 925.0 |
| contact.html | 132.0 | 936.5 |
| resumes.html | 72.0 | 1321.5 |
| quality.html | 72.5 | 939.5 |
| cases/demandpilot.html | 73.0 | 936.0 |
| cases/transactionshield.html | 59.5 | 947.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
