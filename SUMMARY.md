# Portfolio verification results

Generated UTC: 2026-10-28T08:38:46.744566+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 33 reachable; 0 broken; 110 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 301.5 | 978.5 |
| work.html | 240.0 | 1349.0 |
| evidence.html | 219.0 | 1383.5 |
| engineering.html | 123.0 | 957.5 |
| proof-map.html | 196.5 | 1327.0 |
| hiring.html | 118.0 | 958.0 |
| interview.html | 120.0 | 1321.5 |
| profile.html | 121.5 | 947.5 |
| contact.html | 187.5 | 960.5 |
| resumes.html | 122.0 | 935.0 |
| quality.html | 122.5 | 958.0 |
| cases/demandpilot.html | 119.0 | 957.0 |
| cases/transactionshield.html | 127.5 | 960.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
