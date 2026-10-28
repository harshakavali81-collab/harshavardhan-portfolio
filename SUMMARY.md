# Portfolio verification results

Generated UTC: 2026-10-28T08:35:32.392564+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 107 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 143/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 309.5 | 1003.5 |
| work.html | 303.5 | 1343.0 |
| evidence.html | 233.5 | 1380.5 |
| engineering.html | 137.0 | 966.5 |
| proof-map.html | 211.0 | 1317.0 |
| hiring.html | 150.5 | 954.5 |
| interview.html | 109.0 | 1319.5 |
| profile.html | 189.5 | 950.0 |
| contact.html | 203.5 | 970.5 |
| resumes.html | 151.5 | 939.5 |
| quality.html | 140.5 | 961.5 |
| cases/demandpilot.html | 147.0 | 961.5 |
| cases/transactionshield.html | 150.5 | 965.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
