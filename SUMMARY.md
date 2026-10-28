# Portfolio verification results

Generated UTC: 2026-10-28T06:27:22.512705+00:00

## Direct checks
- Live URL HTTP 200: 14/14
- External links: 51 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 112/112 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 121.5 | 320.0 |
| work.html | 225.0 | 358.5 |
| profile.html | 168.5 | 232.0 |
| contact.html | 258.5 | 365.5 |
| resumes.html | 62.5 | 212.0 |
| quality.html | 119.0 | 335.0 |
| cases/demandpilot.html | 111.0 | 339.0 |
| cases/transactionshield.html | 140.0 | 338.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
