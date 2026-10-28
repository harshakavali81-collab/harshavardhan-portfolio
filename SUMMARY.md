# Portfolio verification results

Generated UTC: 2026-10-28T14:31:00.526343+00:00

## Direct checks
- Live and current-release URL checks: 24/24
- External links: 166 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 192/192 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 482.0 | 1919.0 |
| certificates.html | 185.0 | 873.0 |
| portfolio-readiness.html | 211.0 | 1193.5 |
| career-portfolio.html | 141.5 | 932.0 |
| work.html | 289.5 | 1894.5 |
| job-platforms.html | 240.5 | 1344.5 |
| evidence.html | 265.0 | 1816.5 |
| engineering.html | 142.5 | 1344.0 |
| proof-map.html | 234.5 | 1356.5 |
| hiring.html | 146.5 | 1364.5 |
| interview.html | 145.0 | 1342.5 |
| profile.html | 257.0 | 1408.0 |
| contact.html | 243.0 | 1349.0 |
| resumes.html | 155.5 | 963.0 |
| quality.html | 151.5 | 1341.5 |
| cases/demandpilot.html | 134.0 | 993.5 |
| cases/transactionshield.html | 150.5 | 1365.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
