#!/usr/bin/env python3
"""Regression checks for KH's premium-black theme and recruiter navigation.

Structural checks only. Browser rendering, deployment, and outside links are
verified separately in the portfolio's live QA workflow.
"""
from pathlib import Path
from html.parser import HTMLParser
import re

ROOT = Path(__file__).resolve().parents[1]

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def check() -> None:
    home = read("index.html")
    css = read("assets/kedhar-inspired.css")
    interior = read("assets/kedhar-interior.css")
    script = read("assets/kedhar-inspired.js")
    assert "KH BLACK SIGNATURE — PREMIUM OBSIDIAN & CHAMPAGNE" in css
    assert "KH BLACK SIGNATURE — CORE CAREER PAGES" in interior
    assert "background-color:#080808!important" in css
    assert "background:#080808!important" in interior
    assert "prefers-reduced-motion:reduce" in css
    assert "prefers-reduced-motion:reduce" in interior
    assert 'class="bh-body"' in home
    # Black Label must be the final stylesheet, even if legacy links remain.
    assert "kh-obsidian-final.css" in home
    assert home.rfind("kh-obsidian-final.css") > home.rfind("light-gold-final.css")
    assert home.rfind("kh-ivory-accent.css") > home.rfind("kh-obsidian-final.css")
    assert '@import url("./kh-obsidian-final.css")' in read("assets/light-gold-final.css")
    assert "KH / BLACK LABEL" in read("assets/kh-obsidian-final.css")
    assert '<meta name="theme-color" content="#090909">' in home
    assert 'href="assets/kedhar-inspired.css"' in home
    assert 'id="bh-search"' in home and 'id="bh-category"' in home
    assert "requestAnimationFrame" in script
    assert "aria-expanded" in script
    assert 'id="recruiter-desk"' in home
    assert home.count('class="bh-resource"') == 4
    assert home.count('class="bh-feature"') == 6
    assert home.count('class="bh-project-extras"') == 35
    assert home.count('class="bh-project-demo"') == 9
    assert home.count('class="bh-demo-card"') == 6
    assert 'id="demos"' in home
    assert 'href="resumes.html"' in home
    assert 'href="recruiter.html"' in home
    assert 'href="proof-map.html"' in home
    assert 'href="hiring.html"' in home
    assert 'href="job-platforms.html"' in home
    assert 'href="linkedin-setup.html"' in home
    links = re.findall(r'class="bh-project-source" href="([^"]+)"', home)
    assert len(links) == 51, len(links)
    assert len(set(links)) == 51
    assert all(link.startswith("https://github.com/harshakavali81-collab/") for link in links)
    career = ("profile.html", "linkedin-projects.html", "job-platforms.html",
              "linkedin-setup.html", "work.html", "resumes.html", "contact.html",
              "recruiter.html", "hiring.html", "engineering.html", "evidence.html",
              "proof-map.html", "quality.html", "interview.html")
    for name in career:
        page = read(name)
        assert 'class="bh-interior"' in page, f"Missing themed body: {name}"
        assert 'href="assets/kedhar-interior.css"' in page, f"Missing theme link: {name}"
        assert "kh-ivory-accent.css" in page, f"Missing final seven-color theme: {name}"
    case_paths = sorted((ROOT / "cases").glob("*.html"))
    assert len(case_paths) >= 15, len(case_paths)
    for path in case_paths:
        page = path.read_text(encoding="utf-8")
        assert 'class="bh-interior' in page, f"Missing themed case: {path.name}"
        assert 'href="../assets/kedhar-interior.css"' in page
        assert "kh-ivory-accent.css" in page, f"Missing final seven-color theme: {path.name}"
    assert read("linkedin-setup.html").count('class="project"') == 31
    print(f"Premium black verified structurally: 51 unique projects, 6 featured cases, "
          f"4 recruiter resources, {len(career)} career pages, {len(case_paths)} case pages.")
    print("Live browser contrast, link availability, and deployed CSS require independent checks.")

if __name__ == "__main__":
    check()
