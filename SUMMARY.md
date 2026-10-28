# Portfolio verification results

Generated UTC: 2026-10-28T08:49:09.090903+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 143 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 150/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 231.0 | 982.0 |
| work.html | 191.0 | 1353.0 |
| evidence.html | 349.0 | 1379.5 |
| engineering.html | 88.5 | 955.0 |
| proof-map.html | 152.0 | 1322.5 |
| hiring.html | 80.0 | 954.0 |
| interview.html | 87.5 | 1320.0 |
| profile.html | 86.5 | 946.5 |
| contact.html | 153.0 | 958.0 |
| resumes.html | 79.0 | 943.5 |
| quality.html | 81.0 | 958.5 |
| cases/demandpilot.html | 81.5 | 957.0 |
| cases/transactionshield.html | 85.5 | 961.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
