# Portfolio verification results

Generated UTC: 2026-11-23T14:45:14.965367+00:00

Source commit: 44bc7aec7f5823c9827039a111e4b42b003cb85e

## Direct checks
- Live and current-release URL checks: 26/26
- External links: 275 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 208/208 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 481.5 | 2588.5 |
| all-projects.html | 473.5 | 1745.0 |
| flagship-projects.html | 367.5 | 1368.0 |
| certificates.html | 199.0 | 1538.5 |
| portfolio-readiness.html | 329.0 | 888.0 |
| career-portfolio.html | 225.5 | 1324.5 |
| work.html | 671.0 | 2058.0 |
| job-platforms.html | 258.0 | 1772.5 |
| evidence.html | 404.0 | 1744.5 |
| engineering.html | 220.5 | 1809.5 |
| proof-map.html | 316.0 | 1734.5 |
| hiring.html | 283.5 | 1594.5 |
| interview.html | 195.0 | 1661.0 |
| profile.html | 311.5 | 1903.5 |
| contact.html | 299.5 | 1592.0 |
| resumes.html | 331.5 | 1869.0 |
| quality.html | 184.0 | 1133.5 |
| cases/demandpilot.html | 176.0 | 1798.0 |
| cases/transactionshield.html | 234.0 | 1148.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
