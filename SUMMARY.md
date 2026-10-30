# Portfolio verification results

Generated UTC: 2026-10-30T03:12:47.039924+00:00

Source commit: 00e615767b56f543705c697d2672e23c94b98ab5

## Direct checks
- Live and current-release URL checks: 26/26
- External links: 275 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 208/208 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 457.0 | 2597.5 |
| all-projects.html | 398.5 | 1826.5 |
| flagship-projects.html | 291.5 | 1051.5 |
| certificates.html | 180.5 | 1129.0 |
| portfolio-readiness.html | 212.0 | 1584.5 |
| career-portfolio.html | 267.5 | 1241.5 |
| work.html | 389.0 | 2172.0 |
| job-platforms.html | 407.0 | 1786.5 |
| evidence.html | 384.5 | 1699.0 |
| engineering.html | 239.5 | 1772.5 |
| proof-map.html | 333.5 | 1775.5 |
| hiring.html | 197.5 | 1648.0 |
| interview.html | 291.5 | 1166.0 |
| profile.html | 405.0 | 1976.5 |
| contact.html | 418.0 | 1670.5 |
| resumes.html | 227.5 | 671.0 |
| quality.html | 257.0 | 678.5 |
| cases/demandpilot.html | 211.5 | 1823.0 |
| cases/transactionshield.html | 172.0 | 1651.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
