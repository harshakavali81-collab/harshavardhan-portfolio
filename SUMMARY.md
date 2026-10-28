# Portfolio verification results

Generated UTC: 2026-10-28T08:32:43.429004+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 34 reachable; 0 broken; 107 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 143/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 51.0 | 310.0 |
| work.html | 52.0 | 386.5 |
| evidence.html | 66.0 | 409.5 |
| engineering.html | 51.0 | 378.5 |
| proof-map.html | 57.0 | 875.0 |
| hiring.html | 56.0 | 978.5 |
| interview.html | 50.0 | 1338.0 |
| profile.html | 54.0 | 969.0 |
| contact.html | 37.0 | 976.5 |
| resumes.html | 47.0 | 995.5 |
| quality.html | 48.5 | 973.0 |
| cases/demandpilot.html | 42.0 | 980.0 |
| cases/transactionshield.html | 48.0 | 986.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
