#!/usr/bin/env python3
"""Live performance and browser QA: reports explicit measured outcomes, not guesses."""
import os, json, re, time, math, argparse, threading
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit, quote, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed
from playwright.sync_api import sync_playwright
import requests

ROOT=Path(__file__).resolve().parents[1]
BASE="https://harshakavali81-collab.github.io/harshavardhan-portfolio/"
PAGES=["","flagship-projects.html","certificates.html","portfolio-readiness.html","career-portfolio.html","work.html","job-platforms.html","linkedin-projects.html","evidence.html","engineering.html","proof-map.html","profile.html","recruiter.html","resumes.html","resume.html","data-analyst-resume.html","contact.html","hiring.html","interview.html","quality.html"]+["cases/"+n+".html" for n in ["ecommerce","transactionshield","demandpilot","evidencedesk","zomato"]]
PERF=["","flagship-projects.html","certificates.html","portfolio-readiness.html","career-portfolio.html","work.html","job-platforms.html","evidence.html","engineering.html","proof-map.html","hiring.html","interview.html","profile.html","contact.html","resumes.html","quality.html","cases/demandpilot.html","cases/transactionshield.html"]
# Release sentinels distinguish the current career release from an older HTTP-200 Pages version.
CURRENT_RELEASE_MARKERS={
    "index.html":'id="career-12"',
    "career-portfolio.html":'id="twelve-elements"',
    "portfolio-readiness.html":'id="proof-policy"',
    "certificates.html":'id="certificates"',
    "flagship-projects.html":'id="fraud"',
    "resume.html":'class="kh-resume-screen"',
    "data-analyst-resume.html":'class="kh-resume-screen"',
}
NOW=lambda:datetime.now(timezone.utc).isoformat()

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        for key in ("href","src"):
            u=d.get(key)
            if u and urlsplit(u).scheme in ("http","https"):
                self.links.append(u)

def check_links(out):
    all_urls={}
    for f in sorted(ROOT.glob("*.html")) + sorted((ROOT / "cases").glob("*.html")):
        p=Links();p.feed(f.read_text(encoding="utf-8"))
        for url in p.links:
            all_urls.setdefault(url,set()).add(f.relative_to(ROOT).as_posix())
    token=os.environ.get("GITHUB_TOKEN","")
    def check(url):
        host=urlsplit(url).hostname or ""
        parts=unquote(urlsplit(url).path).strip("/").split("/")
        target=url
        via="http"
        if host=="github.com" and len(parts)>=2:
            if len(parts)>4 and parts[2] in ("blob","tree") and parts[3] in ("main","master"):
                target="https://api.github.com/repos/"+quote(parts[0])+"/"+quote(parts[1])+"/contents/"+quote("/".join(parts[4:]),safe="/")+"?ref="+quote(parts[3])
                via="github-file-api"
            else:
                target="https://api.github.com/repos/"+quote(parts[0])+"/"+quote(parts[1])
                via="github-repo-api"
        elif host=="github.com" and len(parts)==1:
            target="https://api.github.com/users/"+quote(parts[0]);via="github-user-api"
        elif host=="raw.githubusercontent.com" and len(parts)>=4:
            target="https://api.github.com/repos/"+quote(parts[0])+"/"+quote(parts[1])+"/contents/"+quote("/".join(parts[3:]),safe="/")+"?ref="+quote(parts[2]);via="github-asset-api"
        r={"url":url,"pages":sorted(all_urls[url]),"via":via}
        try:
            headers={"User-Agent":"KHPortfolio-QA","Accept":"application/vnd.github+json"}
            if token and target.startswith("https://api.github.com/"):
                headers["Authorization"]="Bearer "+token
            resp=requests.get(target,headers=headers,timeout=18,allow_redirects=True,stream=True)
            code=resp.status_code;resp.close()
            r["status"]=code
            r["result"]="ok" if 200<=code<400 else "broken" if code in (404,410) else "unknown" if code in (401,403,429,999) else "http-error"
        except requests.RequestException as e:
            r.update({"result":"unknown","error":str(e)[:150]})
        return r
    external=[]
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures=[pool.submit(check,u) for u in all_urls]
        for f in as_completed(futures):
            external.append(f.result())
    external.sort(key=lambda a:a["url"])
    live=[]
    for p in PAGES:
        try:
            r=requests.get(BASE+p,timeout=22,headers={"User-Agent":"KHPortfolio-QA"})
            page_name=p or "index.html"
            expected=CURRENT_RELEASE_MARKERS.get(page_name)
            # Cache-busting/retry only for release-specific pages. A public 200
            # without current content is not a passing deployment check.
            release_ok=(expected is None or expected in r.text) and r.status_code==200
            if expected and not release_ok:
                for _ in range(4):
                    time.sleep(8)
                    try:
                        r=requests.get(BASE+p+"?kh-release="+str(os.environ.get("GITHUB_SHA","20261028")),timeout=22,headers={"User-Agent":"KHPortfolio-QA","Cache-Control":"no-cache"})
                        release_ok=r.status_code==200 and expected in r.text
                        if release_ok: break
                    except requests.RequestException:
                        pass
            live.append({"page":page_name,"status":r.status_code,"bytes":len(r.content),
                         "ok":r.status_code==200 and release_ok,
                         "current_release_marker":release_ok if expected else None})
        except requests.RequestException as e:
            live.append({"page":p or "index.html","ok":False,"error":str(e)[:170]})
    summary={k:sum(x["result"]==k for x in external) for k in ("ok","broken","unknown","http-error")}
    result={"checked_at":NOW(),"live_pages":live,"external":external,"external_counts":summary}
    (out/"external-links.json").write_text(json.dumps(result,indent=2))
    return result

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass

