# Portfolio verification results

Generated UTC: 2026-10-28T08:31:57.855009+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 107 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 143/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 51.5 | 302.5 |
| work.html | 58.5 | 396.0 |
| evidence.html | 53.5 | 409.0 |
| engineering.html | 42.5 | 375.0 |
| proof-map.html | 52.5 | 380.5 |
| hiring.html | 42.5 | 350.5 |
| interview.html | 45.0 | 350.0 |
| profile.html | 40.0 | 341.5 |
| contact.html | 60.0 | 367.0 |
| resumes.html | 49.0 | 345.5 |
| quality.html | 44.0 | 324.0 |
| cases/demandpilot.html | 41.0 | 342.5 |
| cases/transactionshield.html | 43.5 | 331.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
