# Portfolio verification results

Generated UTC: 2026-10-28T08:45:09.135245+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 143 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 221.0 | 951.5 |
| work.html | 192.5 | 1334.0 |
| evidence.html | 150.0 | 1410.0 |
| engineering.html | 65.0 | 933.0 |
| proof-map.html | 115.5 | 1355.0 |
| hiring.html | 59.0 | 932.5 |
| interview.html | 65.0 | 1298.0 |
| profile.html | 61.5 | 924.5 |
| contact.html | 113.0 | 948.0 |
| resumes.html | 67.5 | 916.5 |
| quality.html | 57.5 | 942.5 |
| cases/demandpilot.html | 67.5 | 932.0 |
| cases/transactionshield.html | 61.0 | 938.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
