# Portfolio verification results

Generated UTC: 2026-10-28T15:52:26.341848+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 169 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 191/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 533.0 | 2239.5 |
| flagship-projects.html | 255.5 | 1004.0 |
| certificates.html | 251.0 | 1545.0 |
| portfolio-readiness.html | 230.5 | 1517.5 |
| career-portfolio.html | 218.5 | 1821.0 |
| work.html | 321.5 | 2082.0 |
| job-platforms.html | 319.5 | 1734.5 |
| evidence.html | 288.0 | 2411.5 |
| engineering.html | 193.5 | 1727.0 |
| proof-map.html | 304.5 | 1722.0 |
| hiring.html | 195.0 | 1569.5 |
| interview.html | 229.0 | 1585.5 |
| profile.html | 357.0 | 1933.0 |
| contact.html | 284.5 | 1571.0 |
| resumes.html | 228.0 | 1832.5 |
| quality.html | 234.5 | 1585.5 |
| cases/demandpilot.html | 263.0 | 1686.0 |
| cases/transactionshield.html | 229.5 | 1096.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
