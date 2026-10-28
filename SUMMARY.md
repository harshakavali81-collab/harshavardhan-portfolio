# Portfolio verification results

Generated UTC: 2026-10-28T08:48:21.266343+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 143 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 205.5 | 952.5 |
| work.html | 253.0 | 1316.0 |
| evidence.html | 146.0 | 1385.0 |
| engineering.html | 132.0 | 936.0 |
| proof-map.html | 114.5 | 1297.0 |
| hiring.html | 55.0 | 932.0 |
| interview.html | 59.5 | 1297.5 |
| profile.html | 54.5 | 934.0 |
| contact.html | 102.5 | 936.0 |
| resumes.html | 159.0 | 914.0 |
| quality.html | 49.5 | 933.5 |
| cases/demandpilot.html | 57.0 | 933.0 |
| cases/transactionshield.html | 52.0 | 936.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
