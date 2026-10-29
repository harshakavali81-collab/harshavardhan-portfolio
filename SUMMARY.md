# Portfolio verification results

Generated UTC: 2026-10-29T08:07:00.929759+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 252 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 182/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 567.5 | 2412.0 |
| flagship-projects.html | 189.5 | 1381.5 |
| certificates.html | 311.0 | 1560.5 |
| portfolio-readiness.html | 203.0 | 1542.0 |
| career-portfolio.html | 240.0 | 1825.5 |
| work.html | 343.5 | 2077.5 |
| job-platforms.html | 309.0 | 1738.0 |
| evidence.html | 432.5 | 2447.5 |
| engineering.html | 229.5 | 1734.5 |
| proof-map.html | 326.0 | 1731.5 |
| hiring.html | 259.5 | 1625.5 |
| interview.html | 206.0 | 1118.0 |
| profile.html | 368.5 | 1939.0 |
| contact.html | 360.5 | 1595.5 |
| resumes.html | 214.5 | 1873.0 |
| quality.html | 361.0 | 1605.5 |
| cases/demandpilot.html | 249.5 | 1605.0 |
| cases/transactionshield.html | 226.0 | 1624.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
