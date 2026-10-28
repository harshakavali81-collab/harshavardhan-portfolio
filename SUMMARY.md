# Portfolio verification results

Generated UTC: 2026-10-28T08:20:03.341785+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 103 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 177.5 | 331.5 |
| work.html | 68.5 | 404.5 |
| evidence.html | 491.0 | 426.0 |
| engineering.html | 100.0 | 397.0 |
| proof-map.html | 103.0 | 413.0 |
| hiring.html | 87.0 | 394.5 |
| interview.html | 95.5 | 393.0 |
| profile.html | 90.5 | 398.0 |
| contact.html | 105.0 | 398.0 |
| resumes.html | 97.0 | 346.5 |
| quality.html | 97.5 | 343.0 |
| cases/demandpilot.html | 104.5 | 347.5 |
| cases/transactionshield.html | 110.5 | 386.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
