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
import json

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

    # Evidence ledger integrity: no missing sources, duplicated records or
    # broken connections between the machine-readable register and case pages.
    ledger = ROOT / "data" / "project-evidence.json"
    required_slugs = {"ecommerce", "transactionshield", "demandpilot", "evidencedesk", "zomato", "supportlens", "streamwatch"}
    if not ledger.exists():
        problems.append("Missing data/project-evidence.json")
    else:
        try:
            source = json.loads(ledger.read_text(encoding="utf-8"))
            entries = source["entries"]
            if not isinstance(entries, list) or len(entries) != 7:
                problems.append("Evidence register must contain exactly seven curated projects")
            seen: set[str] = set()
            keys = ("slug", "title", "question", "test", "metric", "metricLabel",
                    "metricDetail", "tradeoff", "limitations", "reviewNext",
                    "source", "evidence", "casePage", "claimLevel", "architecture")
            for item in entries:
                if not isinstance(item, dict):
                    problems.append("Evidence register contains a non-object project")
                    continue
                slug = item.get("slug", "")
                if slug in seen:
                    problems.append(f"Repeated evidence slug: {slug}")
                seen.add(slug)
                for key in keys:
                    val = item.get(key)
                    if not val or (isinstance(val, str) and not val.strip()):
                        problems.append(f"Evidence project {slug}: missing {key}")
                case_path = ROOT / str(item.get("casePage", ""))
                if not case_path.is_file() or case_path.resolve() not in pages:
                    problems.append(f"Evidence project {slug}: case study path unavailable")
                for key in ("source", "evidence"):
                    url = str(item.get(key, ""))
                    if not url.startswith("https://github.com/harshakavali81-collab/"):
                        problems.append(f"Evidence project {slug}: invalid {key} URL")
                if not isinstance(item.get("architecture"), list) or len(item.get("architecture", [])) < 3:
                    problems.append(f"Evidence project {slug}: architecture should have at least three steps")
            if seen != required_slugs:
                problems.append(f"Evidence slugs differ from seven curated case studies: {sorted(seen)}")
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            problems.append(f"Malformed evidence ledger: {exc}")
    notebook = (ROOT / "engineering.html").resolve()
    if notebook not in pages:
        problems.append("Missing Engineering Notebook page")
    else:
        for adr in ("adr-ecommerce", "adr-fraud", "adr-forecast", "adr-rag", "adr-bi"):
            if adr not in pages[notebook].ids:
                problems.append(f"Engineering Notebook missing #{adr}")

    luxury_css = ROOT / "assets" / "luxury-theme.css"
    if not luxury_css.exists():
        problems.append("Missing portfolio luxury theme stylesheet")
    else:
        theme_source = luxury_css.read_text(encoding="utf-8")
        for required in ("--obsidian:#080808", "--metal:linear-gradient", "prefers-reduced-motion", "forced-colors:active"):
            if required not in theme_source:
                problems.append("Incomplete premium theme: " + required)
    for page, scan in pages.items():
        required_href = "../assets/luxury-theme.css" if "cases" in page.relative_to(ROOT).parts else "assets/luxury-theme.css"
        if not any(url == required_href for attr, url in scan.links if attr == "href"):
            problems.append(f"{page.relative_to(ROOT)}: champagne-gold/obsidian stylesheet missing")
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
