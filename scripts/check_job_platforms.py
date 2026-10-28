#!/usr/bin/env python3
"""Check portfolio job-platform copy page and project-source catalog."""
from pathlib import Path
from html.parser import HTMLParser
import re
ROOT=Path(__file__).resolve().parents[1]
def text(path):return (ROOT/path).read_text(encoding="utf-8")
page=text("job-platforms.html")
assert page.count('class="panel project"')==15
assert len(re.findall(r'<li><a href="https://github.com/harshakavali81-collab/',page))==31
assert 'href="assets/luxury-theme.css"' in page
assert 'id="panel-linkedin"' in page and 'id="panel-naukri"' in page and 'id="panel-foundit"' in page
assert 'id="project-search"' in page and 'id="project-count"' in page
assert (ROOT/"assets/job-platforms.js").exists()
assert 'navigator.clipboard' in text("assets/job-platforms.js")
assert 'manual-copy' in text("assets/job-platforms.js")
for name in ("README.md","index.html","profile.html","linkedin-projects.html"):
    assert "job-platforms.html" in text(name), name
assert '## 8. Complete projects and recruiter profile center' in text("docs/JOB_PORTAL_PROFILE_KIT.md")
print("Profile center: 3 platforms, 15 projects, 31 sources, resume links and copy controls verified")
