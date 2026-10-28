# Portfolio verification results

Generated UTC: 2026-10-28T13:03:11.401946+00:00

## Direct checks
- Live and current-release URL checks: 22/22
- External links: 162 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 175/176 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 451.0 | 2003.0 |
| career-portfolio.html | 125.0 | 1310.5 |
| work.html | 305.5 | 1722.5 |
| job-platforms.html | 261.0 | 1398.0 |
| evidence.html | 268.5 | 1748.0 |
| engineering.html | 123.5 | 1367.5 |
| proof-map.html | 242.0 | 1669.5 |
| hiring.html | 195.5 | 1361.0 |
| interview.html | 127.0 | 1681.0 |
| profile.html | 274.5 | 1463.0 |
| contact.html | 211.0 | 1358.0 |
| resumes.html | 121.0 | 1311.0 |
| quality.html | 121.0 | 1358.5 |
| cases/demandpilot.html | 119.0 | 1348.0 |
| cases/transactionshield.html | 124.0 | 1369.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
