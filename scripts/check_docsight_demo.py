#!/usr/bin/env python3
"""Offline syntax and privacy-contract checks for DocSight's standalone browser demo."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


class DemoScan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.scripts, self.in_script, self.remote = [], [], False, []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.append(attributes["id"])
        if tag == "script":
            self.in_script = True
            if attributes.get("src"):
                self.remote.append(attributes["src"])

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_script = False

    def handle_data(self, data):
        if self.in_script:
            self.scripts.append(data)


def main():
    path = ROOT / "docsight-demo.html"
    assert path.exists(), "Demo file missing"
    scanner = DemoScan()
    scanner.feed(path.read_text(encoding="utf-8"))
    mandatory = {"source", "sample", "file", "clear", "analyze", "results", "bars", "summaries", "export"}
    assert mandatory.issubset(scanner.ids)
    assert len(scanner.ids) == len(set(scanner.ids)), "Duplicate element IDs"
    assert not scanner.remote, "Remote scripts are forbidden in offline demo"
    script = "\n".join(scanner.scripts)
    for unsafe in ("fetch(", "XMLHttpRequest", "sendBeacon(", "WebSocket(", "localStorage", "sessionStorage"):
        assert unsafe not in script, f"Unexpected network or storage API: {unsafe}"
    assert "textContent" in script and "createElement" in script
    parsed = subprocess.run(["node", "--check"], input=script, text=True, capture_output=True)
    assert parsed.returncode == 0, parsed.stderr
    for name in ("index.html", "work.html", "cases/docsight.html", "README.md"):
        assert "docsight-demo.html" in (ROOT / name).read_text(encoding="utf-8"), name
    print("DocSight offline browser demo passed structural, navigation and JavaScript syntax checks.")


if __name__ == "__main__":
    main()
