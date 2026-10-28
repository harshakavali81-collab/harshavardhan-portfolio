# Portfolio verification results

Generated UTC: 2026-10-28T08:27:14.923578+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 67.0 | 369.5 |
| work.html | 51.0 | 419.5 |
| evidence.html | 52.5 | 430.0 |
| engineering.html | 31.5 | 319.5 |
| proof-map.html | 48.5 | 407.5 |
| hiring.html | 45.0 | 407.0 |
| interview.html | 32.0 | 395.5 |
| profile.html | 28.0 | 360.0 |
| contact.html | 46.0 | 394.5 |
| resumes.html | 29.0 | 364.0 |
| quality.html | 30.5 | 365.5 |
| cases/demandpilot.html | 29.0 | 341.0 |
| cases/transactionshield.html | 30.5 | 384.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
