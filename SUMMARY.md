# Portfolio verification results

Generated UTC: 2026-10-28T08:12:49.026968+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 117 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 86.5 | 379.5 |
| work.html | 92.5 | 412.0 |
| evidence.html | 104.5 | 400.5 |
| engineering.html | 90.0 | 388.0 |
| proof-map.html | 113.0 | 440.5 |
| hiring.html | 90.0 | 389.0 |
| interview.html | 90.5 | 384.5 |
| profile.html | 92.0 | 294.0 |
| contact.html | 104.5 | 388.0 |
| resumes.html | 69.0 | 238.5 |
| quality.html | 113.0 | 389.5 |
| cases/demandpilot.html | 115.5 | 401.0 |
| cases/transactionshield.html | 91.5 | 396.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
