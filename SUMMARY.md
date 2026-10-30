# Portfolio verification results

Generated UTC: 2026-10-30T16:00:14.869173+00:00

Source commit: 98215ea228e44ffc3e611c09e2c8584a29b99e32

## Direct checks
- Live and current-release URL checks: 26/26
- External links: 275 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 208/208 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 401.0 | 2586.0 |
| all-projects.html | 529.5 | 1790.0 |
| flagship-projects.html | 217.5 | 1448.0 |
| certificates.html | 198.0 | 1589.5 |
| portfolio-readiness.html | 296.0 | 1588.5 |
| career-portfolio.html | 221.5 | 597.5 |
| work.html | 361.5 | 2111.5 |
| job-platforms.html | 393.0 | 1837.5 |
| evidence.html | 367.0 | 1813.5 |
| engineering.html | 187.0 | 1208.0 |
| proof-map.html | 356.5 | 1753.0 |
| hiring.html | 226.0 | 1640.5 |
| interview.html | 220.0 | 1148.5 |
| profile.html | 375.5 | 1933.0 |
| contact.html | 335.5 | 1651.5 |
| resumes.html | 204.0 | 2000.0 |
| quality.html | 187.0 | 693.5 |
| cases/demandpilot.html | 197.0 | 1807.0 |
| cases/transactionshield.html | 174.0 | 1633.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
