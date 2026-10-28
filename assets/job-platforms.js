(()=>{"use strict";
const $=s=>document.getElementById(s);
function choose(name){document.querySelectorAll(".platform-panel").forEach(p=>p.hidden=p.id!=="panel-"+name);
document.querySelectorAll(".tab").forEach(t=>{const on=t.dataset.platform===name;t.setAttribute("aria-selected",String(on));t.tabIndex=on?0:-1});
const url=new URL(location.href);url.searchParams.set("platform",name);history.replaceState(null,"",url);}
async function copy(text){const msg=$("feedback"),fallback=$("manual-copy");fallback.hidden=true;
try{if(!navigator.clipboard?.writeText)throw Error("Clipboard unavailable");await navigator.clipboard.writeText(text);msg.textContent="Copied. Paste into your job portal and save it there."}
catch(_){fallback.value=text;fallback.hidden=false;fallback.focus();fallback.select();msg.textContent="Clipboard unavailable. Select and copy the text shown below.";}}
function filter(){const term=$("project-search").value.toLowerCase().trim(),kind=$("category").value;let n=0;
document.querySelectorAll(".project").forEach(c=>{const good=(kind==="All"||c.dataset.category===kind)&&(!term||c.dataset.search.includes(term));c.hidden=!good;if(good)n++});
$("project-count").textContent=n+" of 15 featured projects";}
document.querySelectorAll(".tab").forEach(t=>t.addEventListener("click",()=>choose(t.dataset.platform)));
document.querySelectorAll("[data-copy]").forEach(b=>b.addEventListener("click",()=>copy($(b.dataset.copy).textContent.trim())));
document.querySelectorAll(".copy-project").forEach(b=>b.addEventListener("click",()=>{const p=b.closest(".project");copy(p.querySelector("h3").textContent+"\n"+p.querySelector(".description").textContent.trim()+"\nSkills: "+p.querySelector(".skilltext").textContent+"\nGitHub: "+p.querySelector(".source").href)}));
$("project-search").addEventListener("input",filter);$("category").addEventListener("change",filter);
const selected=new URLSearchParams(location.search).get("platform");choose(["linkedin","naukri","foundit"].includes(selected)?selected:"linkedin");filter();
})();