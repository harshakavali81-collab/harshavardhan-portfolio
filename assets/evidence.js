(() => {
  "use strict";
  const root = document.getElementById("ledger-app");
  if (!root) return;
  const board = document.getElementById("ledger-cards");
  const selectA = document.getElementById("compare-a");
  const selectB = document.getElementById("compare-b");
  const comparison = document.getElementById("comparison-results");
  const status = document.getElementById("ledger-status");
  const count = document.getElementById("ledger-count");
  const buttons = [...document.querySelectorAll("[data-ledger-filter]")];
  let entries = [];
  let filter = "all";
  const make = (tag, classes, value) => {
    const element = document.createElement(tag);
    if (classes) element.className = classes;
    if (value !== undefined) element.textContent = value;
    return element;
  };
  const link = (href, text) => {
    const a = make("a", "", text);
    a.href = href;
    if (href.startsWith("https://")) {
      a.target = "_blank";
      a.rel = "noopener noreferrer";
    }
    return a;
  };
  function tags(parent, values) {
    const box = make("div", "ledger-tags");
    for (const item of values) box.append(make("span", "", item));
    parent.append(box);
  }
  function drawCards() {
    const visible = entries.filter(e => filter === "all" || e.discipline === filter);
    board.replaceChildren();
    for (const item of visible) {
      const article = make("article", "ledger-card");
      article.dataset.slug = item.slug;
      article.append(make("div", "eyebrow", item.role));
      article.append(make("h3", "", item.title));
      article.append(make("p", "", item.question));
      tags(article, item.stack);
      const metric = make("div", "metric");
      metric.append(make("strong", "", item.metric));
      metric.append(make("span", "", item.metricLabel));
      article.append(metric);
      article.append(make("p", "", item.metricDetail));
      article.append(make("div", "smallcap", "What the result does not prove"));
      article.append(make("p", "", item.limitations));
      article.append(make("div", "ledger-status", item.claimLevel));
      const links = make("div", "ledger-source");
      links.append(link(item.casePage, "Deep case study ↗"));
      links.append(link(item.evidence, "Original evidence ↗"));
      links.append(link(item.source, "Repository ↗"));
      article.append(links);
      board.append(article);
    }
    count.textContent = visible.length + " of " + entries.length + " projects shown";
    buttons.forEach(btn => btn.setAttribute("aria-pressed", String(btn.dataset.ledgerFilter === filter)));
  }
  function addDetail(dl, label, value) {
    dl.append(make("dt", "", label));
    dl.append(make("dd", "", value));
  }
  function drawCompare() {
    comparison.replaceChildren();
    const a = entries.find(x => x.slug === selectA.value);
    const b = entries.find(x => x.slug === selectB.value);
    if (!a || !b) {
      status.textContent = "Choose both projects to compare.";
      return;
    }
    if (a.slug === b.slug) {
      status.textContent = "Select two different projects for a useful comparison.";
      return;
    }
    const both = [a, b];
    for (const item of both) {
      const card = make("article", "");
      card.append(make("div", "eyebrow", item.role));
      card.append(make("h3", "", item.title));
      const dl = make("dl", "");
      addDetail(dl, "Core engineering question", item.question);
      addDetail(dl, "Input and evaluation population", item.sample);
      addDetail(dl, "Test / metric", item.metric + " — " + item.metricLabel + ". " + item.metricDetail);
      addDetail(dl, "Validation", item.test);
      addDetail(dl, "Technical trade-off", item.tradeoff);
      addDetail(dl, "Limitations", item.limitations);
      addDetail(dl, "Next reproducible check", item.reviewNext);
      card.append(dl);
      const src = make("div", "ledger-source");
      src.append(link(item.casePage, "Case study ↗"));
      src.append(link(item.evidence, "Evidence ↗"));
      card.append(src);
      comparison.append(card);
    }
    const u = new URL(location.href);
    u.searchParams.set("a", a.slug);
    u.searchParams.set("b", b.slug);
    history.replaceState(null, "", u);
    status.textContent = a.title + " and " + b.title + " compared; each result includes context and limitations.";
  }
  async function init() {
    try {
      const response = await fetch("data/project-evidence.json", {cache: "no-cache"});
      if (!response.ok) throw new Error("HTTP " + response.status);
      const payload = await response.json();
      if (!Array.isArray(payload.entries) || payload.entries.length < 5) throw new Error("Incomplete evidence register");
      entries = payload.entries;
      const params = new URLSearchParams(location.search);
      for (const item of entries) {
        selectA.append(new Option(item.title, item.slug));
        selectB.append(new Option(item.title, item.slug));
      }
      const valid = value => entries.some(item => item.slug === value);
      selectA.value = valid(params.get("a")) ? params.get("a") : "ecommerce";
      selectB.value = valid(params.get("b")) ? params.get("b") : "demandpilot";
      buttons.forEach(button => button.addEventListener("click", () => {
        filter = button.dataset.ledgerFilter;
        drawCards();
      }));
      document.getElementById("compare-submit").addEventListener("click", drawCompare);
      selectA.addEventListener("change", drawCompare);
      selectB.addEventListener("change", drawCompare);
      drawCards();
      drawCompare();
      root.dataset.ready = "true";
      status.textContent = "Register loaded: " + entries.length + " source-backed projects and two-project comparison ready.";
    } catch (error) {
      root.dataset.ready = "false";
      status.textContent = "The interactive register could not load. Use the direct project links below or download the source JSON.";
      console.warn("Portfolio evidence register unavailable:", error);
    }
  }
  init();
})();
