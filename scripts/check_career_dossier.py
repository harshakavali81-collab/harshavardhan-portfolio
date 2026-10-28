"""Static verification of the public recruiter dossier and gold-only career theme."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class LinkAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag in ("a", "link", "img", "script"):
            value = a.get("href") or a.get("src")
            if value:
                self.links.append(value)

def check():
    page = ROOT / "career-portfolio.html"
    assert page.exists(), "Career portfolio not found"
    html = page.read_text(encoding="utf-8")
    css = (ROOT / "assets/portfolio-upgrade.css").read_text(encoding="utf-8")
    audit = LinkAudit()
    audit.feed(html)
    assert len(audit.ids) == len(set(audit.ids))
    for section in ("main", "overview", "selected", "credentials", "recommendations", "standards", "contact"):
        assert section in audit.ids, f"Missing section: {section}"
    assert html.count('class="kh-case"') == 5, "Expected five curated STAR case studies"
    assert '31 GitHub repository entries' in html or '31 GitHub' in html or '31 repositories' in html
    for term in ("Python", "Power BI", "LinkedIn", "resumes.html", "source", "synthetic"):
        assert term.lower() in html.lower(), f"Missing career evidence: {term}"
    for link in audit.links:
        parsed = urlsplit(link)
        if parsed.scheme or link.startswith("//") or link.startswith("mailto:") or link.startswith("tel:"):
            continue
        rel = unquote(parsed.path)
        if rel:
            target = (page.parent / rel)
            assert target.exists(), f"Missing local link: {link}"
        if parsed.fragment and not rel:
            assert unquote(parsed.fragment) in audit.ids, f"Bad in-page anchor: {link}"
    assert "body.kh-dossier" in css
    assert "#080808" in css and "#d4af70" in css
    for p in ["index.html", "profile.html", "linkedin-setup.html", "linkedin-projects.html", "work.html", "contact.html"]:
        markup = (ROOT / p).read_text(encoding="utf-8")
        assert "portfolio-upgrade.css" in markup, f"Theme missing in {p}"
    assert "career-portfolio.html" in (ROOT / "index.html").read_text(encoding="utf-8")
    assert "career-portfolio.html" in (ROOT / "linkedin-setup.html").read_text(encoding="utf-8")
    print("PASS: career dossier structure, local links, 5 case studies, gold theme and LinkedIn handoff.")

if __name__ == "__main__":
    check()
