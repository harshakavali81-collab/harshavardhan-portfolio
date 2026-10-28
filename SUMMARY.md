# Portfolio verification results

Generated UTC: 2026-10-28T07:37:21.661132+00:00

## Direct checks
- Live URL HTTP 200: 17/17
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 136/136 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 28.5 | 300.0 |
| work.html | 43.5 | 338.5 |
| proof-map.html | 42.0 | 350.0 |
| hiring.html | 24.5 | 320.5 |
| interview.html | 24.5 | 292.0 |
| profile.html | 22.0 | 182.5 |
| contact.html | 34.5 | 340.0 |
| resumes.html | 21.5 | 200.5 |
| quality.html | 26.0 | 314.0 |
| cases/demandpilot.html | 34.5 | 322.0 |
| cases/transactionshield.html | 25.5 | 322.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
