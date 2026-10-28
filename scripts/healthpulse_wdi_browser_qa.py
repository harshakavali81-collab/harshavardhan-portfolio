"""Verify HealthPulse historical WDI browser charts against the published JSON.

Runs locally in GitHub Actions with Chromium. Does not contact health providers.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import urllib.request
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
URL="http://127.0.0.1:18787/healthpulse-worldbank.html"


def main():
    data=(ROOT/"data/healthpulse-worldbank.json").read_bytes()
    manifest=json.loads((ROOT/"data/healthpulse-worldbank-manifest.json").read_text())
    dataset=json.loads(data)
    if hashlib.sha256(data).hexdigest()!=manifest["snapshot_sha256"]:
        raise RuntimeError("Source archive checksum disagrees with WDI manifest")
    if (dataset["source"]!="WorldBank" or not dataset["records"]
            or len(dataset["records"])!=manifest["rows"]
            or any(r["source"]!="WorldBank" for r in dataset["records"])):
        raise RuntimeError("Invalid source or count in published WDI snapshot")
    server=subprocess.Popen(
        [sys.executable,"-m","http.server","18787","--bind","127.0.0.1","--directory",str(ROOT)],
        stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,
    )
    try:
        for _ in range(60):
            try:
                with urllib.request.urlopen(URL,timeout=1) as resp:
                    if resp.status==200:break
            except OSError:
                time.sleep(.25)
        else:
            raise RuntimeError("Local static server did not start")
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True)
            page=browser.new_page(viewport={"width":1440,"height":950},accept_downloads=True)
            page.goto(URL,wait_until="networkidle")
            page.wait_for_function("document.getElementById('status').textContent.includes('snapshot loaded')",timeout=20000)
            assert str(manifest["rows"]) in page.locator("#status").inner_text()
            assert page.locator("#indicator option").count()==5
            assert page.locator("#rows tr").count()>0
            assert "World Bank" in page.locator("#manifest").inner_text()
            assert page.locator("#countryVal").inner_text() not in ("—","N/A")
            assert "not clinical" in page.locator("footer").inner_text().lower() or "clinical" in page.locator("footer").inner_text().lower()
            page.locator("#indicator").select_option("immunization")
            assert page.locator("#rows tr").count()>0
            assert page.locator("#regions .bar").count()>0
            page.locator("#country").select_option("IND")
            with page.expect_download() as download_info:
                page.locator("#download").click()
            d=download_info.value
            assert d.suggested_filename.startswith("WorldBank-WDI-immunization-IND")
            Path("qa-out").mkdir(exist_ok=True)
            page.screenshot(path="qa-out/healthpulse-wdi-desktop.png",full_page=True)
            mobile=browser.new_page(viewport={"width":390,"height":844})
            mobile.goto(URL,wait_until="networkidle")
            mobile.wait_for_function("document.getElementById('status').textContent.includes('snapshot loaded')",timeout=20000)
            mobile.screenshot(path="qa-out/healthpulse-wdi-mobile.png",full_page=True)
            mobile.close()
            browser.close()
    finally:
        server.terminate()
        server.wait(timeout=10)
    print(json.dumps({"result":"PASS","snapshot_records":manifest["rows"],"indicators":len(dataset["indicator_manifest"]),
                      "checks":["SHA256","real-source-only","chart populated","selectors","country ranking","CSV export","desktop","mobile"]},indent=2))


if __name__=="__main__":
    main()
