# Portfolio verification results

Generated UTC: 2026-10-28T08:32:20.895066+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 107 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 142/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 57.5 | 299.5 |
| work.html | 66.5 | 388.0 |
| evidence.html | 100.0 | 418.5 |
| engineering.html | 73.0 | 365.5 |
| proof-map.html | 70.0 | 395.5 |
| hiring.html | 69.5 | 362.5 |
| interview.html | 75.5 | 334.5 |
| profile.html | 66.0 | 381.5 |
| contact.html | 79.0 | 392.5 |
| resumes.html | 75.5 | 360.0 |
| quality.html | 63.5 | 329.5 |
| cases/demandpilot.html | 73.5 | 693.0 |
| cases/transactionshield.html | 59.0 | 1029.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
