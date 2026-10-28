# Portfolio verification results

Generated UTC: 2026-10-28T10:03:03.225743+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 160 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 168/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 217.0 | 977.5 |
| work.html | 186.5 | 1328.5 |
| job-platforms.html | 94.0 | 744.0 |
| evidence.html | 164.0 | 1371.0 |
| engineering.html | 63.0 | 948.0 |
| proof-map.html | 152.5 | 1310.5 |
| hiring.html | 69.0 | 946.5 |
| interview.html | 73.5 | 1320.0 |
| profile.html | 66.0 | 936.0 |
| contact.html | 113.5 | 951.0 |
| resumes.html | 71.0 | 920.0 |
| quality.html | 63.5 | 938.0 |
| cases/demandpilot.html | 65.5 | 958.5 |
| cases/transactionshield.html | 76.0 | 939.0 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
