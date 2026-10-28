/* Accessible, no-build portfolio interactions. */
(()=>{"use strict";
const header=document.querySelector(".bh-header"),menu=document.querySelector(".bh-menu"),nav=document.querySelector(".bh-nav"),progress=document.querySelector(".bh-progress");
if(menu&&nav){menu.addEventListener("click",()=>{const open=menu.getAttribute("aria-expanded")!=="true";menu.setAttribute("aria-expanded",String(open));nav.classList.toggle("bh-nav-open",open);menu.textContent=open?"Close menu ×":"Menu ☰"});nav.addEventListener("click",event=>{if(event.target.closest("a")){menu.setAttribute("aria-expanded","false");nav.classList.remove("bh-nav-open");menu.textContent="Menu ☰"}});window.addEventListener("keydown",event=>{if(event.key==="Escape"){menu.setAttribute("aria-expanded","false");nav.classList.remove("bh-nav-open");menu.textContent="Menu ☰"}})}
let scrolling=false;window.addEventListener("scroll",()=>{if(scrolling)return;scrolling=true;requestAnimationFrame(()=>{const max=document.documentElement.scrollHeight-innerHeight;progress&&(progress.style.width=(max>0?Math.max(0,Math.min(100,100*scrollY/max)):0)+"%");scrolling=false})},{passive:true});
const search=document.getElementById("bh-search"),scope=document.getElementById("bh-category"),status=document.getElementById("bh-result"),empty=document.getElementById("bh-empty"),cards=[...document.querySelectorAll(".bh-project")];
if(search&&scope&&status&&empty){const filter=()=>{const query=search.value.trim().toLowerCase(),category=scope.value;let count=0;for(const card of cards){const pass=(category==="All"||card.dataset.group===category)&&(!query||(card.dataset.search||"").includes(query));card.hidden=!pass;if(pass)count++}status.textContent="Showing "+count+" of "+cards.length+" repositories";empty.hidden=count!==0};search.addEventListener("input",filter);scope.addEventListener("change",filter);filter()}

/* KH role finder: accessible, explicit CV links and role-specific project evidence. */
const roleDetails={
 "Data Analyst":{desc:"Clean data, build SQL KPIs and explain business patterns through Power BI and Excel dashboards.",skills:"SQL · Excel · Power BI · Python · Pandas · EDA",work:"E-Commerce Sales & Customer Analytics",resume:"data-analyst-resume.html",label:"View Data Analyst resume ↗"},
 "AI / ML":{desc:"Develop and evaluate NLP, retrieval and machine-learning prototypes with clear evidence and limitations.",skills:"Python · scikit-learn · NLP · RAG · model evaluation",work:"EvidenceDesk — Document Q&A",resume:"resume.html",label:"View AI / ML resume ↗"},
 "Python Developer":{desc:"Build maintainable Python services, testable backend APIs and useful automation workflows.",skills:"Python · FastAPI · SQL · Git · REST APIs · testing",work:"TransactionShield — Fraud Risk Scoring",resume:"resume.html",label:"View Python-aligned resume ↗"}
};
const roleButtons=[...document.querySelectorAll("button[data-role]")],roleTitle=document.getElementById("role-title"),roleDesc=document.getElementById("role-desc"),roleSkills=document.getElementById("role-skills"),roleWork=document.getElementById("role-work"),roleResume=document.getElementById("role-resume");
function renderRole(name){
 const r=roleDetails[name];if(!r||!roleTitle||!roleDesc||!roleSkills||!roleWork||!roleResume)return;
 for(const button of roleButtons)button.setAttribute("aria-pressed",String(button.dataset.role===name));
 roleTitle.textContent=name;roleDesc.textContent=r.desc;
 roleSkills.textContent="Skills: "+r.skills;roleWork.textContent="Example: "+r.work;
 roleResume.href=r.resume;roleResume.textContent=r.label;
}
for(const b of roleButtons)b.addEventListener("click",()=>renderRole(b.dataset.role));
if(roleButtons.length)renderRole(roleButtons.find(b=>b.getAttribute("aria-pressed")==="true")?.dataset.role||"Data Analyst");
})();