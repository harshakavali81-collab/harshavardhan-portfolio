#!/usr/bin/env python3
"""Static regression checks for recruiter content and reliable contact options."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def check():
    profile = read("profile.html")
    contact = read("contact.html")
    homepage = read("index.html")
    theme = read("assets/luxury-theme.css")
    for part in ('id="main"', 'href="#main"', 'id="career-goals"',
                 'Career objective', 'Roles of interest', 'Why consider me',
                 'Availability &amp; contact', 'hiring.html', 'proof-map.html',
                 'resumes.html'):
        assert part in profile, "Missing profile element: " + part
    for part in ('mailto:kavaliharshavardhan98@gmail.com', 'id="copy-message"',
                 'id="manual-copy"', 'navigator.clipboard.writeText',
                 'window.open(gmailUrl(message)', 'copy-message").addEventListener'):
        assert part in contact, "Missing contact fallback: " + part
    assert 'id="mail-form"' in contact
    for part in ('KH ATELIER', '.kh-hobby-card.kh-book', '.kh-recruiter-ribbon',
                 '.kh-profile-grid', '@media print', 'prefers-reduced-motion'):
        assert part in theme, "Missing theme rule: " + part
    for page in (homepage, profile, contact):
        assert 'assets/luxury-theme.css' in page, "Missing shared stylesheet"
    print("Career profile, visual theme and email alternatives: checks passed")

if __name__ == "__main__":
    check()
