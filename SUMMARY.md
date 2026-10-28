# Portfolio verification results

Generated UTC: 2026-10-28T08:48:35.859302+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 143 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 232.0 | 973.5 |
| work.html | 165.5 | 1343.0 |
| evidence.html | 173.5 | 1376.0 |
| engineering.html | 81.5 | 954.5 |
| proof-map.html | 155.0 | 1320.0 |
| hiring.html | 80.5 | 959.0 |
| interview.html | 81.5 | 1319.5 |
| profile.html | 82.5 | 951.0 |
| contact.html | 140.0 | 953.5 |
| resumes.html | 80.0 | 937.5 |
| quality.html | 81.5 | 954.0 |
| cases/demandpilot.html | 81.5 | 958.0 |
| cases/transactionshield.html | 81.0 | 956.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
