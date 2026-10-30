# Portfolio verification results

Generated UTC: 2026-10-30T03:06:34.384478+00:00

Source commit: 55a28e6a4e7df2e15ffa3cb7767eb7993f9e0f0a

## Direct checks
- Live and current-release URL checks: 26/26
- External links: 275 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 206/208 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 501.5 | 2586.0 |
| all-projects.html | 396.0 | 1810.0 |
| flagship-projects.html | 211.5 | 1433.5 |
| certificates.html | 236.5 | 1584.0 |
| portfolio-readiness.html | 238.0 | 1316.5 |
| career-portfolio.html | 230.0 | 1254.0 |
| work.html | 430.0 | 2133.0 |
| job-platforms.html | 372.0 | 1770.0 |
| evidence.html | 347.5 | 1693.5 |
| engineering.html | 260.5 | 1209.0 |
| proof-map.html | 354.0 | 1762.5 |
| hiring.html | 224.0 | 1153.0 |
| interview.html | 195.5 | 669.0 |
| profile.html | 407.0 | 1959.5 |
| contact.html | 363.0 | 1663.0 |
| resumes.html | 244.0 | 1900.0 |
| quality.html | 232.5 | 680.0 |
| cases/demandpilot.html | 373.0 | 1227.0 |
| cases/transactionshield.html | 208.5 | 672.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
