#!/usr/bin/env python3
"""Check portfolio job-platform copy page and project-source catalog."""
from pathlib import Path
from html.parser import HTMLParser
import re
ROOT=Path(__file__).resolve().parents[1]
def text(path):return (ROOT/path).read_text(encoding="utf-8")
page=text("job-platforms.html")
assert page.count('class="panel project"')==31
assert page.count('data-tier="additional"')==16
assert 'id="project-scope"' in page
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
links=re.findall(r'class="btn source" href="([^"]+)"',page)
assert len(links)==31 and len(set(links))==31
print("Profile center: 3 platforms, 31 project cards, 16 additional READMEs, 31 unique GitHub links")

# LinkedIn recruiter project center: prominent navigation, copy-ready entries and
# explicit disclosure that this site does not write to the member's account.
showcase=text("linkedin-projects.html")
setup=text("linkedin-setup.html")
assert showcase.count('class="project-card"')==51
assert showcase.count('data-tier="additional"')==36
assert 'id="scope"' in showcase
assert showcase.count('<li data-search=')==51
assert showcase.count('class="primary-link"')==51
assert 'id="search"' in showcase and 'id="project-grid"' in showcase
assert 'data-filter="All"' in showcase
assert 'href="linkedin-setup.html"' in showcase
assert 'href="assets/luxury-theme.css"' in showcase
assert '<strong>51</strong>' in showcase
assert setup.count('class="project"')==31
assert setup.count('data-copy="project-')==31
assert 'navigator.clipboard.writeText' in setup
assert 'does not sign in to or update LinkedIn' in setup
assert 'Activity → Posts' in setup
assert 'href="assets/luxury-theme.css"' in setup
for f in ("index.html","work.html","README.md"):
    assert "linkedin-setup.html" in text(f), f
assert "## 13. Ready-to-publish LinkedIn portfolio launch post" in text("docs/LINKEDIN_PROFILE_PROJECTS_MASTER.md")

# Independently published public-benefit AI source pages must remain discoverable.
new_repos=(
    "AI-Disaster-Response-Public-Safety", "AI-Flood-Disaster-Early-Warning",
    "Emergency-Services-Copilot", "Trusted-Public-Health-Assistant",
    "AI-Road-Safety-Intelligence", "Scam-Phishing-Awareness",
    "Multilingual-Civic-Services-Navigator",
    "Missing-Person-Information-Coordination",
    "AI-Air-Quality-Monitor", "AI-Accessibility-Civic-Reporting"
)
for repo_name in new_repos:
    repo_url=f"https://github.com/harshakavali81-collab/{repo_name}"
    assert repo_url in showcase
    assert repo_url in text("index.html")
    assert repo_url in text("public-benefit-ai-projects.html")
assert text("public-benefit-ai-projects.html").count('<article class="card" id=')==10
print("LinkedIn showcase: 51 cards (15 featured, 36 additional); LinkedIn setup: 31 existing copy-ready entries; 51 GitHub sources verified")
