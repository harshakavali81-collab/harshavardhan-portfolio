# Portfolio verification results

Generated UTC: 2026-10-28T14:07:58.176246+00:00

## Direct checks
- Live and current-release URL checks: 23/23
- External links: 166 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 184/184 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 388.0 | 1847.0 |
| portfolio-readiness.html | 160.0 | 1170.0 |
| career-portfolio.html | 150.0 | 548.5 |
| work.html | 310.0 | 1718.5 |
| job-platforms.html | 229.0 | 1340.5 |
| evidence.html | 259.5 | 1716.0 |
| engineering.html | 149.0 | 1328.0 |
| proof-map.html | 276.5 | 1311.0 |
| hiring.html | 154.0 | 626.0 |
| interview.html | 161.5 | 1318.0 |
| profile.html | 253.0 | 1376.5 |
| contact.html | 246.5 | 1322.0 |
| resumes.html | 135.5 | 597.0 |
| quality.html | 188.5 | 972.0 |
| cases/demandpilot.html | 148.0 | 1325.0 |
| cases/transactionshield.html | 247.5 | 1311.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
