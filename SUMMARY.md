# Portfolio verification results

Generated UTC: 2026-10-28T10:01:46.574777+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 160 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 168/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 363.5 | 1037.5 |
| work.html | 225.5 | 1373.5 |
| job-platforms.html | 194.0 | 785.5 |
| evidence.html | 226.5 | 1406.5 |
| engineering.html | 179.0 | 985.0 |
| proof-map.html | 208.5 | 1339.0 |
| hiring.html | 129.5 | 1018.0 |
| interview.html | 133.5 | 1346.0 |
| profile.html | 120.0 | 970.0 |
| contact.html | 188.0 | 981.5 |
| resumes.html | 150.5 | 961.0 |
| quality.html | 127.5 | 984.0 |
| cases/demandpilot.html | 159.5 | 981.0 |
| cases/transactionshield.html | 130.5 | 985.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
