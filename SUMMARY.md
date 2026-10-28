# Portfolio verification results

Generated UTC: 2026-10-28T07:37:55.816288+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 63 reachable; 0 broken; 0 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 172.0 | 347.0 |
| work.html | 164.5 | 377.0 |
| proof-map.html | 181.0 | 384.5 |
| hiring.html | 169.5 | 344.0 |
| interview.html | 140.0 | 369.0 |
| profile.html | 74.5 | 245.0 |
| contact.html | 121.5 | 369.5 |
| resumes.html | 73.0 | 203.5 |
| quality.html | 144.0 | 373.0 |
| cases/demandpilot.html | 133.0 | 348.5 |
| cases/transactionshield.html | 146.5 | 447.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
