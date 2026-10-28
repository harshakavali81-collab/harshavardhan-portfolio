# Portfolio verification results

Generated UTC: 2026-10-28T11:09:16.012902+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 48/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 365.5 | 1199.0 |
| work.html | 186.0 | 866.0 |
| job-platforms.html | 184.5 | 679.5 |
| evidence.html | 247.5 | 905.0 |
| engineering.html | 157.0 | 829.0 |
| proof-map.html | 207.0 | 815.5 |
| hiring.html | 153.5 | 818.0 |
| interview.html | 133.5 | 812.0 |
| profile.html | 226.5 | 849.0 |
| contact.html | 162.0 | 826.5 |
| resumes.html | 144.0 | 815.5 |
| quality.html | 145.0 | 826.5 |
| cases/demandpilot.html | 156.0 | 823.0 |
| cases/transactionshield.html | 113.0 | 817.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
