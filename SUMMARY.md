# Portfolio verification results

Generated UTC: 2026-10-28T07:12:09.525512+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 54 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 147.0 | 338.5 |
| work.html | 248.5 | 378.0 |
| proof-map.html | 107.5 | 394.5 |
| profile.html | 94.0 | 229.5 |
| contact.html | 132.5 | 385.5 |
| resumes.html | 97.0 | 238.5 |
| quality.html | 112.0 | 349.5 |
| cases/demandpilot.html | 104.5 | 394.5 |
| cases/transactionshield.html | 111.5 | 388.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
