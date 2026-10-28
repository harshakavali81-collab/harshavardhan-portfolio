# Portfolio verification results

Generated UTC: 2026-10-28T08:12:01.525267+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 128.0 | 369.5 |
| work.html | 153.0 | 394.0 |
| evidence.html | 153.0 | 405.0 |
| engineering.html | 117.5 | 352.5 |
| proof-map.html | 118.0 | 390.0 |
| hiring.html | 113.5 | 354.5 |
| interview.html | 108.5 | 353.0 |
| profile.html | 91.5 | 235.0 |
| contact.html | 127.0 | 381.0 |
| resumes.html | 95.0 | 214.5 |
| quality.html | 110.0 | 382.5 |
| cases/demandpilot.html | 119.0 | 361.0 |
| cases/transactionshield.html | 114.0 | 323.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
