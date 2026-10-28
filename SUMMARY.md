# Portfolio verification results

Generated UTC: 2026-10-28T06:42:57.730204+00:00

## Direct checks
- Live URL HTTP 200: 14/14
- External links: 52 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 112/112 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 230.5 | 280.5 |
| work.html | 128.5 | 421.0 |
| profile.html | 187.5 | 255.5 |
| contact.html | 158.5 | 417.5 |
| resumes.html | 192.5 | 195.0 |
| quality.html | 343.0 | 347.0 |
| cases/demandpilot.html | 203.0 | 432.5 |
| cases/transactionshield.html | 226.0 | 382.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
