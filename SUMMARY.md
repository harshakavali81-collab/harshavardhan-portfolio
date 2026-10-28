# Portfolio verification results

Generated UTC: 2026-10-28T06:50:56.995079+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 54 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 58.5 | 342.5 |
| work.html | 90.5 | 361.0 |
| proof-map.html | 62.5 | 375.5 |
| profile.html | 45.0 | 234.5 |
| contact.html | 62.0 | 361.5 |
| resumes.html | 42.0 | 218.0 |
| quality.html | 56.0 | 360.0 |
| cases/demandpilot.html | 52.0 | 300.5 |
| cases/transactionshield.html | 49.0 | 336.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
