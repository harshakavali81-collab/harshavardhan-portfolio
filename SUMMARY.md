# Portfolio verification results

Generated UTC: 2026-11-02T12:31:05.226644+00:00

Source commit: 44bc7aec7f5823c9827039a111e4b42b003cb85e

## Direct checks
- Live and current-release URL checks: 26/26
- External links: 275 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 208/208 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 241.0 | 2582.0 |
| all-projects.html | 279.0 | 1772.5 |
| flagship-projects.html | 92.0 | 966.5 |
| certificates.html | 110.5 | 1526.0 |
| portfolio-readiness.html | 85.0 | 1044.0 |
| career-portfolio.html | 138.5 | 1810.5 |
| work.html | 232.0 | 2052.5 |
| job-platforms.html | 243.0 | 1715.0 |
| evidence.html | 175.5 | 1638.5 |
| engineering.html | 115.0 | 1706.5 |
| proof-map.html | 495.5 | 1693.0 |
| hiring.html | 806.0 | 1569.0 |
| interview.html | 1158.5 | 1585.0 |
| profile.html | 252.5 | 1930.5 |
| contact.html | 161.0 | 1559.5 |
| resumes.html | 144.5 | 1829.5 |
| quality.html | 176.5 | 1581.0 |
| cases/demandpilot.html | 83.5 | 1748.0 |
| cases/transactionshield.html | 94.0 | 1588.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
