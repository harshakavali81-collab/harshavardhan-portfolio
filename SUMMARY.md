# Portfolio verification results

Generated UTC: 2026-10-29T08:35:23.141653+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 272 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 181/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): FAIL / NOT VERIFIED

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 348.0 | 16378.5 |
| flagship-projects.html | 70.5 | 1338.5 |
| certificates.html | 73.5 | 1521.5 |
| portfolio-readiness.html | 79.0 | 1499.5 |
| career-portfolio.html | 73.5 | 1824.5 |
| work.html | 206.0 | 2052.5 |
| job-platforms.html | 161.5 | 1731.5 |
| evidence.html | 193.0 | 2420.0 |
| engineering.html | 268.5 | 1720.0 |
| proof-map.html | 132.0 | 1694.5 |
| hiring.html | 80.5 | 1567.0 |
| interview.html | 208.0 | 1566.5 |
| profile.html | 219.0 | 1949.5 |
| contact.html | 154.5 | 1567.0 |
| resumes.html | 72.5 | 1833.0 |
| quality.html | 74.5 | 1585.0 |
| cases/demandpilot.html | 82.5 | 1596.0 |
| cases/transactionshield.html | 81.0 | 1598.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
