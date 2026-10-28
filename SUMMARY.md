# Portfolio verification results

Generated UTC: 2026-10-28T08:20:42.894384+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 51.0 | 375.0 |
| work.html | 48.5 | 424.5 |
| evidence.html | 68.0 | 443.5 |
| engineering.html | 47.0 | 409.0 |
| proof-map.html | 54.5 | 414.5 |
| hiring.html | 44.5 | 415.0 |
| interview.html | 48.5 | 334.0 |
| profile.html | 46.5 | 369.5 |
| contact.html | 61.0 | 410.0 |
| resumes.html | 42.0 | 369.5 |
| quality.html | 43.5 | 376.0 |
| cases/demandpilot.html | 52.0 | 390.0 |
| cases/transactionshield.html | 50.5 | 389.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
