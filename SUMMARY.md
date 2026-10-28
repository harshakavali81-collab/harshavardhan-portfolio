# Portfolio verification results

Generated UTC: 2026-10-28T07:15:13.279736+00:00

## Direct checks
- Live URL HTTP 200: 15/15
- External links: 59 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 120/120 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 83.0 | 343.5 |
| work.html | 131.0 | 410.0 |
| proof-map.html | 95.5 | 383.0 |
| profile.html | 73.5 | 241.5 |
| contact.html | 104.0 | 370.0 |
| resumes.html | 143.0 | 223.0 |
| quality.html | 95.5 | 368.5 |
| cases/demandpilot.html | 91.0 | 385.0 |
| cases/transactionshield.html | 90.5 | 388.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
