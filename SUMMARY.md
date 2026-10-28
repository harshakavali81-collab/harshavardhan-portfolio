# Portfolio verification results

Generated UTC: 2026-10-28T07:38:58.802404+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 62 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 129.0 | 319.0 |
| work.html | 134.0 | 347.5 |
| evidence.html | 205.5 | 378.0 |
| engineering.html | 143.5 | 344.5 |
| proof-map.html | 126.5 | 365.0 |
| hiring.html | 83.5 | 336.0 |
| interview.html | 114.0 | 357.5 |
| profile.html | 103.0 | 194.0 |
| contact.html | 163.5 | 358.5 |
| resumes.html | 108.5 | 210.0 |
| quality.html | 149.5 | 326.0 |
| cases/demandpilot.html | 105.0 | 330.5 |
| cases/transactionshield.html | 159.5 | 370.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
