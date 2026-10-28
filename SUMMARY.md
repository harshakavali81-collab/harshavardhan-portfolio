# Portfolio verification results

Generated UTC: 2026-10-28T08:27:48.815360+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 48.0 | 351.0 |
| work.html | 56.5 | 409.5 |
| evidence.html | 66.0 | 433.0 |
| engineering.html | 41.5 | 394.0 |
| proof-map.html | 46.5 | 405.0 |
| hiring.html | 56.0 | 397.5 |
| interview.html | 43.0 | 384.5 |
| profile.html | 49.0 | 399.0 |
| contact.html | 58.0 | 393.5 |
| resumes.html | 42.0 | 362.5 |
| quality.html | 43.5 | 330.0 |
| cases/demandpilot.html | 42.5 | 374.0 |
| cases/transactionshield.html | 42.5 | 338.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
