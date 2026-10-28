# Portfolio verification results

Generated UTC: 2026-10-28T10:58:13.401876+00:00

## Direct checks
- Live URL HTTP 200: 21/21
- External links: 159 reachable; 0 broken; 2 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 104/168 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 277.0 | 1209.0 |
| work.html | 182.5 | 858.0 |
| job-platforms.html | 138.0 | 639.5 |
| evidence.html | 238.5 | 874.0 |
| engineering.html | 107.5 | 810.0 |
| proof-map.html | 154.5 | 808.0 |
| hiring.html | 147.5 | 804.0 |
| interview.html | 73.0 | 817.5 |
| profile.html | 211.0 | 833.0 |
| contact.html | 155.5 | 815.5 |
| resumes.html | 152.0 | 788.5 |
| quality.html | 170.0 | 815.5 |
| cases/demandpilot.html | 168.0 | 809.5 |
| cases/transactionshield.html | 144.0 | 818.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
