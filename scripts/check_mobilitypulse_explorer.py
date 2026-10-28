#!/usr/bin/env python3
"""Validate the standalone MobilityPulse synthetic demo without a browser."""
from pathlib import Path
from html.parser import HTMLParser
from tempfile import TemporaryDirectory
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set()
        self.tabs={}
        self.images=[]
        self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get("id"): self.ids.add(a["id"])
        if tag=="button" and a.get("role")=="tab":
            self.tabs[a.get("id")]=a.get("aria-controls")
        if tag=="img": self.images.append(a)
        if tag=="a": self.links.append(a.get("href",""))

def main():
    html=(ROOT/"mobilitypulse-explorer.html").read_text(encoding="utf8")
    page=Page();page.feed(html)
    for name in ("overview","routes","stops","reliability","accessibility","feeds"):
        assert page.tabs.get("t-"+name)=="p-"+name
        assert "p-"+name in page.ids
    assert len(page.tabs)==6
    assert "synthetic" in html.lower() and "not live" in html.lower()
    assert "wheelchair" in html.lower()
    assert "cases/mobilitypulse.html" in page.links
    assert all(img.get("alt") for img in page.images)
    for n in range(1,11):
        assert list((ROOT/"assets/mobilitypulse").glob(f"{n:02}-*.svg"))
    js=re.findall(r"<script[^>]*>(.*?)</script>",html,flags=re.S|re.I)
    assert len(js)==1
    with TemporaryDirectory() as td:
        f=Path(td)/"main.js";f.write_text(js[0],encoding="utf8")
        subprocess.run(["node","--check",str(f)],check=True)
    print("PASS: tab targets, disclosures, imagery and valid JavaScript")
if __name__=="__main__":
    main()
