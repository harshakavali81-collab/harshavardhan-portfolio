# Portfolio verification results

Generated UTC: 2026-10-28T06:21:47.706037+00:00

## Direct checks
- Live URL HTTP 200: 13/13
- External links: 44 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 104/104 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 109.5 | 313.5 |
| work.html | 133.0 | 372.0 |
| profile.html | 142.5 | 241.5 |
| contact.html | 109.5 | 371.0 |
| resumes.html | 107.0 | 225.0 |
| cases/demandpilot.html | 93.0 | 381.5 |
| cases/transactionshield.html | 281.5 | 351.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
