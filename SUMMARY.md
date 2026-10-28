# Portfolio verification results

Generated UTC: 2026-10-28T11:05:54.410153+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 55/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 184.5 | 1536.0 |
| work.html | 89.5 | 1439.5 |
| job-platforms.html | 86.0 | 632.0 |
| evidence.html | 105.0 | 868.0 |
| engineering.html | 377.5 | 789.0 |
| proof-map.html | 99.0 | 781.5 |
| hiring.html | 59.5 | 855.0 |
| interview.html | 56.5 | 791.5 |
| profile.html | 114.5 | 815.5 |
| contact.html | 116.0 | 791.5 |
| resumes.html | 341.0 | 759.5 |
| quality.html | 60.0 | 791.5 |
| cases/demandpilot.html | 63.5 | 789.0 |
| cases/transactionshield.html | 69.5 | 793.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
