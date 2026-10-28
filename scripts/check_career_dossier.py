"""Static verification of the public recruiter dossier and gold-only career theme."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class LinkAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
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
    assert "No professional awards" in html
    assert "Street Cause Hyderabad" in html and "self-reported" in html
    assert "referee" in html.lower(), "Reference privacy statement missing"
    assert "KH GOLD-ONLY CAREER RELEASE" in css
    assert "body.kh-dossier" in css and "color-scheme:dark" in css
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    profile = (ROOT / "profile.html").read_text(encoding="utf-8")
    assert 'id="career-12"' in home and "career-portfolio.html#twelve-elements" in home
    assert 'id="professional-links"' in profile and 'id="beyond"' in profile
    assert home.count('class="bh-project-source" href=') == 31
    # Canonical two-color release: visually support ONLY #080808 and #d4af37.
    import re
    marker = "KH FINAL / TWO-COLOR BLACK + GOLD"
    assert marker in css, "Owner-selected pure black/gold theme missing"
    final_css = css[css.rfind(marker):]
    palette = set(re.findall(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])", final_css.lower()))
    assert palette == {"#080808", "#d4af37"}, f"Unexpected final theme colors: {palette}"
    assert css.rfind(marker) > css.rfind("KH SOFT GOLD"), "Older styling overrides the two-color theme"
    for destination in ("index.html", "contact.html", "recruiter.html",
                        "profile.html", "career-portfolio.html", "resumes.html"):
        markup = (ROOT / destination).read_text(encoding="utf-8")
        for required in ("tel:+918008273318", "github.com/harshakavali81-collab"):
            assert required in markup, f"{destination}: missing recruiter contact {required}"
    for pdf in ("Kavali_Harshavardhan_Data_Analyst_Resume.pdf",
                "Kavali_Harshavardhan_AIML_DataAnalyst_Resume.pdf"):
        assert (ROOT / "assets" / pdf).exists(), f"Missing resume PDF: {pdf}"
    # Recruiter-focused job-portfolio requirements are linked, not invented.
    readiness = (ROOT / "portfolio-readiness.html").read_text(encoding="utf-8")
    assert readiness.count('class="kh-ready-section"') == 5
    assert readiness.count('class="kh-ready-status"') == 32
    assert readiness.count('class="kh-ready-expand"') == 7
    assert "36 technical checks for portfolio projects." in readiness
    assert "Complete project case-study template — 19 review fields" in readiness
    assert "32 practical requirements" in readiness
    assert "Verify repositories" in readiness and "Security review" in readiness
    assert "not proof of a working production deployment" in readiness
    for doc in ("index.html", "profile.html", "career-portfolio.html", "recruiter.html"):
        assert 'href="portfolio-readiness.html"' in (ROOT / doc).read_text(encoding="utf-8"), doc
    # Regression for the white facts bar visible in the user's screenshot.
    assert "KH SCREEN REFINEMENTS" in css
    assert "body.bh-body .bh-stats{" in css
    after_fix = css[css.index("KH SCREEN REFINEMENTS"):]
    assert "background:#080808!important" in after_fix
    assert "font-size:clamp(1.4rem,2.8vw,2.1rem)!important" in after_fix
    contact_page = (ROOT / "contact.html").read_text(encoding="utf-8")
    assert "view=cm&fs=1" in contact_page
    assert 'id="open-mail-app"' in contact_page
    assert 'id="open-gmail"' in contact_page and 'id="copy-message"' in contact_page
    certificates = (ROOT / "certificates.html").read_text(encoding="utf-8")
    assert certificates.count('class="kh-proof-card"') == 7
    for label in ("AWS Academy Cloud Developing","AWS Academy Data Engineering",
                  "AI–ML Virtual Internship","Android Developer Virtual Internship",
                  "Intelligent Automation Virtual Internship","Entrepreneurship Orientation Program"):
        assert label in certificates, f"Missing uploaded qualification: {label}"
    assert "tfTqbAM0" in certificates and "GqcOmj3t" in certificates
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    # Six owner-selected featured projects replace the previous curated six.
    selected_names = (
        "Multilingual-Project",
        "Zomato-Insights-Dashboard-project-with-PowerBI",
        "Women-Saftey-Device-by-Using-GPS-and-GSM-",
        "A-Multimodal-AI-Customer-Support-Copilot",
        "DemandPilot-AI-Enterprise-AI-Demand-Forecasting-Inventory-Optimization-Platform",
        "AirAware-AI-Air-Pollution-Heat-Risk-Intelligence",
    )
    from html.parser import HTMLParser
    class FeaturedParser(HTMLParser):
        def __init__(self):
            super().__init__(); self.in_feature = False; self.depth = 0; self.hrefs = []
        def handle_starttag(self, tag, attrs):
            attr = dict(attrs)
            if tag == "article" and attr.get("class") == "bh-feature":
                self.in_feature = True; self.depth = 0
            if self.in_feature:
                if tag == "div": self.depth += 1
                if tag == "a" and "href" in attr: self.hrefs.append(attr["href"])
        def handle_endtag(self, tag):
            if self.in_feature and tag == "div": self.depth = max(0,self.depth - 1)
            if self.in_feature and tag == "article": self.in_feature = False
    assert home.count('class="bh-feature"') == 6
    assert home.count('class="kh-resume-project"') == 0, "No duplicate resume project cards"
    featured = FeaturedParser()
    featured.feed(home)
    for name in selected_names:
        assert f"https://github.com/harshakavali81-collab/{name}" in featured.hrefs, f"Featured link missing: {name}"
    for slug in ("multilingual","zomato","women-safety","copilot","demandpilot","airaware"):
        href = f"cases/{slug}.html"
        assert href in featured.hrefs, f"Case link missing: {slug}"
        assert (ROOT / href).exists(), f"Missing case study: {href}"
    assert home.count('class="kh-cert-highlight-grid"') == 1
    for phrase in ("Multilingual Indian Language Knowledge Base", "Women Safety Device",
                   "Multimodal AI Customer Support Copilot", "AirAware AI",
                   'id="resume-skills"', 'id="academic-history"', 'id="hobbies"'):
        assert phrase in home, phrase
    assert "assets/resume-evidence.css?v=20261028-edu2" in home
    assert "assets/kh-ivory-accent.css?v=20261028-featured6" in home
    accents = (ROOT / "assets/kh-ivory-accent.css").read_text(encoding="utf-8")
    visible_palette = set(re.findall(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])", accents.lower()))
    assert visible_palette == {"#080808","#d4af37","#f0e6d2"}, visible_palette
    theme = (ROOT / "assets/resume-evidence.css").read_text(encoding="utf-8")
    palette = set(re.findall(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])", theme.lower()))
    assert palette == {"#080808","#d4af37"}
    # 2026 official academic results: all visible recruiter pages use the
    # supplied B.Tech consolidated sheet, AP Intermediate memo and SSC GPA.
    for page_name in ("index.html", "profile.html", "certificates.html",
                      "resume.html", "data-analyst-resume.html", "career-portfolio.html",
                      "recruiter.html", "hiring.html", "job-platforms.html",
                      "linkedin-setup.html"):
        body = (ROOT / page_name).read_text(encoding="utf-8")
        assert "7.02" not in body, f"Stale B.Tech CGPA in {page_name}"
        assert "7.36" not in body, f"Stale B.Tech CGPA in {page_name}"
    for page_name in ("index.html", "profile.html", "certificates.html",
                      "resume.html", "data-analyst-resume.html", "recruiter.html",
                      "hiring.html"):
        body = (ROOT / page_name).read_text(encoding="utf-8")
        assert "7.03" in body, f"Official B.Tech result missing in {page_name}"
        assert "864/1000" in body, f"Official Intermediate result missing in {page_name}"
        assert "9.2 GPA" in body or "GPA 9.2" in body, f"SSC GPA missing in {page_name}"
    for resume in ("Kavali_Harshavardhan_Data_Analyst_Resume.pdf",
                   "Kavali_Harshavardhan_AIML_DataAnalyst_Resume.pdf"):
        raw = (ROOT / "assets" / resume).read_bytes()
        assert raw.startswith(b"%PDF-1.4"), resume
        assert b"7.03/10" in raw and b"864/1000" in raw and b"GPA 9.2/10" in raw
        i = raw.rfind(b"startxref")
        assert i > 0, resume
        off = int(raw[i+len(b"startxref"):].split()[0])
        assert raw[off:off+4] == b"xref", f"Invalid PDF cross-reference: {resume}"
    flagship = (ROOT / "flagship-projects.html").read_text(encoding="utf-8")
    assert flagship.count('class="kh-flagship"') == 3
    assert flagship.count('class="kh-spec"') == 57, "Each of 3 flagship projects must show 19 case-study requirements"
    for term in ("Multilingual Indian Language Knowledge Base", "Zomato Insights Dashboard",
                 "DemandPilot", "Synthetic", "Reproducibility"):
        assert term.lower() in flagship.lower(), term
    assert 'href="flagship-projects.html"' in (ROOT / "index.html").read_text(encoding="utf-8")
    assert "Registration numbers, birth date" in (ROOT / "certificates.html").read_text(encoding="utf-8")
    guide = (ROOT / "portfolio-readiness.html").read_text(encoding="utf-8")
    assert 'id="eight-essentials"' in guide and 'id="role-paths"' in guide
    assert guide.count('class="kh-ready-essentials"') == 1
    assert (ROOT / "docs/GITHUB_PROFILE_README.md").is_file()
    # End strict theme/contact checks.
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
