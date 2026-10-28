# Portfolio verification results

Generated UTC: 2026-10-28T14:44:48.509588+00:00

## Direct checks
- Live and current-release URL checks: 25/25
- External links: 170 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 200/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 349.5 | 1906.0 |
| flagship-projects.html | 136.0 | 567.5 |
| certificates.html | 149.5 | 1100.0 |
| portfolio-readiness.html | 158.5 | 1292.0 |
| career-portfolio.html | 121.0 | 552.0 |
| work.html | 227.0 | 1724.5 |
| job-platforms.html | 211.0 | 1339.5 |
| evidence.html | 230.0 | 1725.5 |
| engineering.html | 124.0 | 1355.0 |
| proof-map.html | 187.0 | 1331.5 |
| hiring.html | 145.0 | 1347.0 |
| interview.html | 132.0 | 1339.0 |
| profile.html | 237.0 | 1462.5 |
| contact.html | 189.5 | 1342.0 |
| resumes.html | 133.0 | 608.0 |
| quality.html | 138.0 | 993.5 |
| cases/demandpilot.html | 129.5 | 1356.5 |
| cases/transactionshield.html | 132.0 | 1368.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
