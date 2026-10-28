# Portfolio verification results

Generated UTC: 2026-10-28T09:10:34.958720+00:00

## Direct checks
- Live URL HTTP 200: 19/19
- External links: 152 reachable; 0 broken; 1 access-limited/unknown; 0 HTTP errors
- Chromium, Firefox and WebKit viewport tests: 151/152 passed
- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): PASS

## Performance: p75 page-load event, 3 cold contexts per case

| Page | Desktop ms | Simulated 4G mobile ms |
|---|---:|---:|
| index.html | 275.5 | 994.5 |
| work.html | 245.5 | 1375.5 |
| evidence.html | 259.5 | 1375.5 |
| engineering.html | 141.0 | 996.0 |
| proof-map.html | 211.5 | 1337.5 |
| hiring.html | 174.0 | 980.0 |
| interview.html | 173.0 | 1345.0 |
| profile.html | 182.0 | 965.5 |
| contact.html | 219.5 | 988.0 |
| resumes.html | 141.5 | 965.5 |
| quality.html | 144.0 | 979.0 |
| cases/demandpilot.html | 168.0 | 976.5 |
| cases/transactionshield.html | 130.5 | 983.5 |

## Limits
- All measured timings are from GitHub-hosted runners, not universal user experiences.
- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.
- Internal links and target files are separately checked by the existing static-site audit.
- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.
- screenshots/ contains representative desktop, tablet and mobile browser renders.
