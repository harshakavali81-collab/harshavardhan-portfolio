# Portfolio verification results

Generated UTC: 2026-10-28T06:24:52.796640+00:00

## Direct checks
- Live URL HTTP 200: 13/13
- External links: 45 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 104/104 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 154.0 | 256.5 |
| work.html | 143.5 | 344.5 |
| profile.html | 122.5 | 196.0 |
| contact.html | 176.0 | 336.0 |
| resumes.html | 113.5 | 191.0 |
| cases/demandpilot.html | 215.5 | 336.0 |
| cases/transactionshield.html | 160.5 | 350.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
