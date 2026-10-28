# Portfolio verification results

Generated UTC: 2026-10-28T10:48:31.103828+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 144/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 264.0 | 1187.5 |
| work.html | 198.5 | 854.5 |
| job-platforms.html | 124.5 | 646.0 |
| evidence.html | 150.5 | 897.0 |
| engineering.html | 110.5 | 819.5 |
| proof-map.html | 145.0 | 812.0 |
| hiring.html | 90.0 | 811.0 |
| interview.html | 90.0 | 811.5 |
| profile.html | 190.5 | 846.0 |
| contact.html | 326.5 | 819.0 |
| resumes.html | 88.5 | 785.5 |
| quality.html | 88.0 | 811.0 |
| cases/demandpilot.html | 145.5 | 815.0 |
| cases/transactionshield.html | 122.5 | 815.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
