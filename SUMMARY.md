# Portfolio verification results

Generated UTC: 2026-10-28T06:40:21.945357+00:00

## Direct checks
- Live URL HTTP 200: 14/14
- External links: 51 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 112/112 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 109.5 | 292.5 |
| work.html | 141.0 | 374.0 |
| profile.html | 95.5 | 230.0 |
| contact.html | 121.0 | 370.5 |
| resumes.html | 91.0 | 223.5 |
| quality.html | 113.5 | 323.0 |
| cases/demandpilot.html | 109.0 | 354.5 |
| cases/transactionshield.html | 109.5 | 380.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
