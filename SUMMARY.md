# Portfolio verification results

Generated UTC: 2026-10-28T08:13:11.875651+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 126.0 | 359.5 |
| work.html | 230.0 | 395.5 |
| evidence.html | 445.5 | 385.5 |
| engineering.html | 119.5 | 374.5 |
| proof-map.html | 143.0 | 392.5 |
| hiring.html | 124.5 | 377.0 |
| interview.html | 112.0 | 368.0 |
| profile.html | 114.5 | 240.5 |
| contact.html | 129.5 | 372.5 |
| resumes.html | 100.5 | 297.5 |
| quality.html | 88.0 | 313.0 |
| cases/demandpilot.html | 128.5 | 380.5 |
| cases/transactionshield.html | 124.5 | 349.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
