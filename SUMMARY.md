# Portfolio verification results

Generated UTC: 2026-10-28T08:08:14.042975+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 106 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 106.5 | 285.0 |
| work.html | 154.0 | 349.0 |
| evidence.html | 146.0 | 362.5 |
| engineering.html | 91.5 | 326.0 |
| proof-map.html | 161.5 | 356.0 |
| hiring.html | 98.0 | 343.0 |
| interview.html | 107.0 | 347.5 |
| profile.html | 88.5 | 208.5 |
| contact.html | 92.0 | 351.5 |
| resumes.html | 93.5 | 205.5 |
| quality.html | 104.0 | 314.5 |
| cases/demandpilot.html | 104.5 | 327.5 |
| cases/transactionshield.html | 103.0 | 335.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
