# Portfolio verification results

Generated UTC: 2026-11-16T12:50:36.718430+00:00

Source commit: 44bc7aec7f5823c9827039a111e4b42b003cb85e

## Direct checks
- Live and current-release URL checks: 26/26
- External links: 275 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 208/208 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 604.0 | 2586.5 |
| all-projects.html | 389.0 | 1787.5 |
| flagship-projects.html | 276.0 | 977.0 |
| certificates.html | 187.5 | 1548.0 |
| portfolio-readiness.html | 195.5 | 1540.5 |
| career-portfolio.html | 184.5 | 1187.5 |
| work.html | 279.5 | 2063.0 |
| job-platforms.html | 461.5 | 1737.0 |
| evidence.html | 469.5 | 1641.0 |
| engineering.html | 248.0 | 1172.5 |
| proof-map.html | 281.0 | 1738.5 |
| hiring.html | 168.5 | 1577.0 |
| interview.html | 212.5 | 1600.5 |
| profile.html | 396.5 | 1910.5 |
| contact.html | 358.0 | 1595.5 |
| resumes.html | 271.0 | 1858.0 |
| quality.html | 375.5 | 1611.5 |
| cases/demandpilot.html | 165.5 | 1206.0 |
| cases/transactionshield.html | 231.0 | 1596.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
