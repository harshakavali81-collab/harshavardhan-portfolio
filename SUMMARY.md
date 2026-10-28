# Portfolio verification results

Generated UTC: 2026-10-28T10:50:25.603243+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 144/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 301.0 | 1229.0 |
| work.html | 197.0 | 858.5 |
| job-platforms.html | 130.0 | 641.5 |
| evidence.html | 165.5 | 892.0 |
| engineering.html | 72.5 | 820.0 |
| proof-map.html | 119.5 | 812.5 |
| hiring.html | 72.0 | 822.5 |
| interview.html | 75.5 | 810.5 |
| profile.html | 173.0 | 850.0 |
| contact.html | 158.5 | 815.5 |
| resumes.html | 72.0 | 796.5 |
| quality.html | 71.0 | 819.0 |
| cases/demandpilot.html | 73.0 | 821.0 |
| cases/transactionshield.html | 74.0 | 827.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
