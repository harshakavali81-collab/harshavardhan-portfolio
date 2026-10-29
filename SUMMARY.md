# Portfolio verification results

Generated UTC: 2026-10-29T14:35:44.131765+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 275 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 176/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): FAIL / NOT VERIFIED

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 455.5 | 11964.5 |
| flagship-projects.html | 212.0 | 1386.0 |
| certificates.html | 275.5 | 1581.0 |
| portfolio-readiness.html | 239.0 | 1098.5 |
| career-portfolio.html | 235.0 | 1866.5 |
| work.html | 444.5 | 2152.0 |
| job-platforms.html | 324.0 | 1803.0 |
| evidence.html | 288.0 | 1702.5 |
| engineering.html | 181.5 | 1779.0 |
| proof-map.html | 294.5 | 1750.5 |
| hiring.html | 183.0 | 1158.5 |
| interview.html | 244.0 | 1627.0 |
| profile.html | 355.0 | 1985.0 |
| contact.html | 295.5 | 1623.5 |
| resumes.html | 222.0 | 1926.5 |
| quality.html | 224.5 | 1643.0 |
| cases/demandpilot.html | 266.0 | 1832.0 |
| cases/transactionshield.html | 219.0 | 1645.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
