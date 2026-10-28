# Portfolio verification results

Generated UTC: 2026-10-28T08:09:07.418573+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 106 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 153.5 | 276.5 |
| work.html | 181.0 | 334.0 |
| evidence.html | 174.5 | 354.5 |
| engineering.html | 118.5 | 321.5 |
| proof-map.html | 164.5 | 345.0 |
| hiring.html | 138.0 | 292.5 |
| interview.html | 116.5 | 384.5 |
| profile.html | 127.0 | 202.0 |
| contact.html | 105.5 | 337.0 |
| resumes.html | 122.5 | 193.5 |
| quality.html | 136.5 | 325.0 |
| cases/demandpilot.html | 138.0 | 293.0 |
| cases/transactionshield.html | 133.5 | 343.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
