# Portfolio verification results

Generated UTC: 2026-10-28T16:18:29.106511+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 169 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 192/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): FAIL / NOT VERIFIED

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 299.5 | 2312.5 |
| flagship-projects.html | 103.0 | 947.0 |
| certificates.html | 104.0 | None |
| portfolio-readiness.html | 85.5 | 1592.5 |
| career-portfolio.html | 80.0 | 1814.5 |
| work.html | 231.5 | 2049.5 |
| job-platforms.html | 170.5 | 2140.5 |
| evidence.html | 213.0 | 2397.5 |
| engineering.html | 84.0 | 1201.5 |
| proof-map.html | 212.5 | 1687.0 |
| hiring.html | 89.0 | 1697.0 |
| interview.html | 94.5 | 2889.0 |
| profile.html | 213.5 | 1921.0 |
| contact.html | 158.0 | 1555.5 |
| resumes.html | 94.5 | 2593.5 |
| quality.html | 106.5 | 2211.0 |
| cases/demandpilot.html | 89.5 | 1581.5 |
| cases/transactionshield.html | 89.0 | 1587.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