def browser_qa(out):
    import functools
    server=ThreadingHTTPServer(("127.0.0.1",0),functools.partial(Quiet,directory=str(ROOT)))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    base="http://127.0.0.1:"+str(server.server_port)+"/"
    profiles=[("chromium","desktop",1440,900),("chromium","tablet",768,1024),("chromium","mobile",390,844),("chromium","small-mobile",320,700),("firefox","desktop",1440,900),("firefox","mobile",390,844),("webkit","desktop",1440,900),("webkit","mobile",390,844)]
    shots=out/"screenshots";shots.mkdir(exist_ok=True)
    evidence_entries=json.loads((ROOT/"data/project-evidence.json").read_text(encoding="utf-8"))["entries"]
    expected_evidence_count=len(evidence_entries)
    expected_ml_count=sum(row["discipline"]=="ml" for row in evidence_entries)
    assert expected_evidence_count>=5, "Evidence dataset unexpectedly small"
    cases=[];issues=[]
    try:
        with sync_playwright() as p:
            for engine,label,w,h in profiles:
                browser=None
                try:
                    browser=getattr(p,engine).launch(headless=True)
                    context=browser.new_context(viewport={"width":w,"height":h},device_scale_factor=1,
                      is_mobile=label in ("mobile","small-mobile") and engine!="firefox",
                      has_touch=label in ("mobile","small-mobile"))
                    for path in PAGES:
                        page=context.new_page()
                        res={"engine":engine,"profile":label,"page":path or "index.html"}
                        try:
                            response=page.goto(base+path,wait_until="domcontentloaded",timeout=25000)
                            if not response or response.status!=200: raise AssertionError("HTTP not 200")
                            # DOMContentLoaded does not guarantee imported fonts/styles have
                            # finished; wait for real theme variables, never an arbitrary pause.
                            try:
                                page.wait_for_function("""() => {
                                    const s = getComputedStyle(document.body);
                                    return s.getPropertyValue('--bg').trim() === '#080808' &&
                                           s.getPropertyValue('--accent').trim() === '#d4af37';
                                }""", timeout=12000)
                            except Exception as ex:
                                raise AssertionError("Premium theme did not apply within 12 seconds") from ex
                            metrics=page.evaluate("""() => ({
                               scroll:document.documentElement.scrollWidth,
                               width:window.innerWidth,
                               h1:!!document.querySelector('h1'),
                               anchors:document.querySelectorAll('a[href]').length
                            })""")
                            res.update({"scroll_width":metrics["scroll"],"viewport_width":metrics["width"]})
                            if not metrics["h1"] or metrics["anchors"]<2:raise AssertionError("Missing heading or navigation")
                            if metrics["scroll"]>metrics["width"]+3:raise AssertionError("horizontal overflow: "+str(metrics))
                            if page.locator('link[href$="luxury-theme.css"]').count()!=1:
                                raise AssertionError("Premium theme stylesheet link not found")
                            branding = page.evaluate("""() => {
                               const body = getComputedStyle(document.body);
                               const title = document.querySelector('main h1');
                               return {
                                 backgroundToken: body.getPropertyValue('--bg').trim(),
                                 goldToken: body.getPropertyValue('--accent').trim(),
                                 titleFoil: title ? getComputedStyle(title).backgroundImage : ''
                               };
                            }""")
                            if branding["backgroundToken"] != "#080808":
                                raise AssertionError("Obsidian black background token was not applied: "+str(branding))
                            if branding["goldToken"] != "#d4af37":
                                raise AssertionError("Champagne gold accent token was not applied: "+str(branding))

                            if path=="flagship-projects.html":
                                if page.locator(".kh-flagship").count()!=3:
                                    raise AssertionError("Three role-focused flagship projects missing")
                                if page.locator(".kh-spec").count()!=57:
                                    raise AssertionError("All 19 fields per flagship project required")
                                if page.locator("#zomato a[href*='github.com/']").count()<1:
                                    raise AssertionError("Zomato evidence source missing")
                                body_color=page.locator("body").evaluate("e=>getComputedStyle(e).backgroundColor")
                                if body_color!="rgb(8, 8, 8)":
                                    raise AssertionError("Flagship palette is no longer black/gold")
                            if path=="certificates.html":
                                if page.locator(".kh-proof-card").count()!=7:
                                    raise AssertionError("Seven document-backed training records required")
                                for link in ("https://www.credly.com/go/tfTqbAM0",
                                             "https://www.credly.com/go/GqcOmj3t"):
                                    if page.locator("a[href='"+link+"']").count()!=1:
                                        raise AssertionError("AWS Academy Credly link missing: "+link)
                                back_color=page.locator("body").evaluate("e=>getComputedStyle(e).backgroundColor")
                                if back_color!="rgb(8, 8, 8)":
                                    raise AssertionError("Credential gallery black theme regression: "+back_color)
                            if path=="portfolio-readiness.html":
                                if page.locator(".kh-ready-section").count()!=5:
                                    raise AssertionError("Five recruiter portfolio checklist categories required")
                                if page.locator(".kh-ready-section li").count()!=32:
                                    raise AssertionError("Exactly 32 portfolio checks must be shown")
                                color_values=page.locator("body").evaluate("""e => {
                                    const s=getComputedStyle(e);
                                    const first=getComputedStyle(document.querySelector('.kh-ready-card'));
                                    return [s.backgroundColor,first.backgroundColor]
                                }""")
                                if color_values!=["rgb(8, 8, 8)","rgb(8, 8, 8)"]:
                                    raise AssertionError("Recruiter readiness page broke two-color theme: "+str(color_values))
                            if path=="career-portfolio.html":
                                if page.locator(".kh-element").count()!=12:
                                    raise AssertionError("Twelve documented career elements must be visible")
                                if page.locator(".kh-case").count()!=5:
                                    raise AssertionError("Five recruiter case studies must be present")
                                if page.locator("a[href='profile.html#beyond']").count()!=1:
                                    raise AssertionError("Hobbies / interests link is missing")
                                if page.locator("a[href='job-platforms.html']").count()<1:
                                    raise AssertionError("Job-platform profile hub is missing")
                            if path in ("resume.html","data-analyst-resume.html"):
                                resume_colors=page.evaluate("""() => ({
                                  bg:getComputedStyle(document.body).backgroundColor,
                                  paper:getComputedStyle(document.querySelector('.paper')).backgroundColor,
                                  printText:document.querySelector('.paper').innerText.length
                                })""")
                                if resume_colors["bg"]!="rgb(8, 8, 8)":
                                    raise AssertionError("HTML resume screen background is not black: "+str(resume_colors))
                                if resume_colors["printText"]<200:
                                    raise AssertionError("Resume content missing")
                            if path.startswith("cases/"):
                                for part in ("overview","problem","process","solution","results","reflection"):
                                    if page.locator("#"+part).count()!=1:raise AssertionError("missing section "+part)
                            if path=="job-platforms.html":
                                if page.locator(".platform-panel").count()!=3:
                                    raise AssertionError("Expected LinkedIn, Naukri and foundit profiles")
                                if page.locator(".project").count()!=31:
                                    raise AssertionError("Expected 31 repository cards")
                                if page.locator(".catalog li").count()!=31:
                                    raise AssertionError("Expected 31 GitHub repositories")
                                page.locator("#project-scope").select_option("featured")
                                if page.locator(".project:not([hidden])").count()!=15:
                                    raise AssertionError("Featured filter must show 15")
                                page.locator("#project-scope").select_option("additional")
                                if page.locator(".project:not([hidden])").count()!=16:
                                    raise AssertionError("Additional filter must show 16")
                                page.locator("#project-scope").select_option("All")
                                if page.locator(".project:not([hidden])").count()!=31:
                                    raise AssertionError("All projects filter must show 31")
                                page.locator("#tab-naukri").click()
                                if page.locator("#panel-naukri").is_hidden():
                                    raise AssertionError("Naukri profile tab failed")
                                page.locator("#tab-foundit").click()
                                if page.locator("#panel-foundit").is_hidden():
                                    raise AssertionError("foundit profile tab failed")
                                page.locator("#tab-linkedin").click()
                                page.locator("#category").select_option("Analytics & BI")
                                selected=page.locator(".project:not([hidden])")
                                if selected.count()!=8:
                                    raise AssertionError("Analytics category should show eight projects")
                                page.locator("#category").select_option("All")
                                if page.locator(".project:not([hidden])").count()!=31:
                                    raise AssertionError("Clearing project filter did not restore 31 project cards")
                                page.locator("#project-search").fill("zomato")
                                if page.locator(".project:not([hidden])").count()!=1:
                                    raise AssertionError("Project search failed")
                                page.locator("#project-search").fill("")
                                if page.locator(".project:not([hidden])").count()!=31:
                                    raise AssertionError("Project search reset failed")
                            if path=="linkedin-projects.html":
                                if page.locator(".project-card").count()!=31:
                                    raise AssertionError("LinkedIn project showcase should contain 31 cards")
                                page.locator("#scope").select_option("featured")
                                if page.locator(".project-card:not([hidden])").count()!=15:
                                    raise AssertionError("LinkedIn featured filter incorrect")
                                page.locator("#scope").select_option("additional")
                                if page.locator(".project-card:not([hidden])").count()!=16:
                                    raise AssertionError("LinkedIn other filter incorrect")
                                page.locator("#scope").select_option("All")
                                if page.locator(".project-card:not([hidden])").count()!=31:
                                    raise AssertionError("LinkedIn all filter incorrect")
                            if path=="work.html":
                                page.wait_for_function(
                                    "() => document.documentElement.dataset.workFiltersReady === 'true'",
                                    timeout=5000)
                                data_filter=page.locator("button[data-filter='Data']")
                                if engine=="webkit" and label=="mobile":
                                    data_filter.tap()
                                else:
                                    data_filter.click()
                                try:
                                    page.wait_for_function("""() => {
                                      const selected = document.querySelector('[data-filter="Data"]');
                                      const cards = [...document.querySelectorAll('.case-card')];
                                      return selected?.getAttribute('aria-pressed') === 'true' &&
                                        cards.filter(c => !c.hasAttribute('hidden')).length === 2 &&
                                        cards.filter(c => !c.hasAttribute('hidden')).every(c => c.dataset.type === 'Data') &&
                                        cards.filter(c => c.hasAttribute('hidden')).length === cards.length - 2;
                                    }""", timeout=5000)
                                except Exception:
                                    visible=page.locator(".case-card:not([hidden])").count()
                                    pressed=data_filter.get_attribute("aria-pressed")
                                    diagnostics=page.evaluate("""() => ({
                                      ready:document.documentElement.dataset.workFiltersReady,
                                      selected:document.querySelector('[data-filter="Data"]')?.getAttribute('aria-pressed'),
                                      resources:performance.getEntriesByType('resource')
                                        .filter(r=>r.name.includes('work-filters.js')).map(r=>r.responseStatus || 'loaded')
                                    })""")
                                    raise AssertionError(
                                        f"Work Data filter did not settle: visible={visible}, selected={pressed}, details={diagnostics}")
                                if engine=="webkit" and label=="mobile":
                                    page.locator("button[data-filter='All']").tap()
                                else:
                                    page.locator("button[data-filter='All']").click()
                                page.wait_for_function("""() => {
                                    const cards=[...document.querySelectorAll('.case-card')];
                                    return cards.length >= 5 && cards.every(c=>!c.hasAttribute('hidden'));
                                }""", timeout=5000)
                            if path=="":
                                stats=page.locator(".bh-stats")
                                if stats.count()!=1:
                                    raise AssertionError("Homepage facts strip missing")
                                colors=stats.evaluate("""e => {
                                    const cs=getComputedStyle(e);
                                    const first=getComputedStyle(e.querySelector('.bh-stat strong'));
                                    return [cs.backgroundColor,first.color]
                                }""")
                                if colors!=["rgb(8, 8, 8)","rgb(212, 175, 55)"]:
                                    raise AssertionError("Two-color homepage statistics strip regression: "+str(colors))
                                if page.locator("#recruiter-contact a[href^='tel:']").count()!=1:
                                    raise AssertionError("Recruiter direct phone shortcut missing")
                            if path=="":
                                page.locator("button[data-role='Data Analyst']").click()
                                if "data-analyst-resume.html" not in (page.locator("#role-resume").get_attribute("href") or ""):
                                    raise AssertionError("Data Analyst role routing")
                            if path=="":
                                role_buttons=page.locator("button[data-role]")
                                if role_buttons.count()!=3:
                                    raise AssertionError("Expected three working role-selector buttons")
                                page.locator("button[data-role='AI / ML']").click()
                                if "resume.html" not in (page.locator("#role-resume").get_attribute("href") or ""):
                                    raise AssertionError("AI / ML resume routing failed")
                                if page.locator("#role-title").inner_text()!="AI / ML":
                                    raise AssertionError("AI / ML heading did not update")
                                page.locator("button[data-role='Python Developer']").click()
                                if "Python" not in page.locator("#role-title").inner_text():
                                    raise AssertionError("Python role selector failed")
                                page.locator("button[data-role='Data Analyst']").click()
                            if path=="proof-map.html":
                                page.locator("button[data-role='ml']").click()
                                if page.locator("#role-heading").inner_text()!="AI / Machine Learning":
                                    raise AssertionError("AI/ML proof map heading failed to switch")
                                if page.locator(".proof-item").count()!=3:
                                    raise AssertionError("AI/ML evidence count should be three")
                                if "AIML_DataAnalyst_Resume.pdf" not in (page.locator("#role-cv").get_attribute("href") or ""):
                                    raise AssertionError("AI/ML resume link missing")
                                page.locator("button[data-role='data']").click()
                                if page.locator(".proof-item").count()!=2:
                                    raise AssertionError("Data analyst evidence count should be two")
                            if path=="evidence.html":
                                page.locator("#ledger-app[data-ready='true']").wait_for(timeout=12000)
                                if page.locator(".ledger-card").count()!=expected_evidence_count:
                                    raise AssertionError("Evidence count does not match project register")
                                page.locator("button[data-ledger-filter='ml']").click()
                                if page.locator(".ledger-card").count()!=expected_ml_count:
                                    raise AssertionError("ML evidence filter count does not match project register")
                                page.locator("#compare-b").select_option("transactionshield")
                                if page.locator("#comparison-results article").count()!=2:
                                    raise AssertionError("The side-by-side evidence comparison did not render")
                                if "TransactionShield" not in page.locator("#comparison-results").inner_text():
                                    raise AssertionError("Selected comparison was not updated")
                            if path=="engineering.html":
                                for adr in ("adr-ecommerce","adr-fraud","adr-forecast","adr-rag","adr-bi"):
                                    if page.locator("#"+adr).count()!=1:
                                        raise AssertionError("Missing engineering decision "+adr)
                            if path=="hiring.html":
                                if page.locator(".faq details").count()!=10:
                                    raise AssertionError("recruiter FAQ count should be ten")
                                page.locator(".faq details").nth(1).locator("summary").click()
                                if not page.locator(".faq details").nth(1).evaluate("d => d.open"):
                                    raise AssertionError("FAQ keyboard/mouse disclosure failed")
                                if page.locator("a[href='interview.html']").count()<1:
                                    raise AssertionError("interview link missing")
                            if path=="interview.html":
                                if page.locator("article.story").count()!=5:
                                    raise AssertionError("five interview project stories expected")
                                page.locator("article.story").first.locator("summary").click()
                                if not page.locator("article.story").first.locator("details").evaluate("d => d.open"):
                                    raise AssertionError("interview question disclosure failed")
                            if path=="contact.html":
                                if page.locator("form#mail-form").count()!=1:
                                    raise AssertionError("Contact form missing")
                                if page.locator("a[href*='mail.google.com/mail/?']").count()<1:
                                    raise AssertionError("Optional direct Gmail compose link missing")
                                if page.locator("a[href^='mailto:']").count()<1:
                                    raise AssertionError("Email app link missing")
                                for button_id in ("#copy-email","#copy-message","#open-mail-app"):
                                    if page.locator(button_id).count()!=1:
                                        raise AssertionError("Contact fallback missing: "+button_id)
                                page.locator("#copy-email").click()
                                page.locator("#copy-status").wait_for(state="visible", timeout=5000)
                                if not page.locator("#copy-status").inner_text().strip():
                                    raise AssertionError("Copy-email feedback missing")
                                context.route("https://mail.google.com/**",
                                    lambda route: route.fulfill(status=200, content_type="text/html",
                                        body="<html><title>Gmail test route</title><body>Gmail preview</body></html>"))
                                page.locator("#sender").fill("Portfolio QA")
                                page.locator("#reply").fill("qa@example.com")
                                page.locator("#message").fill("Please review this project portfolio.")
                                with page.expect_popup(timeout=13000) as popup_info:
                                    page.locator("#open-gmail").click()
                                popup=popup_info.value
                                popup.wait_for_url("https://mail.google.com/mail/**", timeout=13000)
                                from urllib.parse import parse_qs
                                gmail_query=parse_qs(urlsplit(popup.url).query)
                                if gmail_query.get("to")!=["kavaliharshavardhan98@gmail.com"]:
                                    raise AssertionError("Gmail draft recipient incorrect")
                                if gmail_query.get("view")!=["cm"] or gmail_query.get("fs")!=["1"]:
                                    raise AssertionError("Gmail compose routing missing")
                                if "Portfolio QA" not in gmail_query.get("su", [""])[0]:
                                    raise AssertionError("Gmail draft subject missing sender")
                                if "Please review this project portfolio." not in gmail_query.get("body", [""])[0]:
                                    raise AssertionError("Gmail draft body was not encoded correctly")
                                popup.close()
                                page.locator("#copy-message").click()
                                page.locator("#mail-status").wait_for(state="visible",timeout=5000)
                                if not page.locator("#mail-status").inner_text().strip():
                                    raise AssertionError("Complete copy feedback missing")
                                if page.locator("form#mail-form").count()!=1:
                                    raise AssertionError("Contact page lost after popup draft handoff")
                            res["result"]="pass"
                            if (engine,label,path) in [
                               ("chromium","desktop",""),("chromium","mobile",""),("chromium","tablet","work.html"),
                               ("chromium","mobile","contact.html"),("chromium","desktop","career-portfolio.html"),
                               ("chromium","mobile","career-portfolio.html"),("chromium","desktop","portfolio-readiness.html"),("chromium","mobile","portfolio-readiness.html"),("chromium","desktop","certificates.html"),("chromium","mobile","certificates.html"),("chromium","desktop","flagship-projects.html"),("chromium","mobile","flagship-projects.html"),("webkit","mobile","career-portfolio.html"),("webkit","mobile",""),
                               ("webkit","mobile","profile.html"),("firefox","desktop","cases/demandpilot.html")]:
                                file=engine+"-"+label+"-"+(path.replace("/","-") or "home")+".png"
                                page.screenshot(path=str(shots/file),full_page=not (engine=="webkit" and label=="mobile" and path==""),animations="disabled",timeout=20000)
                                res["screenshot"]="screenshots/"+file
                        except Exception as ex:
                            res.update({"result":"fail","reason":str(ex)[:250]});issues.append(res)
                        cases.append(res)
                        page.close()
                    context.close()
                except Exception as ex:
                    issues.append({"engine":engine,"profile":label,"result":"fail","reason":str(ex)[:250]})
                finally:
                    if browser:browser.close()
    finally:
        server.shutdown();server.server_close()
    result={"checked_at":NOW(),"profiles":profiles,"checks":cases,"passed":sum(x["result"]=="pass" for x in cases),"total":len(cases),"issues":issues}
    (out/"device-browser.json").write_text(json.dumps(result,indent=2))
    return result

