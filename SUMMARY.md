# Portfolio verification results

Generated UTC: 2026-10-28T06:28:17.703057+00:00

## Direct checks
- Live URL HTTP 200: 14/14
- External links: 51 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 112/112 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 48.0 | 343.0 |
| work.html | 61.5 | 366.0 |
| profile.html | 35.5 | 221.5 |
| contact.html | 60.5 | 369.5 |
| resumes.html | 36.5 | 226.0 |
| quality.html | 40.5 | 369.0 |
| cases/demandpilot.html | 33.5 | 387.5 |
| cases/transactionshield.html | 35.5 | 392.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
