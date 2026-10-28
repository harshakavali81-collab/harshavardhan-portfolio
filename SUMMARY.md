# Portfolio verification results

Generated UTC: 2026-10-28T10:00:18.267039+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 168/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 311.0 | 1000.5 |
| work.html | 331.0 | 1380.5 |
| job-platforms.html | 226.0 | 784.0 |
| evidence.html | 255.0 | 1398.0 |
| engineering.html | 224.0 | 984.5 |
| proof-map.html | 288.0 | 1345.5 |
| hiring.html | 225.0 | 1081.5 |
| interview.html | 166.5 | 1345.5 |
| profile.html | 184.5 | 973.5 |
| contact.html | 262.0 | 987.0 |
| resumes.html | 198.5 | 969.5 |
| quality.html | 187.5 | 1040.5 |
| cases/demandpilot.html | 188.0 | 1042.0 |
| cases/transactionshield.html | 232.0 | 984.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
