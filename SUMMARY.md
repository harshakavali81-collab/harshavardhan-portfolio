# Portfolio verification results

Generated UTC: 2026-10-28T16:05:32.858223+00:00

## Direct checks
- Live and current-release URL checks: 24/25
- External links: 169 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 192/200 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 444.5 | 2313.0 |
| flagship-projects.html | 226.0 | 600.5 |
| certificates.html | 197.5 | 1552.5 |
| portfolio-readiness.html | 205.0 | 1102.5 |
| career-portfolio.html | 187.5 | 1843.0 |
| work.html | 366.5 | 2140.0 |
| job-platforms.html | 370.0 | 1748.0 |
| evidence.html | 344.5 | 2436.0 |
| engineering.html | 169.5 | 1186.0 |
| proof-map.html | 342.0 | 1742.5 |
| hiring.html | 204.0 | 1606.0 |
| interview.html | 211.0 | 1137.5 |
| profile.html | 388.0 | 1919.0 |
| contact.html | 346.5 | 1624.0 |
| resumes.html | 197.0 | 1262.0 |
| quality.html | 201.0 | 1782.0 |
| cases/demandpilot.html | 197.5 | 645.5 |
| cases/transactionshield.html | 194.0 | 1126.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
