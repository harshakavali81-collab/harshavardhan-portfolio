# Portfolio verification results

Generated UTC: 2026-10-28T08:11:29.490395+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 116 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 37.0 | 364.0 |
| work.html | 50.5 | 390.5 |
| evidence.html | 66.0 | 378.0 |
| engineering.html | 31.0 | 369.0 |
| proof-map.html | 56.5 | 390.0 |
| hiring.html | 35.5 | 371.0 |
| interview.html | 36.5 | 362.5 |
| profile.html | 27.0 | 226.0 |
| contact.html | 55.5 | 365.5 |
| resumes.html | 30.5 | 210.5 |
| quality.html | 44.0 | 327.0 |
| cases/demandpilot.html | 32.5 | 294.0 |
| cases/transactionshield.html | 42.0 | 336.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
