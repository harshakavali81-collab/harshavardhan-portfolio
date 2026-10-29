# Portfolio verification results

Generated UTC: 2026-10-29T07:53:47.727452+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 240 reachable; 2 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 181/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 278.5 | 2241.0 |
| flagship-projects.html | 88.0 | 1331.0 |
| certificates.html | 87.5 | 1513.5 |
| portfolio-readiness.html | 60.5 | 1036.0 |
| career-portfolio.html | 70.5 | 1800.5 |
| work.html | 213.0 | 2037.0 |
| job-platforms.html | 168.0 | 1701.0 |
| evidence.html | 165.5 | 2388.0 |
| engineering.html | 73.0 | 1690.5 |
| proof-map.html | 133.0 | 1678.0 |
| hiring.html | 66.0 | 1558.0 |
| interview.html | 63.5 | 1548.0 |
| profile.html | 176.0 | 1903.5 |
| contact.html | 136.5 | 1543.0 |
| resumes.html | 69.5 | 1813.0 |
| quality.html | 71.0 | 1570.0 |
| cases/demandpilot.html | 96.5 | 1566.0 |
| cases/transactionshield.html | 70.0 | 1566.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
