# Portfolio verification results

Generated UTC: 2026-10-28T08:16:19.265664+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 122 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 92.5 | 377.5 |
| work.html | 148.5 | 398.5 |
| evidence.html | 143.0 | 385.5 |
| engineering.html | 98.0 | 372.0 |
| proof-map.html | 100.0 | 389.0 |
| hiring.html | 81.0 | 379.0 |
| interview.html | 87.0 | 367.5 |
| profile.html | 119.0 | 415.0 |
| contact.html | 101.0 | 375.5 |
| resumes.html | 75.5 | 199.0 |
| quality.html | 86.5 | 372.5 |
| cases/demandpilot.html | 80.0 | 348.5 |
| cases/transactionshield.html | 76.5 | 380.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
