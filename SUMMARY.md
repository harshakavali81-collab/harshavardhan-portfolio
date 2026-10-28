# Portfolio verification results

Generated UTC: 2026-10-28T08:54:38.458602+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 146 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 377.5 | 1072.5 |
| work.html | 350.5 | 1436.5 |
| evidence.html | 356.0 | 1464.0 |
| engineering.html | 272.5 | 1051.5 |
| proof-map.html | 344.0 | 1403.0 |
| hiring.html | 273.0 | 1037.5 |
| interview.html | 342.5 | 1406.0 |
| profile.html | 331.5 | 1021.5 |
| contact.html | 322.5 | 1044.0 |
| resumes.html | 304.0 | 1016.5 |
| quality.html | 200.0 | 790.0 |
| cases/demandpilot.html | 306.5 | 1048.5 |
| cases/transactionshield.html | 254.0 | 1029.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
