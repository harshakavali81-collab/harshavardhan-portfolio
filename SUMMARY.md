# Portfolio verification results

Generated UTC: 2026-10-28T07:36:10.465781+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 101.5 | 361.5 |
| work.html | 172.5 | 358.0 |
| proof-map.html | 110.5 | 376.0 |
| hiring.html | 105.0 | 361.5 |
| interview.html | 105.0 | 323.5 |
| profile.html | 95.5 | 222.0 |
| contact.html | 176.5 | 358.0 |
| resumes.html | 92.0 | 217.0 |
| quality.html | 109.5 | 371.5 |
| cases/demandpilot.html | 100.5 | 370.5 |
| cases/transactionshield.html | 96.5 | 349.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
