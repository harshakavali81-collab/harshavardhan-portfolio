# Portfolio verification results

Generated UTC: 2026-10-29T08:40:42.303540+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 272 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 182/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): FAIL / NOT VERIFIED

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 368.0 | 11967.0 |
| flagship-projects.html | 160.5 | 1370.0 |
| certificates.html | 152.5 | 1550.5 |
| portfolio-readiness.html | 203.0 | 1547.5 |
| career-portfolio.html | 151.0 | 1195.0 |
| work.html | 255.0 | 2051.5 |
| job-platforms.html | 240.0 | 1717.5 |
| evidence.html | 242.5 | 2444.5 |
| engineering.html | 135.0 | 1720.0 |
| proof-map.html | 243.0 | 1715.0 |
| hiring.html | 132.0 | 1593.0 |
| interview.html | 177.0 | 1603.0 |
| profile.html | 276.0 | 1922.5 |
| contact.html | 246.0 | 1595.5 |
| resumes.html | 139.0 | 1854.5 |
| quality.html | 140.5 | 1107.5 |
| cases/demandpilot.html | 155.0 | 636.5 |
| cases/transactionshield.html | 125.0 | 1601.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
