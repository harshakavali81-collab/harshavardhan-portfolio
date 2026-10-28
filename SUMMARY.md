# Portfolio verification results

Generated UTC: 2026-10-28T11:01:19.668194+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 88/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 253.5 | 1261.0 |
| work.html | 204.0 | 853.5 |
| job-platforms.html | 96.5 | 655.5 |
| evidence.html | 121.5 | 887.5 |
| engineering.html | 74.5 | 819.0 |
| proof-map.html | 122.0 | 808.0 |
| hiring.html | 71.5 | 810.0 |
| interview.html | 131.5 | 810.5 |
| profile.html | 143.0 | 852.5 |
| contact.html | 127.5 | 829.0 |
| resumes.html | 67.5 | 788.0 |
| quality.html | 71.5 | 817.5 |
| cases/demandpilot.html | 70.0 | 819.0 |
| cases/transactionshield.html | 70.0 | 821.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
