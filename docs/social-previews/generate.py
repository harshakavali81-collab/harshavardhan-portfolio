"""Render original typographic GitHub social cards; not application screenshots.

Requires Inkscape on PATH. Run: python generate.py
"""
from pathlib import Path
import json
import textwrap
import html
import subprocess

ROOT = Path(__file__).resolve().parent

def render(item):
    title = item['title']
    lines = textwrap.wrap(title, width=36, break_long_words=False)
    size = 53 if len(lines) <= 3 else 45
    line_height = 66 if len(lines) <= 3 else 56
    first = 252 if len(lines) <= 3 else 222
    texts = ''.join(f'<text x="76" y="{first + i * line_height}" font-size="{size}" font-weight="700">{html.escape(line)}</text>' for i, line in enumerate(lines))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640">
<title>{html.escape(title)} — portfolio project</title>
<desc>Original typographic social preview, not a screenshot or performance claim.</desc>
<rect width="1280" height="640" fill="#090909"/>
<rect x="28" y="28" width="1224" height="584" rx="20" fill="#141414" stroke="#3B3324" stroke-width="2"/>
<path d="M76 146H1204" stroke="#3B3324" stroke-width="2"/>
<g font-family="DejaVu Sans, sans-serif" fill="#F5F0E6">
<text x="76" y="99" font-size="23" letter-spacing="4" fill="#D4AF65">KAVALI HARSHAVARDHAN</text>
<text x="1204" y="99" font-size="18" text-anchor="end" fill="#B8B4AC">PROJECT PORTFOLIO</text>
{texts}
<rect x="76" y="475" width="195" height="39" rx="19" fill="#D4AF65"/>
<text x="173" y="501" font-size="15" font-weight="700" text-anchor="middle" fill="#090909">EXPLORE THE SOURCE</text>
<text x="291" y="501" font-size="18" fill="#B8B4AC">Code · Documentation · Roadmap</text>
<path d="M76 549H1204" stroke="#3B3324"/>
<text x="76" y="584" font-size="18" fill="#E6D6AF">github.com/harshakavali81-collab</text>
<text x="1204" y="584" font-size="16" text-anchor="end" fill="#B8B4AC">Portfolio project · See README for scope</text>
</g></svg>'''
    out = ROOT / 'assets'
    out.mkdir(exist_ok=True)
    path = out / f"{item['repo']}.svg"
    path.write_text(svg)
    subprocess.run(['inkscape', str(path), '--export-type=png', '--export-filename='+str(path.with_suffix('.png'))], check=True, capture_output=True)

if __name__ == '__main__':
    for item in json.loads((ROOT / 'manifest.json').read_text()):
        render(item)
