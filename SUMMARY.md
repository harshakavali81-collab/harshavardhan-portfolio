# Portfolio verification results

Generated UTC: 2026-10-28T07:17:39.422598+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 620.0 | 315.5 |
| work.html | 205.0 | 348.5 |
| proof-map.html | 213.5 | 363.0 |
| profile.html | 93.5 | 218.5 |
| contact.html | 80.0 | 348.0 |
| resumes.html | 96.5 | 210.5 |
| quality.html | 113.5 | 349.0 |
| cases/demandpilot.html | 65.0 | 330.0 |
| cases/transactionshield.html | 112.5 | 329.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
