# Portfolio verification results

Generated UTC: 2026-10-28T13:47:33.251474+00:00

## Direct checks
- Live and current-release URL checks: 23/23
- External links: 163 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 184/184 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 446.0 | 1910.0 |
| portfolio-readiness.html | 197.0 | 913.0 |
| career-portfolio.html | 247.0 | 933.5 |
| work.html | 296.5 | 1755.0 |
| job-platforms.html | 312.5 | 1357.0 |
| evidence.html | 316.5 | 1758.0 |
| engineering.html | 241.0 | 1365.5 |
| proof-map.html | 299.0 | 1371.5 |
| hiring.html | 195.0 | 1378.0 |
| interview.html | 195.0 | 1350.5 |
| profile.html | 353.5 | 1491.5 |
| contact.html | 318.5 | 1376.0 |
| resumes.html | 237.0 | 1337.0 |
| quality.html | 213.5 | 1365.5 |
| cases/demandpilot.html | 221.0 | 1385.0 |
| cases/transactionshield.html | 195.5 | 1383.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
