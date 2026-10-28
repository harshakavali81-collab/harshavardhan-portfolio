#!/usr/bin/env python3
"""Validate this static GitHub Pages portfolio without network access.

Checks internal href/src targets, fragments, duplicate IDs and mandatory case-study
sections. External URLs and browser rendering are intentionally outside its scope.
"""
from __future__ import annotations
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
IGNORED_PREFIXES = ("mailto:", "tel:", "data:", "javascript:")
CASE_IDS = ("overview", "problem", "process", "solution", "results", "reflection")


class Scan(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.images_without_alt: int = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = dict(attrs)
        if d.get("id"):
            self.ids.append(d["id"] or "")
        if tag == "img" and d.get("alt") is None:
            self.images_without_alt += 1
        for attr in ("href", "src"):
            if d.get(attr):
                self.links.append((attr, d[attr] or ""))


def main() -> int:
    problems: list[str] = []
    files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "cases").glob("*.html"))
    pages: dict[Path, Scan] = {}
    for page in files:
        if ".git" in page.parts:
            continue
        scan = Scan()
        scan.feed(page.read_text(encoding="utf-8"))
        pages[page.resolve()] = scan
        duplicates = [item for item, count in Counter(scan.ids).items() if count > 1]
        if duplicates:
            problems.append(f"{page.relative_to(ROOT)}: duplicate IDs: {duplicates}")
        if scan.images_without_alt:
            problems.append(f"{page.relative_to(ROOT)}: {scan.images_without_alt} images missing alt")

    if not (ROOT / "index.html").exists():
        problems.append("Missing index.html")
    for slug in ("ecommerce", "transactionshield", "demandpilot", "evidencedesk", "zomato"):
        page = (ROOT / "cases" / f"{slug}.html").resolve()
        if page not in pages:
            problems.append(f"Missing case page cases/{slug}.html")
            continue
        for section in CASE_IDS:
            if section not in pages[page].ids:
                problems.append(f"{page.relative_to(ROOT)} missing section #{section}")

    for page, scan in pages.items():
        for _, url in scan.links:
            if url.startswith(IGNORED_PREFIXES) or url.startswith("//"):
                continue
            parsed = urlsplit(url)
            if parsed.scheme in ("http", "https"):
                continue  # External URLs need online audit; not verified here.
            if parsed.scheme:
                continue
            fragment = unquote(parsed.fragment)
            local = unquote(parsed.path)
            if local.startswith("/"):
                target = ROOT / local.lstrip("/")
            elif local:
                target = page.parent / local
            else:
                target = page
            target = target.resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                problems.append(f"{page.relative_to(ROOT)}: link leaves repository: {url}")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                problems.append(f"{page.relative_to(ROOT)}: missing linked file {url}")
                continue
            if fragment and target.suffix.lower() == ".html":
                linked = pages.get(target)
                if linked and fragment not in linked.ids:
                    problems.append(f"{page.relative_to(ROOT)}: missing fragment {url}")

    if problems:
        print("SITE AUDIT FAILED")
        for msg in problems:
            print("-", msg)
        return 1
    print(f"Site audit passed: {len(pages)} HTML pages checked, internal links/assets verified.")
    print("External website availability and live browser load time require separate checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
