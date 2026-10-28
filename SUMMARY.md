# Portfolio verification results

Generated UTC: 2026-10-28T09:16:07.529807+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 152 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 240.0 | 964.5 |
| work.html | 196.5 | 1324.0 |
| evidence.html | 161.0 | 1357.5 |
| engineering.html | 63.0 | 939.0 |
| proof-map.html | 123.0 | 1297.0 |
| hiring.html | 76.0 | 936.0 |
| interview.html | 59.0 | 1376.5 |
| profile.html | 92.5 | 935.5 |
| contact.html | 113.0 | 936.5 |
| resumes.html | 73.5 | 916.5 |
| quality.html | 62.5 | 939.0 |
| cases/demandpilot.html | 68.5 | 935.5 |
| cases/transactionshield.html | 72.0 | 933.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
