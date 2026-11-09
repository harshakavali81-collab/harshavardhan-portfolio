# Portfolio verification results

Generated UTC: 2026-11-09T12:58:01.634193+00:00

Source commit: 44bc7aec7f5823c9827039a111e4b42b003cb85e

## Direct checks
- Live and current-release URL checks: 26/26
- External links: 275 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 208/208 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 334.0 | 2572.5 |
| all-projects.html | 237.5 | 1797.5 |
| flagship-projects.html | 152.5 | 1359.0 |
| certificates.html | 134.5 | 1555.0 |
| portfolio-readiness.html | 134.5 | 1524.0 |
| career-portfolio.html | 129.5 | 1815.5 |
| work.html | 239.0 | 2065.0 |
| job-platforms.html | 224.0 | 1722.5 |
| evidence.html | 228.5 | 1619.5 |
| engineering.html | 130.0 | 1724.0 |
| proof-map.html | 225.5 | 1709.0 |
| hiring.html | 132.0 | 1598.5 |
| interview.html | 125.0 | 1584.0 |
| profile.html | 262.0 | 1919.0 |
| contact.html | 214.5 | 1587.5 |
| resumes.html | 129.5 | 1846.5 |
| quality.html | 137.0 | 1588.5 |
| cases/demandpilot.html | 125.5 | 1762.0 |
| cases/transactionshield.html | 141.0 | 1592.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
