# Portfolio verification results

Generated UTC: 2026-10-28T08:15:33.661761+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 121 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 100.5 | 321.5 |
| work.html | 160.5 | 384.0 |
| evidence.html | 272.5 | 398.5 |
| engineering.html | 103.0 | 373.0 |
| proof-map.html | 105.0 | 388.5 |
| hiring.html | 105.5 | 370.0 |
| interview.html | 107.5 | 374.0 |
| profile.html | 162.0 | 400.5 |
| contact.html | 127.5 | 366.0 |
| resumes.html | 110.0 | 221.0 |
| quality.html | 117.0 | 332.0 |
| cases/demandpilot.html | 107.0 | 344.5 |
| cases/transactionshield.html | 109.5 | 382.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
