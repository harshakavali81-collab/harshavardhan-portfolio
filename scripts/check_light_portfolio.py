#!/usr/bin/env python3
"""Offline regression checks for the soft-gold design and all GitHub project links."""
from pathlib import Path
from html.parser import HTMLParser
import re

ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


class Projects(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.projects = []
        self.source_urls = []
        self.art = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set((attrs.get("class") or "").split())
        if tag == "article" and "project-card" in classes:
            self.projects.append((attrs.get("data-tier"), attrs.get("data-category")))
        if tag == "a" and "primary-link" in classes:
            self.source_urls.append(attrs.get("href"))
        if tag == "div" and "project-art" in classes:
            self.art += 1


def main() -> None:
    css = read("assets/luxury-theme.css")
    assert "LIGHT GOLD EDITION 2026 — refined-light-theme" in css
    assert "background-color:#faf9f6!important" in css
    assert "color:#27313a!important" in css
    assert "background:#ffffff!important" in css
    assert "--accent:#947448" in css
    assert ".portfolio-gallery-promo" in css
    assert ".project-card .project-art" in css
    assert "@media(max-width:750px)" in css
    assert "@media print" in css

    showcase = read("linkedin-projects.html")
    page = Projects()
    page.feed(showcase)
    assert len(page.projects) == 31, f"project count: {len(page.projects)}"
    assert len(page.source_urls) == 31, "every card must link to GitHub"
    assert len(set(page.source_urls)) == 31, "no duplicate repository links"
    assert all(url and url.startswith(
        "https://github.com/harshakavali81-collab/") for url in page.source_urls)
    assert sum(tier == "featured" for tier, _ in page.projects) == 15
    assert sum(tier == "additional" for tier, _ in page.projects) == 16
    assert all(category for _, category in page.projects)
    assert page.art == 31, f"art thumbnails: {page.art}"
    assert 'id="search"' in showcase
    assert 'id="scope"' in showcase
    assert 'id="project-grid"' in showcase

    job = read("job-platforms.html")
    job_sources = re.findall(r'class="btn source" href="([^"]+)"', job)
    assert len(job_sources) == 31
    assert set(page.source_urls) == set(job_sources), "project pages are out of sync"

    home = read("index.html")
    assert 'class="portfolio-gallery-promo"' in home
    assert 'href="linkedin-projects.html"' in home
    assert "View all 31 projects" in home
    assert 'href="linkedin-setup.html"' in home

    setup = read("linkedin-setup.html")
    assert setup.count('class="project"') == 31
    assert setup.count('data-copy="project-') == 31
    assert 'does not sign in to or update LinkedIn' in setup
    assert "navigator.clipboard.writeText" in setup
    assert 'href="assets/luxury-theme.css"' in setup

    master = read("docs/LINKEDIN_PROFILE_PROJECTS_MASTER.md")
    assert "## 16. Copy-ready additional projects" in master
    assert len(re.findall(r"^### [0-9]+\.", master, flags=re.M)) == 31

    readme = read("README.md")
    assert "Soft Gold & Ivory Visual Identity" in readme
    print("Soft-gold theme and complete 31-source gallery: static regression checks passed")
    print("31 unique GitHub URLs match job-platform catalog; LinkedIn copy and mobile CSS present")
    print("Public hosting and visual/browser render still require separate external verification")


if __name__ == "__main__":
    main()
