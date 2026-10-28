# Portfolio verification results

Generated UTC: 2026-10-28T07:14:21.853228+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 143.0 | 277.0 |
| work.html | 263.5 | 329.5 |
| proof-map.html | 113.0 | 344.0 |
| profile.html | 98.0 | 206.5 |
| contact.html | 188.0 | 361.5 |
| resumes.html | 129.0 | 196.5 |
| quality.html | 144.5 | 466.0 |
| cases/demandpilot.html | 183.5 | 322.5 |
| cases/transactionshield.html | 103.0 | 344.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
