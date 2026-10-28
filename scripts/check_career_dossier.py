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
    for section in ("main", "overview", "pillars", "selected", "credentials", "recommendations", "standards", "contact"):
        assert section in audit.ids, f"Missing section: {section}"
    assert html.count('class="kh-case"') == 5, "Expected five curated STAR case studies"

    assert html.count('class="kh-pillar"') == 5, "Expected five recruiter-facing portfolio pillars"
    # Twelve-element career extension: do not silently drop any requested element.
    assert "twelve-elements" in audit.ids, "Missing the 12-element career section"
    assert html.count('class="kh-element"') == 12, "Career dossier must contain all twelve elements"
    for heading in (
        "Career summary", "Mission statement", "Brief biography",
        "Role-specific resumes", "Marketable skills",
        "Documented accomplishments", "Work samples and case studies",
        "Awards and recognition", "Degrees and certifications",
        "Professional development", "Volunteer and community service",
        "References and testimonials",
    ):
        assert heading in html, f"Missing career element: {heading}"
    for url_fragment in ("github.com/harshakavali81-collab", "linkedin.com/in/kavali-harshavardhan", "job-platforms.html", "profile.html#beyond"):
        assert url_fragment in html, f"Missing professional link: {url_fragment}"
    assert "No independent professional awards" in html
    assert "No specific volunteering" in html
    assert "referee" in html.lower(), "Reference privacy statement missing"
    assert "KH GOLD-ONLY CAREER RELEASE" in css
    assert "body.kh-dossier" in css and "color-scheme:dark" in css
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    profile = (ROOT / "profile.html").read_text(encoding="utf-8")
    assert 'id="career-12"' in home and "career-portfolio.html#twelve-elements" in home
    assert 'id="professional-links"' in profile and 'id="beyond"' in profile
    assert home.count('class="bh-project-source" href=') == 31
    # Twelve-element career extension: END

    for term in ("Problem.", "My approach.", "Outcome and evidence.", "What I learned."):
        assert html.count(term) >= 5, f"Five case studies must include {term}"
    for proof in ("evidence.html", "quality.html", "GitHub Actions"):
        assert proof in html, f"Missing transparent evidence routing: {proof}"
    assert "kh-proof-guidance" in html
    assert "portfolio-upgrade.css" in html
    assert "<meta name=\"viewport\"" in html
    assert "mailto:" in html
    assert "linkedin-projects.html" in html and "resumes.html" in html

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

    for rule in ("KH FINAL METALLIC FOIL CASCADE BRIDGE", "--kh-foil:linear-gradient",
                 "Cormorant+Garamond", "Cinzel", ".kh-pillars", "@media(max-width:620px)",
                 "prefers-reduced-motion:reduce", "forced-colors:active"):
        assert rule in css, f"Missing responsive or accessible metallic gold theme feature: {rule}"

    for p in ["index.html", "profile.html", "linkedin-setup.html", "linkedin-projects.html", "work.html", "contact.html"]:
        markup = (ROOT / p).read_text(encoding="utf-8")
        assert "portfolio-upgrade.css" in markup, f"Theme missing in {p}"
    assert "career-portfolio.html" in (ROOT / "index.html").read_text(encoding="utf-8")
    assert "career-portfolio.html" in (ROOT / "linkedin-setup.html").read_text(encoding="utf-8")
    print("PASS: career dossier, five recruiter pillars, five evidence-led case studies, links, metallic-gold screen theme and LinkedIn handoff.")

if __name__ == "__main__":
    check()
