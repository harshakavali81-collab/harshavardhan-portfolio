# Portfolio verification results

Generated UTC: 2026-10-28T06:19:12.939429+00:00

## Direct checks
- Live URL HTTP 200: 13/13
- External links: 42 reachable; 1 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 102/104 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 129.0 | 292.5 |
| work.html | 184.0 | 375.5 |
| profile.html | 68.0 | 222.0 |
| contact.html | 134.0 | 364.5 |
| resumes.html | 106.5 | 213.5 |
| cases/demandpilot.html | 117.5 | 312.0 |
| cases/transactionshield.html | 118.5 | 344.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
