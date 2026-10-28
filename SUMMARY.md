# Portfolio verification results

Generated UTC: 2026-10-28T13:18:08.261293+00:00

## Direct checks
- Live and current-release URL checks: 22/22
- External links: 162 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 175/176 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 797.5 | 2189.0 |
| career-portfolio.html | 298.0 | 1465.0 |
| work.html | 778.0 | 1906.0 |
| job-platforms.html | 933.5 | 1544.0 |
| evidence.html | 672.0 | 1920.0 |
| engineering.html | 324.0 | 1554.0 |
| proof-map.html | 632.0 | 1523.5 |
| hiring.html | 288.5 | 711.5 |
| interview.html | 291.0 | 1605.5 |
| profile.html | 666.0 | 1626.5 |
| contact.html | 630.0 | 1523.0 |
| resumes.html | 288.5 | 1495.0 |
| quality.html | 286.0 | 1529.5 |
| cases/demandpilot.html | 305.0 | 1560.0 |
| cases/transactionshield.html | 422.5 | 1528.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
