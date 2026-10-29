# Portfolio verification results

Generated UTC: 2026-10-29T08:26:08.976766+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 282 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 181/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 599.0 | 2444.5 |
| flagship-projects.html | 270.5 | 1404.5 |
| certificates.html | 350.0 | 1122.0 |
| portfolio-readiness.html | 276.5 | 1622.5 |
| career-portfolio.html | 230.0 | 1860.0 |
| work.html | 378.0 | 2134.5 |
| job-platforms.html | 333.0 | 1771.5 |
| evidence.html | 399.5 | 2467.0 |
| engineering.html | 269.0 | 1209.5 |
| proof-map.html | 326.0 | 1761.0 |
| hiring.html | 291.5 | 1146.0 |
| interview.html | 285.0 | 1634.0 |
| profile.html | 538.5 | 1956.0 |
| contact.html | 394.5 | 1625.5 |
| resumes.html | 255.0 | 1269.5 |
| quality.html | 227.5 | 656.5 |
| cases/demandpilot.html | 264.5 | 1635.0 |
| cases/transactionshield.html | 210.5 | 1641.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
