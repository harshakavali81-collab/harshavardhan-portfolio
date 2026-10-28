# Portfolio verification results

Generated UTC: 2026-10-28T11:07:31.855775+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 40/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 330.0 | 1307.0 |
| work.html | 275.0 | 928.0 |
| job-platforms.html | 173.0 | 658.0 |
| evidence.html | 291.5 | 932.5 |
| engineering.html | 154.0 | 886.5 |
| proof-map.html | 267.5 | 888.0 |
| hiring.html | 262.5 | 879.5 |
| interview.html | 229.5 | 879.5 |
| profile.html | 283.5 | 894.0 |
| contact.html | 273.5 | 901.0 |
| resumes.html | 211.5 | 875.0 |
| quality.html | 163.5 | 895.0 |
| cases/demandpilot.html | 210.0 | 886.5 |
| cases/transactionshield.html | 222.0 | 878.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