def quantile75(a):
    a=sorted(a);n=len(a);index=.75*(n-1);i=int(index)
    return a[i]+(a[min(i+1,n-1)]-a[i])*(index-i)

def performance_qa(out):
    records=[];failures=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        for profile in ("desktop","mobile-fast4g"):
            for path in PERF:
                samples=[]
                for i in range(3):
                    context=browser.new_context(viewport={"width":1440 if profile=="desktop" else 390,"height":900 if profile=="desktop" else 844},is_mobile=profile!="desktop",has_touch=profile!="desktop")
                    context.add_init_script("""(() => {window.__lcp=0; try {new PerformanceObserver(x=>{for(const e of x.getEntries())window.__lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true})}catch(e){}})();""")
                    page=context.new_page()
                    try:
                        if profile!="desktop":
                            c=context.new_cdp_session(page)
                            c.send("Network.enable")
                            c.send("Network.setCacheDisabled",{"cacheDisabled":True})
                            c.send("Network.emulateNetworkConditions",{"offline":False,"latency":120,"downloadThroughput":200000,"uploadThroughput":75000,"connectionType":"cellular4g"})
                            c.send("Emulation.setCPUThrottlingRate",{"rate":4})
                        r=page.goto(BASE+path,wait_until="load",timeout=35000)
                        if not r or r.status!=200:raise RuntimeError("HTTP "+str(r.status if r else "missing"))
                        m=page.evaluate("""() => {const t=performance.getEntriesByType('navigation')[0];return {load_ms:Math.round(t.loadEventEnd-t.startTime), domcontentloaded_ms:Math.round(t.domContentLoadedEventEnd-t.startTime),lcp_ms:Math.round(window.__lcp||0)}}""")
                        samples.append(m)
                    except Exception as ex:
                        failures.append({"profile":profile,"page":path or "index.html","sample":i+1,"error":str(ex)[:200]})
                    finally:
                        context.close()
                p75=round(quantile75([x["load_ms"] for x in samples]),1) if len(samples)==3 else None
                records.append({"profile":profile,"page":path or "index.html","samples":samples,"p75_load_ms":p75,"under_3_seconds":bool(p75 is not None and p75<3000)})
        browser.close()
    result={"checked_at":NOW(),"definition":"Chromium live HTTPS page navigation load event; 3 cold independent contexts per page; p75 < 3000ms","target_ms":3000,
       "desktop":"GitHub hosted runner network; no artificial throttling",
       "mobile":"390px; 120ms RTT, 1.6Mbps down, 0.6Mbps up, CPU 4x slowdown",
       "records":records,"errors":failures,"target_met":all(r["under_3_seconds"] for r in records) and not failures,
       "limits":"Simulated mobile, not representative of all locations, physical devices, ISPs or every visit. First-content paints and LCP available in navigation observations."}
    (out/"performance.json").write_text(json.dumps(result,indent=2))
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",default="qa-out")
    args=parser.parse_args();out=Path(args.output).resolve();out.mkdir(parents=True,exist_ok=True)
    links=check_links(out);dev=browser_qa(out);perf=performance_qa(out)
    counts=links["external_counts"]
    lines=["# Portfolio verification results","",
      "Generated UTC: "+NOW(),"",
      "## Direct checks",
      "- Live and current-release URL checks: "+str(sum(x["ok"] for x in links["live_pages"]))+"/"+str(len(links["live_pages"])),
      "- External links: "+str(counts["ok"])+" reachable; "+str(counts["broken"])+" broken; "+str(counts["unknown"])+" access-limited/unknown; "+str(counts["http-error"])+" HTTP errors",
      "- Chromium, Firefox and WebKit viewport tests: "+str(dev["passed"])+"/"+str(dev["total"])+" passed",
      "- Live site load under 3 seconds (p75 for every critical URL, desktop and simulated 4G mobile): "+("PASS" if perf["target_met"] else "FAIL / NOT VERIFIED"),"",
      "## Performance: p75 page-load event, 3 cold contexts per case","",
      "| Page | Desktop ms | Simulated 4G mobile ms |","|---|---:|---:|"]
    for path in PERF:
        label=path or "index.html"
        m={x["profile"]:x["p75_load_ms"] for x in perf["records"] if x["page"]==label}
        lines.append("| "+label+" | "+str(m.get("desktop"))+" | "+str(m.get("mobile-fast4g"))+" |")
    lines+=["","## Limits","- All measured timings are from GitHub-hosted runners, not universal user experiences.","- External sites returning 401/403/429/999 or network errors are marked unknown, not incorrectly marked working.","- Internal links and target files are separately checked by the existing static-site audit.","- Browser checks use local-hosted copies of repository files. Live HTTP and performance checks use public GitHub Pages.","- screenshots/ contains representative desktop, tablet and mobile browser renders.",""]
    (out/"SUMMARY.md").write_text("\n".join(lines),encoding="utf-8")
    print((out/"SUMMARY.md").read_text(encoding="utf-8"))
    problems=[]
    if not all(x["ok"] for x in links["live_pages"]):problems.append("Live pages unreachable")
    if counts["broken"] or counts["http-error"]:problems.append("Broken or HTTP-failed external URLs")
    if dev["issues"]:problems.append("Browser/viewport functional failures")
    if not perf["target_met"]:problems.append("Under-3-seconds benchmark not satisfied")
    if problems:
        print("QA failed:",", ".join(problems))
        return 1
    print("QA passed for the defined browser, external-link and performance checks.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
