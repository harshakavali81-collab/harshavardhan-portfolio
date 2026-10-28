# Portfolio verification results

Generated UTC: 2026-10-28T08:16:32.201575+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 122 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 49.0 | 308.0 |
| work.html | 40.5 | 352.5 |
| evidence.html | 51.0 | 362.0 |
| engineering.html | 29.0 | 345.0 |
| proof-map.html | 50.0 | 346.5 |
| hiring.html | 34.5 | 293.0 |
| interview.html | 29.5 | 317.0 |
| profile.html | 55.0 | 369.0 |
| contact.html | 42.5 | 343.0 |
| resumes.html | 21.5 | 194.0 |
| quality.html | 27.5 | 293.0 |
| cases/demandpilot.html | 29.5 | 351.5 |
| cases/transactionshield.html | 29.5 | 321.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
