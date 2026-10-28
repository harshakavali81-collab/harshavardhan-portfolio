# Portfolio verification results

Generated UTC: 2026-10-28T14:19:50.551603+00:00

## Direct checks
- Live and current-release URL checks: 24/24
- External links: 166 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 192/192 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 513.5 | 1914.0 |
| certificates.html | 242.0 | 586.5 |
| portfolio-readiness.html | 216.0 | 1148.0 |
| career-portfolio.html | 202.0 | 1256.0 |
| work.html | 335.5 | 1697.5 |
| job-platforms.html | 283.0 | 1317.5 |
| evidence.html | 311.5 | 1716.0 |
| engineering.html | 167.0 | 1317.5 |
| proof-map.html | 292.5 | 1382.0 |
| hiring.html | 188.5 | 1308.0 |
| interview.html | 228.5 | 1028.5 |
| profile.html | 402.0 | 1408.5 |
| contact.html | 278.0 | 1316.5 |
| resumes.html | 196.0 | 1283.5 |
| quality.html | 201.0 | 1347.5 |
| cases/demandpilot.html | 160.5 | 1314.0 |
| cases/transactionshield.html | 219.0 | 1331.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
