# Portfolio verification results

Generated UTC: 2026-10-28T11:04:32.274589+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 64/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 367.5 | 1301.0 |
| work.html | 307.0 | 935.0 |
| job-platforms.html | 234.0 | 675.5 |
| evidence.html | 312.5 | 953.5 |
| engineering.html | 304.5 | 894.0 |
| proof-map.html | 304.0 | 890.0 |
| hiring.html | 256.0 | 897.5 |
| interview.html | 300.0 | 885.5 |
| profile.html | 358.5 | 917.5 |
| contact.html | 312.0 | 886.0 |
| resumes.html | 212.0 | 873.5 |
| quality.html | 318.0 | 894.0 |
| cases/demandpilot.html | 232.0 | 893.5 |
| cases/transactionshield.html | 283.0 | 901.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
