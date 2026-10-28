# Portfolio verification results

Generated UTC: 2026-10-28T09:01:16.194396+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 150 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 466.5 | 1049.5 |
| work.html | 359.0 | 1437.0 |
| evidence.html | 410.0 | 1469.5 |
| engineering.html | 187.5 | 1040.0 |
| proof-map.html | 385.5 | 1413.0 |
| hiring.html | 191.0 | 1037.5 |
| interview.html | 219.5 | 958.0 |
| profile.html | 205.0 | 1030.0 |
| contact.html | 303.0 | 1051.5 |
| resumes.html | 203.0 | 1020.5 |
| quality.html | 318.0 | 1041.0 |
| cases/demandpilot.html | 265.5 | 1045.0 |
| cases/transactionshield.html | 250.0 | 1040.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
