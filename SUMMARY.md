# Portfolio verification results

Generated UTC: 2026-10-28T06:25:15.189573+00:00

## Direct checks
- Live URL HTTP 200: 13/13
- External links: 51 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 104/104 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 102.0 | 277.0 |
| work.html | 158.0 | 360.5 |
| profile.html | 64.5 | 228.5 |
| contact.html | 92.0 | 363.5 |
| resumes.html | 95.0 | 211.5 |
| cases/demandpilot.html | 113.5 | 340.5 |
| cases/transactionshield.html | 106.5 | 364.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
