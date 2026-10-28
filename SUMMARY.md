# Portfolio verification results

Generated UTC: 2026-10-28T08:19:47.311693+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 136 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 152/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 63.5 | 355.0 |
| work.html | 60.5 | 405.5 |
| evidence.html | 46.5 | 420.0 |
| engineering.html | 45.5 | 392.5 |
| proof-map.html | 2936.0 | 406.5 |
| hiring.html | 48.0 | 317.0 |
| interview.html | 336.5 | 315.5 |
| profile.html | 36.0 | 473.5 |
| contact.html | 549.5 | 389.5 |
| resumes.html | 28.0 | 326.5 |
| quality.html | 29.0 | 361.5 |
| cases/demandpilot.html | 31.5 | 372.5 |
| cases/transactionshield.html | 26.5 | 372.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
